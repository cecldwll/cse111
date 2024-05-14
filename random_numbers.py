import random

def main():
    numbers = [16.2, 75.1, 52.3]
    
    print()
    print(numbers)
    
    append_random_numbers(numbers_list=numbers)

    print(numbers)

    append_random_numbers(numbers_list=numbers, quantity=3)

    print(numbers)
    print()

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        numbers_list.append(round(random.uniform(1, 100), 1))

if __name__ == "__main__":
    main()