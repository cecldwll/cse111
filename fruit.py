def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"\noriginal: {fruit_list}")

        # Reverse and print fruit_list
        print(f'reversed: {reverse(fruit_list)}')

        # Append 'orange to the end of fruit_list and print
        print(f'append orange: {append_orange(fruit_list)}')

        # Insert 'cherry' before apple and print
        print(f'insert cherry: {insert_cherry(fruit_list)}')

        # Remove 'banana' and print
        print(f'remove banana: {remove_banana(fruit_list)}')

        # Pop the last element and print
        print(f'pop orange: {pop_orange(fruit_list)}')
        
        # Sort and print
        print(f'sorted: {sort(fruit_list)}')

        # Clear and print
        print(f'cleared: {clear(fruit_list)}')

        print()

    except IndexError as index_err:
        print(index_err)


def reverse(old_list):
    new_list = old_list[::-1]

    return new_list


def append_orange(fruit_list):
    fruit_list = reverse(fruit_list)
    fruit_list.append('orange')

    return fruit_list


def insert_cherry(fruit_list):
    fruit_list = append_orange(fruit_list)
    index = fruit_list.index('apple')
    fruit_list.insert(index, 'cherry')

    return fruit_list


def remove_banana(fruit_list):
    fruit_list = insert_cherry(fruit_list)
    fruit_list.remove('banana')

    return fruit_list


def pop_orange(fruit_list):
    fruit_list = remove_banana(fruit_list)
    index = fruit_list.index('orange')
    fruit_list.pop(index)

    return fruit_list


def sort(fruit_list):
    fruit_list = pop_orange(fruit_list)
    fruit_list.sort()

    return fruit_list


def clear(fruit_list):
    fruit_list = sort(fruit_list)
    fruit_list.clear()

    return fruit_list


if __name__ =="__main__":
    main()