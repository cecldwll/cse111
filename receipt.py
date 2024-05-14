import csv
from datetime import datetime
import random

def main():
    try:
        PRODUCT_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2

        # Call the read_dictionary function and store the compound dictionary in a variable named products_dict
        products_dict = read_dictionary('products.csv', PRODUCT_INDEX)

        # Print the store name
        print('\nInkom Emporium\n')

        # Open the request.csv file for reading
        with open('request.csv', 'r') as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skips the header row

            # Initialize variables for calculations
            total_quantity = 0
            subtotal = 0

            # Use a loop to read and process each row from the request.csv file
            for row in reader:
                product_number = row[0]
                requested_quantity = int(row[1])
                
                try:
                    # Retrieve product information from products_dict
                    product_info = products_dict[product_number]
                    product_name = product_info[NAME_INDEX]
                    product_price = float(product_info[PRICE_INDEX])

                    # Calculate and print subtotal for each item
                    item_total = product_price * requested_quantity
                    print(f"{product_name}: {requested_quantity} @ ${product_price:.2f} - ${item_total:.2f}")

                    # Update totals
                    total_quantity += requested_quantity
                    subtotal += item_total

                except KeyError:
                    print("Error: unknown product ID in the request.csv file")
                    print(f"'{product_number}'")

        # Calculate tax and total amount due
        tax_rate = 0.06
        sales_tax = subtotal * tax_rate
        total_amount_due = subtotal + sales_tax

        # Print totals
        print(f"\nTotal Items: {total_quantity}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax (6%): ${sales_tax:.2f}")
        print(f"Total Amount Due: ${total_amount_due:.2f}")

        # Print thank you message
        print("\nThank you for shopping at Inkom Emporium!")

        # Get current date and time
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%A, %B %d, %Y %I:%M %p}")

        # Print coupon for a random product
        print("\nCoupon for your next purchase:")
        print_coupon(products_dict)

        # Print invitation for an online survey
        print("\nPlease take a moment to complete our online survey. Your feedback is valuable to us.")
        print('www.inkomemporium.com/survey')
        
    except FileNotFoundError:
        print("\nError: File not found.")
        print("[Errno 2] No such file or directory: 'products.csv'")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    print()

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    
    Return:
        a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    
    return dictionary

def print_coupon(products_dict):
    """Print a coupon for a randomly selected product."""
    product_number = random.choice(list(products_dict.keys()))
    product_info = products_dict[product_number]
    product_name = product_info[1]  # Assuming name is at index 1
    product_price = float(product_info[2])  # Assuming price is at index 2

    # Print coupon details
    print(f"Get 10% off your next purchase of {product_name}! Use code {product_number}10 at checkout. Price: ${product_price:.2f}")

if __name__ == "__main__":
    main()
