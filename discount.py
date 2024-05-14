
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()
#day_of_week = 0

# Ask for subtotal
subtotal = float(input('\nPlease enter the subtotal: $'))

# Calculate discounts, sales tax, and totals
if (day_of_week == 1 or day_of_week == 2) and subtotal >= 50.00:
    sale = subtotal * .1
    discount = subtotal - sale
    
    salestax = discount * .06
    total = discount + salestax
    
    print(f'Discount amount: ${sale:.2f}')

elif day_of_week in {1, 2} and subtotal < 50.00:
    buymore = 50.00 - subtotal
    
    salestax = subtotal * .06
    total = salestax + subtotal
    
    print(f'To get 10% off, you need to add ${buymore}.')
else:
    salestax = subtotal * .06
    total = salestax + subtotal

# Output
print(f'Sales tax amount: ${salestax:.2f}')
print(f'Total: ${total:.2f}\n')