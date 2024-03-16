#!/usr/bin/env python
# coding: utf-8

# # Amarachi Akunna Onyekachi
# # GEOG 592 Lab 4

# ### Question 1 
# Create a point feature class (shapefile – q1.shp) from the locations.txt file. (4 Points)
# 

# In[ ]:

import arcpy
arcpy.env.workspace = "T:\\Students\\akunna1\\submissions\\Lab_4\\" #workplace location
arcpy.env.overwriteOutput = True

locationFile = open('locations.txt', 'r') #opening text file for the purpose of reading it and giving it a variable name
allLines = locationFile.readlines()[1:] #reading all the lines except the header line

#creating a new shapefile/ feature class 'q1.shp' and adding the field (column) names
# arcpy.CreateFeatureclass_management('outpath','new feature class name','Point')
arcpy.CreateFeatureclass_management(arcpy.env.workspace, 'q1.shp', 'point')#creates a new feature in a geodatabase
arcpy.AddField_management('q1.shp', 'LocationID', 'Text', '','',10) #to add a new field to a feature class or table in a geodatabase

#The insertCursor module function allows you to insert new rows into a feature class or table
#syntax = arcpy.da.InsertCursor(in_table, field_names)
locationCursor = arcpy.da.InsertCursor('q1.shp',['LocationID', 'SHAPE@XY']) #set the template of the shapefile to insert values

for aLine in allLines:
    aListValues = aLine.split(',') #split the columns in the text files with comma ','
    locationID = aListValues[0]
    x_coordinate = float(aListValues[1])
    y_coordinate = float(aListValues[2])
    
    #inserting  the new row for all rows in the text file
    locationCursor.insertRow([LocationID,(x_coordinate,y_coordinate)]) #inserting rows under the field
    
    
#delete locationCursor    
del locationCursor #deleting the cursor to release any locks on the data

#close textfile
locationFile.close() 


# ### Question 2
# In q2.py, calculate the mean center for q1.shp and add the point to q1.shp, save the new shapefile as q2.shp. (4 Points)

import arcpy
arcpy.env.workspace = "T:\\Students\\akunna1\\submissions\\Lab_4\\" #workplace location
arcpy.env.overwriteOutput = True

locationFile = open('locations.txt', 'r') #opening text file for the purpose of reading it and giving it a variable nam
textLines = locationFile.readlines()[1:] #reading all the lines except the header line

arcpy.CreateFeatureclass_management(arcpy.env.workspace, 'q2.shp', 'point') #creates a new feature in a geodatabase
# arcpy.CreateFeatureclass_management('outpath','new feature class name','Point')

arcpy.AddField_management('q2.shp', 'LocationID', 'Text', '','',10)#to add a new field to a feature class or table in a geodatabase

#The insertCursor module function allows you to insert new rows into a feature class or table
#syntax = arcpy.da.InsertCursor(in_table, field_names)
locationCursor = arcpy.da.InsertCursor('q2.shp',['LocationID', 'SHAPE@XY'])  #set the template of the shapefile to insert values

x = 0
y = 0
count = 0
for aLine in textLines:
    aListValues = aLine.split(',')
    LocationID = aListValues[0]
    x_coordinate = float(aListValues[1])
    y_coordinate = float(aListValues[2])
    x=x_coordinate + x
    y=y_coordinate + y
    count = count + 1

    locationCursor.insertRow([LocationID,(x_coordinate,y_coordinate)])  #inserting rows under the field, LocationID

x_mean_center = x/count
y_mean_center = y/count
locationCursor.insertRow(['MeanCenter',(x_mean_center,y_mean_center)])

del locationCursor
locationFile.close()


# ### Question 3
# Write a script (q3.py) to convert oneline.txt into polyline feature class (shapefile). Oneline.txt includes multiple vertices for one polyline object. Each row represents one vertex – 
# 177030005600   904     2.5     206   904         29.409337        -92.888029………...
# The first column represents the polyline’s ID, and last two columns represent a vertex’s latitude and longitude. (4 Points)
# 

