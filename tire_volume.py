'''
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside 
a tire can be approximated with a formula.

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
'''

import math

# inputs
width = int(input('\nEnter the width of the tire in mm (ex 205): '))
aspect = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

# math
volume = (math.pi * (width ** 2) * aspect * (width * aspect + (2540 * diameter))) / 10000000000

# output
print(f'\nThe approximate volume is {volume:.2f} liters.')

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Exceeding the Requirements
if width == 195 and aspect == 65 and diameter == 15:
    print('\nPrice: $141.00 each')
    buy = input('Would you like to buy tires with the dimensions entered? (yes/no) ')
elif width == 235 and aspect == 75 and diameter == 15:
    print('\nPrice: $211.00 each')
    buy = input('Would you like to buy tires with the dimensions entered? (yes/no) ')
elif width == 205 and aspect == 55 and diameter == 16:
    print('\nPrice: $172.00 each')
    buy = input('Would you like to buy tires with the dimensions entered? (yes/no) ')
elif width == 215 and aspect == 55 and diameter == 17:
    print('\nPrice: $196.00 each')
    buy = input('Would you like to buy tires with the dimensions entered? (yes/no) ')
else:
    buy = 'no'
print()

# Buy
if buy.lower() == 'yes':
    phone_number = input('Please enter your phone number: ')
else:
    phone_number = 'n/a'
print()

# Open txt file and append data from input
with open('volumes.txt', 'at') as volumes_file:
    print(f'{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}, {phone_number}', file=volumes_file)
