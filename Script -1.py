# Question 1
# Diagnosing if a person is underweight or overweight
# (Used try-except for error handling, if-elif-else statement)
try:
    height = float(input('The height of the patient in ft: '))  # in feet
except ValueError:
    print('Invalid Input for Height!')

try:
    weight = float(input('The weight of the patient in lbs: '))  # in pounds
except ValueError:
    print('Invalid Input for Weight!')

try:
    sw = (height * 30.48-105)/0.454 #The standard weight of the patient
except ValueError:
    print('Invalid Input for Height and/or Weight!')
except NameError:
    print('Invalid Input for Height and/or Weight!')

try:
    if weight < sw*0.9 and weight > 0 and height > 0:
        print('Standard weight =', format(sw, '.3f'), 'This person is underweight!')
    elif sw *0.9 <= weight and weight <= sw*1.1 and weight > 0 and height > 0:
        print('Standard weight =', format(sw, '.3f'), 'This person has a normal weight')
    elif sw * 1.1 < weight and weight <= sw*1.2 and weight > 0 and height > 0:
        print('Standard weight =', format(sw, '.3f'), 'This person is overweight!')
    elif sw*1.2 < weight and weight <= sw*1.3 and weight > 0 and height > 0:
        print('Standard weight =', format(sw, '.3f'), 'This person has Class I Obesity!')
    elif sw*1.3< weight and weight <= sw*1.4 and weight > 0 and height > 0:
        print('Standard weight =', format(sw, '.3f'), 'This person has Class II Obesity!')
    elif sw*1.4< weight and weight > 0 and height > 0:
        print('Standard weight =', format(sw, '.3f'), 'This person has Class III Obesity!')
    else:
        print('Standard weight =', format(sw, '.3f'), ', which is impossible for a person!')
except ValueError:
    print('Unable to calculate Standard Weight!')
except NameError:
    print('Unable to calculate the Standard Weight!')
#ValueError: The Python ValueError is raised when the wrong value is assigned to an object.
    #This can happen if the value is invalid for a given operation, or if the value does not exist

#NameError:NameError occurs when you try to use a variable, function, or module that doesn't exist
    #or wasn't used in a valid way. Some of the common mistakes that cause this error are: Using a variable or function name that is yet to be defined.


# What does a negative standard weight mean?

#Question 2
#guessing a number between 1 to 10
# (Used try-except for error handling, if-elif statement, while loop)
import random
tries = 0
number = random.randint(1,100+1) # interger from 1 to 100

#Infinite loop
while(True):
    try:
        guess = int(input('Guess a number between 1 to 100: '))
        while guess != number:
            if guess < number:
                print('Your guess is smaller than the correct number')
                guess = int(input('Guess again: '))
                tries = tries + 1
            elif guess > number:
                print('Your guess is greater than the correct number')
                guess = int(input('Guess again: '))
                tries = tries + 1
        print('Congratulations! You guessed right!', 'It took you,', tries, 'try/tries!')
        break
    except ValueError:
        print('Invalid Input!')
#summary --> if 'guess' is not equal to 'number', it checks for whether it is smaller or greater, counts the number of tries, asks user to guess again
        # until the number is found.

# Question 3
# converting dd:mm:ss to decimal degrees
# (Used try-except for error handling, while loop)
while(True):
    try:
        dms = input('Input your degreee in angular form (dd:mm:ss) to convert it to decimal degrees: ')
        list_dms = dms.split(':')
        decimal_degree = int(list_dms[0]) + (int(list_dms[1]) / 60) + (int(list_dms[2]) / (60 * 60))
        print('The decimal degrees equivalent is', format(decimal_degree, '.2f'), '°')
        break
    except ValueError:
        print('Invalid Format! Unable to convert to decimal degrees!')

#Question 4
import itertools
count = 0
for p in itertools.permutations('123456789'):
    s = ''.join(p)
    tNum = int(s[0:3])
    mNum = int(s[3:6])
    lNum = int(s[6:])
    if (tNum + mNum == lNum):
        print(s)
        count = count + 1  #same as count +=1
print('Total number of solutions = ', count)