# In[ ]:


import arcpy
arcpy.env.workspace = "T:\\Students\\akunna1\\submissions\\Lab_4\\" #workplace location
arcpy.env.overwriteOutput = True

oneline_file = open('oneline.txt', 'r')
text_lines = oneline_file.readlines()

#creating a new polyline feature shapefile
arcpy.CreateFeatureclass_management(arcpy.env.workspace, 'q3.shp', 'polyline')

#adding new field and adding it to the new feature class
arcpy.AddField_management('q3.shp', 'polylineID', 'Text', '','',10)
#Using the InsertCursor tool and adding new fields into the shapefile
polylineCursor = arcpy.da.InsertCursor('q3.shp',['polylineID', 'SHAPE@']) #set the template of the shapefile to insert values

#Creating an empty array
array = arcpy.Array()
points = arcpy.Point()

#looping through each line in the .txt file to get the x,y coordinate and the lineIDs in order to add them to the empty array created
for a_line in text_lines:
    a_list_values = a_line.split()
    lineID = a_list_values[0]
    x_coordinate = float(a_list_values[6])
    y_coordinate = float(a_list_values[5])
    points.X = x_coordinate
    points.Y = y_coordinate
    array.add(points)
    
#creating the polylne with the array points
polyline = arcpy.Polyline(array)


# ### Question 4
# Write a script (q4.py) to convert test.txt into a polyline feature class and save the result to your Lab6 folder. Test.txt contains more than one polyline object. Each polyline object has a unique line ID, such as 177030005600, 177030009200, etc. Please use the Line ID to identify each line segment. You can save the result as a shapefile. Once succeeded, apply your code to allLines.txt, which has thousands of records – more than 20 Mbs. (4 Points)

# In[ ]:


#For test.txt file
import arcpy
arcpy.env.workspace = "T:\\Students\\akunna1\\submissions\\Lab_4\\" #workplace location
arcpy.env.overwriteOutput = True

test_file = open('test.txt', 'r')
test_file_lines = test_file.readlines()

#creating a polyline shapefile 
arcpy.CreateFeatureclass_management(arcpy.env.workspace, 'q4.shp', 'polyline')
#Adding a new field called 'polylineID'
arcpy.AddField_management('q4.shp', 'polylineID', 'Text', '','',10)

#Calling the InsertCursor tool and setting the template to allow addition of new record into the new shapefile 
polylineCursor = arcpy.da.InsertCursor('q4.shp',['polylineID', 'SHAPE@']) #set the template of the shapefile to insert values

#creating an empty array
points = arcpy.Point()
array = arcpy.Array()

#looping through each line in the .txt file and getting the x,y coordinates and the lineIDs
# Then adding them to the empty array
pastID = test_file_lines[0].split()[0] #get first row and first value in the row

for aLine in test_file_lines:
    aList_values = aLine.split()
    lineID =aList_values[0]
    x_coordinate = float(aList_values[6])
    y_coordinate = float(aList_values[5])
    points.X = x_coordinate
    points.Y = y_coordinate
    array.add(points)
    if lineID != pastID:
        polyline = arcpy.Polyline(array)
        polylineCursor.insertRow([lineID, polyline])
        pastID = lineID
        array.removeAll()

del polylineCursor
test_file.close()


# In[ ]:


#for allLines.txt file
import arcpy
arcpy.env.workspace = "T:\\Students\\akunna1\\submissions\\Lab_4\\" #workplace location
arcpy.env.overwriteOutput = True

allLines_file = open('allLines.txt', 'r')
allLines_file_lines = allLines_file.readlines()

#creating a polyline shapefile 
arcpy.CreateFeatureclass_management(arcpy.env.workspace, 'q4_allLines.shp', 'polyline')
#Adding a new field called 'polylineID'
arcpy.AddField_management('q4_allLines.shp', 'polylineID', 'Text', '','',10)

