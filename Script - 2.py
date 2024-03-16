#GEOG 592 Lab 2
#Question 1
# Ask a user to input the radius value for a circle,
# Prompt the user with its area and perimeter values
# (Used try-except for error handling, while loop)
from math import pi
#while(True): keeps the loop running infinitely
while(True):
    try:
        radius_circle = float(input('The radius of the circle in cm: '))
        break #needed to be added to come out of the loop
    except ValueError:
        print('Invalid Format! Input a number!')

def area_peri_circle():
    area_circle = pi*radius_circle**2
    perimeter_circle = 2*pi*radius_circle
    print('The area of the circle is', format(area_circle, '.2f'), 'cm².','\nThe perimeter of the circle is',format(perimeter_circle, '.2f'), 'cm.')
area_peri_circle()
# function is defined at the beginning and called at the end


#Question 2
#Ask user to input a list of numbers, separated by space,
#Prompt the user with the average, median, sum of the list
#Output a sorted list.
# (Added error handling and while loop)
while(True):
    try:
        user_input = input('Input a list of numbers separated by space: ')
        numbers_list = list(map(float, user_input.split(" ")))
        break #needed to be added to come out of the loop
    except ValueError:
        print('Invalid Format! Try again!')
#Calculating the sum
len = len(numbers_list) # counts the number of numbers in the list
sum = 0
for i in numbers_list:
    sum += i # sum = sum + i
print(f'The sum of the numbers in the list: {sum}')
#Calculating the average
print(f'The average of the numbers in the list: {sum/ len}')
#Calculating the median
numbers_list.sort()
if len % 2 == 0:
    median1 = numbers_list[len//2]
    median2 = numbers_list[(len // 2)-1]
    median = (median1 + median2)/2
else:
    median = numbers_list[len//2]
print(f'The median of the numbers in the list: {median}')

#Question 3
ncFile = open('NC2010.txt', 'r') #opening a file for the pupose of reading it i.e file 1
allLines = ncFile.readlines()[1:] #skipping the first line(header) and reading all lines in ncFile i.e file 1
file = open('ncpopchg.txt','w') #opening a new fie for the purpose of writing in it i.e file 2
for aLine in allLines: #working with ncFile ('NC2010.txt') first i.e. file 1
    aListTokens = aLine.split(',') # the split function performs the split based on the comma
    aListTokens[6], aListTokens[8] = float(aListTokens[6]), float(aListTokens[8]) #changing values to float
    pop_change = ((aListTokens[8]-aListTokens[6])/aListTokens[8])*100 #calculation
    file.write(aListTokens[1]+',') #writing to the created file i.e file 2 ('ncpopochang.txt')
    file.write(str(pop_change)+'%'+'\n')
ncFile.close() #closing file 1
file.close() #closing file 2

#Question 4
ncFile2 = open('NC2010.txt', 'r') ##opening a file for the pupose of reading it i.e file 1
allLines2 = ncFile2.readlines()[1:] #skipping the first line(header) of file 1 and reading its content
file2 = open('ncpopchgSorted.txt','w') #opening a new file for the purpose of writing in it i.e file 2
county_list = [] #creating an empty list
for aLine2 in allLines2: #working with file 1
    aListTokens2 = aLine2.split(',') # the split function performs the split based on the comma
    aListTokens2[6], aListTokens2[8] = float(aListTokens2[6]), float(aListTokens2[8]) #chaning values to float
    pop_change2 = ((aListTokens2[8]-aListTokens2[6])/aListTokens2[8])*100 #calculation
    county_list.append((aListTokens2[1],pop_change2)) #adding the values of file 1 to the empty list (county_list) using the append function
county_list.sort(key=lambda x:x[1]) #sorting the appended list (county_list)
for list_2 in county_list: #county_list has two columns
    alinestring = list_2[0]+','+str(list_2[1])+'%'+'\n' #formatting the two colums of county_list and using it to form 'alinestring' variable
    file2.write(alinestring) #writing variable to file 2 (the file that was opening for the purpose of writing into it)

ncFile2.close() #closing file 1
file2.close() # closing file 2

#Question 5
#Part a)calculating the mean center of both list
list1 =[(10,20),(25,8),(34,22),(17,35),(9,1),(31,20),(44,11)] #list 1 of coordinate points
list2 = [(1,21),(19,22),(23,12),(51,26),(78,61),(41,17),(11,21),(81,10),(79,51)] #list 2 of coordinate points
combined_list = list1 + list2 #adding list 1 and list 2 together
def mean_center(tList): #defining the mean center function
    middle_point = [0,0] #setting the median point value
    n = 0
    for p in tList:
        middle_point[0] += p[0]
        middle_point[1] += p[1]
        n+=1
    x = middle_point[0]/n
    y = middle_point[1]/n
    print('%.2f'%x, '%.2f'%y)
mean_center(list1) #mean center of list 1
mean_center(list2) #mean center of list 2
mean_center(combined_list) ##mean center of list 1 and 2

#part b) finding the average distance between a point in list1 and a point in list 2
total_dist = 0
for point1 in list1:
    for point2 in list2:
        dist = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**.5 #calculating the distance of the points
        total_dist += dist #incrementing the distance calculated above into total_dist (was intially set to 0)
avg_dist = total_dist/(len(list1) * len(list2)) 
print('The total distance is', '%.2f'%total_dist)
print('The average distance between a point in list 1 and a point in list 2 is', '%.2f'%avg_dist)

#Question 6
city_file = open('cities.txt','r') #opening a text file for the pupose of reading it i.e file 1
location_file = open('locations.txt','r') #opening a text file for the pupose of reading it i.e file 2
all_cities = city_file.readlines()[1:] #reading file 1, excluding the header
all_locations = location_file.readlines()[1:] #reading file 2, excluding the first line, which is the header
location_list = [] #creating an empty list

for aloc in all_locations: #reading file 2
    alocArgList = aloc.split(',') #spliting the contents of file 2
    location_ID =  alocArgList[0] #calling a column 
    location_x =   float(alocArgList[1]) #calling a column and tranforming its values to float
    location_y =   float(alocArgList[2]) #calling a column and tranforming its values to float
    
    total_distance = 0
    for aCity in all_cities: #reading file 1
        acityArgList = aCity.split(',') #spliting the contents of file 1
        city_name = acityArgList[0] #calling a column 
        city_x = float(acityArgList[1]) #calling a column and tranforming its values to float
        city_y = float(acityArgList[2]) #calling a column and tranforming its values to float
        distance_calc = ((city_x-location_x)**2 + (city_y-location_y)**2)**.5 #distance calculation
        total_distance += distance_calc #incrementing the distance calculated above into total_distance (was intially set to 0)
        total_distance_miles = (total_distance/5280) # Converting feet to miles using 1 mile = 5280 feet
    location_list.append((location_ID, total_distance_miles)) #appending two columns into a an empty lise
location_list.sort(key = lambda x:x[1]) #sorting a list
location_list[0][0]
#print(location_list)
print('Best location ID =' , location_list[0][0],'.','Average Distance (miles) from all cities =', '%.2f'%location_list[0][1] )
