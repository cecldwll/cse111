"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.
"""

# Import the math module so that we can call the math.ceil function.
import math

# Get two numbers from the user.
item = int(input('\nEnter the number of items: '))
iperbox = int(input('Enter the number of items per box: '))

# Compute the number of boxes by dividing and then calling the math.ceil function
box = math.ceil(item / iperbox)

# Display the results for the user to see
print(f'\nFor {item} item(s), packing {iperbox} item(s) in each box, you will need {box} box(es).\n')