#Calling the InsertCursor tool and setting the template to allow addition of new record into the new shapefile 
polylineCursor = arcpy.da.InsertCursor('q4_allLines.shp',['polylineID', 'SHAPE@'])

#creating an empty array
points = arcpy.Point()
array = arcpy.Array()

#looping through each line in the .txt file and getting the x,y coordinates and the lineIDs
# Then adding them to the empty array
pastID = allLines_file_lines[0].split()[0]
for aLine in allLines_file_lines:
    aList_values = aLine.split()
    lineID =aList_values[0]
    x_coordinate = float(aList_values[6])
    y_coordinate = float(aList_values[5])
    points.X = x_coordinate
    points.Y = y_coordinate
    array.add(points)
    if lineID != pastID:
        polyline = arcpy.Polyline(array)
        polylineCursor.insertRow([lineID, polyline])
        pastID = lineID
        array.removeAll()

del polylineCursor
allLines_file.close()


# ### Question 5
# write a script (q5.py) to perform the following procedures: (4 Points)
# 
# a) List all numerical fields from states2010.shp for a user to choose. For example, <1>POP2000		<2>POP2010		<3>POP00_SQMI …, and the user can choose POP2000 by typing 1 and hit “enter” key.
# 
# ) Once your script receives the input from the user, compute (1) total value of the selected field (2) maximum value of the chosen field (3) average value of the chosen field
# 
# c) Prompt the results to the user.
# 
# d) If there is no “popchg” field, create a “popchg” field for states2010.shp, then calculate population change percentage from 2000 to 2010 for each state and populate this field. To add a field to a feature class, you can use AddField_management function. For examples of using this function, you can search ArcGIS10 desktop help.
# 

# In[ ]:


import arcpy
arcpy.env.workspace = "T:\\Students\\akunna1\\submissions\\Lab_4\\" #workplace location
arcpy.env.overwriteOutput = True

states2010_file = "states2010.shp"

numerical_fields = arcpy.ListFields(states2010_file, "", 'Double') + arcpy.ListFields(states2010_file, "", 'Integer') + arcpy.ListFields(states2010_file, "", 'Float')
#arcpy.ListFields is used to list the fields in a table or feature class. All the numerical fields --> Double, Integer, Float

count = 0

for afield in numerical_fields:
    print("<%d>" % count + afield.name)
    count+=1
    
user_input = int(input("Choose a field by typing the corresponding index number.\n"))
stat_cursor = arcpy.da.SearchCursor(states2010_file, [numerical_fields[user_input].name]) # used to iterate over rows in a table or feature class, and extract specific field values for each row.
total = 0
maximum = -9999999999
count = 0

for aRow in stat_cursor:
    # Calculate total and maximum in the loop
    total=int(aRow[0])+total
    count = count+1
    if aRow[0] > maximum:
        maximum = aRow[0]
average = total/count

#Printing the total, average and maximum values
print("The total = {}".format(total))
print("The average = {}".format(average))
print("The maximum value = {}".format(maximum))

del stat_cursor


# In[ ]:


#Searching for popchg field, if found, do nothing, otherwise, create popchg field, and populate the field
#defining the find_field function
def find_field(field_list, field_name): 
    for field in field_list:
        if field.name == field_name:
            return True
    return False

# Testing to see if the "popchg" field exists
if find_field(numerical_fields, "popchg"):
    print ("popchg field already exists, deleting... ")
    arcpy.DeleteField_management(states2010_file, ["popchg"])

# Adding a float field named "popchg" here
#arcpy.AddField_management('name of shapefile "'field name'", "'field type'","10","3") 
arcpy.AddField_management(states2010_file, "popchg", "FLOAT","10","3")
#calling the rows that I want to work with
rows = arcpy.da.UpdateCursor(states2010_file, ["POP2000","POP2010","popchg"])
for row in rows:
    # Getting pop2000 and pop2010 values, calculating the pop change value (row[2] = ...)
    row[2]=((row[1]-row[0])/row[0])*100
    rows.updateRow(row)
del row, rows


# In[ ]:





# In[ ]:





# In[ ]:




