#Set working directory first to Source File Location

#installing packages
# install.packages("tmap")
# install.packages("rgdal")
# install.packages("raster")
# install.packages("rgeos")
# install.packages("dplyr")
# install.packages("ggspatial")
# install.packages("terra")

#Setting Libraries
#Used in Question 1
library(tidyverse) #for data import, tidying, manipulation, and data visualization
library(sf) #for working with spatial data in a modern, tidy data format.
library(dplyr) #Provides a function for each basic verb of data manipulation
library(tidyr) #Contains tools for changing the shape and hierarchy of a dataset, turning deeply nested lists into rectangular data frames, and extracting values out of string columns
library(data.table) #for fast aggregation of large datasets, low latency add/update/remove of columns, quicker ordered joins, and a fast file reader
library(ggplot2) #Provides helpful commands to create complex plots from data in a data frame
library(viridis)
library(ggspatial)

#Used in Question 2
library(tmap) #to create static maps, interactive maps, and animations
library(rgdal) #for reading, writing, and manipulating geospatial data
library(raster)#for manipulating and analyzing raster data
library(rgeos) #performing a wide variety of geometric operations on spatial data (like geoprocessing tools on ArcGIS)
library(terra)

data(World)
qtm(World)

#Question 1
# reading in shapefile
states <- st_read("STATES.shp")

# reading in gas.csv
gas <- read.csv("gas.csv")

# joining shapefile and csv file by state name columns
joined_data <- left_join(states, gas, by = c("STATE_NAME" = "State"))
#STATE_NAME column is from states (STATES.shp) and  State column is from gas

#creating regular gas price map with ggplot2
ggplot(joined_data) +
  geom_sf(aes(fill = Regular)) +
  scale_fill_gradient(low = "yellow", high = "red") +
  labs(title = "Regular Gas Price by State",
       subtitle = "Data from gas.csv",
       fill = "Price (USD/gallon)",
       caption = "Created by Akunna") +
      theme(plot.title = element_text(hjust = 0.5, face = "bold"))

# Question 2
me <- readOGR("C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_8", "Income")
qtm(me)

me@data #exploring the attribute table
names(me)

tm_shape(me) +
  tm_fill("Income", style="fixed", breaks=c(0,23000 ,27000,100000 ),
          labels=c("Under $23k", "$23K to $27k", "Above $27k"),
          palette="YlOrBr")  +
  tm_borders("grey") +
  tm_legend(outside = TRUE, text.size = .8) +
  tm_layout(frame = FALSE)

Aug_ll <- readOGR("C:\\Users\\akunna1\\Desktop\\GEOG 592\\Lab_8", "Augusta_ll")
proj4string(Aug_ll)
Aug_UTM <- spTransform(Aug_ll, CRS("+init=epsg:26919"))
Aug_UTM <- spTransform(Aug_ll, CRS("+proj=utm +zone=19 +datum=NAD83 +units=m +no_defs +ellps=GRS80 +towgs84=0,0,0"))

d50 <- buffer(Aug_UTM, width=50000, quadsegs=10)
d100 <- buffer(Aug_UTM, width=100000, quadsegs=10)
d150 <- buffer(Aug_UTM, width=150000, quadsegs=10)
d200 <- buffer(Aug_UTM, width=200000, quadsegs=10)
d300 <- buffer(Aug_UTM, width=300000, quadsegs=10)

# Let's check the circles on a Maine outline
tm_shape(d300) +tm_borders() +tm_shape(d200) +tm_borders() +tm_shape(d150) +tm_borders() + tm_shape(d100) +tm_borders()+ tm_shape(d50) +tm_borders() +tm_shape(me) +tm_borders()

dAll <- union(d100, d50)
dAll <- union(d200, d150)
dAll <- union(d300, dAll)

dAll$ID <- 1:length(dAll)
dAllme <- crop(dAll, me)

dAllme$Area_band <- gArea(dAllme, byid=TRUE) / 1000000 # Compute area in km2
qtm(dAllme, fill="Area_band")

clp1 <- intersect(me, dAllme)
tm_shape(clp1) + tm_fill(col="Income") + tm_borders()

clp1$Area_sub <- gArea(clp1, byid=TRUE) / 1000000

# Compute the polygon's fraction vis-a_vis the distance band's area
clp1$frac_area <- clp1$Area_sub / clp1$Area_band

# Mutiply income by area fraction--this is the weighted income 
# within each distance band
clp1$wgt_inc <- clp1$Income * clp1$frac_area

dist_inc <- aggregate(clp1, by="ID",sums= list(list(sum, "wgt_inc")))
qtm(dist_inc, fill="wgt_inc") 