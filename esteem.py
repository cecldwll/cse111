# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def main():
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    score = 0
    score += ask_positive_question(
        "1. I feel that I am a person of worth, at least on an"
        " equal plane with others.")
    score += ask_positive_question(
        "2. I feel that I have a number of good qualities.")
    score += ask_negative_question(
        "3. All in all, I am inclined to feel that I am a failure.")
    score += ask_positive_question(
        "4. I am able to do things as well as most other people.")
    score += ask_negative_question(
        "5. I feel I do not have much to be proud of.")
    score += ask_positive_question(
        "6. I take a positive attitude toward myself.")
    score += ask_positive_question(
        "7. On the whole, I am satisfied with myself.")
    score += ask_negative_question(
        "8. I wish I could have more respect for myself.")
    score += ask_negative_question(
        "9. I certainly feel useless at times.")
    score += ask_negative_question(
        "10. At times I think I am no good at all.")

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def ask_positive_question(statement):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3
    return score

def ask_negative_question(statement):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A':
        score = 0
    return score


# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()



'''
pos_questions = []
neg_questions = []
positives = []
negatives = []

pos_sum = 0
neg_sum = 0
num = 0

def main():
    print('\nThis program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters: \n')
    
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.\n')
    
    score = questions()

    print(f'Your score is {score}.')
    print('A score below 15 may indicate problematic low self-esteem.')
    

def questions():
    print('1. I feel that I am a person of worth, at least on an equal plane with others.')
    p1 = input('Enter D, d, a, or A: ')
    pos_questions.append(p1)
    
    print('2. I feel that I have a number of good qualities.')
    p2 = input('Enter D, d, a, or A: ')
    pos_questions.append(p2)
    
    print('3. All in all, I am inclined to feel that I am a failure.')
    n1 = input('Enter D, d, a, or A: ')
    neg_questions.append(n1)

    print('4. I am able to do things as well as most other people.')
    p3 = input('Enter D, d, a, or A: ')
    pos_questions.append(p3)

    print('5. I feel I do not have much to be proud of.')
    n2 = input('Enter D, d, a, or A: ')
    neg_questions.append(n2)

    print('6. I take a positive attitude toward myself.')
    p4 = input('Enter D, d, a, or A: ')
    pos_questions.append(p4)

    print('7. On the whole, I am satisfied with myself.')
    p5 = input('Enter D, d, a, or A: ')
    pos_questions.append(p5)

    print('8. I wish I could have more respect for myself.')
    n3 = input('Enter D, d, a, or A: ')
    neg_questions.append(n3)

    print('9. I certainly feel useless at times.')
    n4 = input('Enter D, d, a, or A: ')
    neg_questions.append(n4)

    print('10. At times I think I am no good at all.')
    n5 = input('Enter D, d, a, or A: ')
    neg_questions.append(n5)

    convert_positives()
    convert_negatives()

    return math()

def convert_positives():
    for i in pos_questions:
        if i == 'D':
            num = 0
        elif i == 'd':
            num = 1
        elif i == 'a':
            num = 2
        elif i == 'A':
            num = 3
        positives.append(num)

def convert_negatives():
    for i in neg_questions:
        if i == 'D':
            num = 3
        elif i == 'd':
            num = 2
        elif i == 'a':
            num = 1
        elif i == 'A':
            num = 0
        negatives.append(num)

def math():
    for i in positives:
        pos_sum = i + pos_sum

    for i in negatives:
        neg_sum = i + neg_sum
    
    all_sum = pos_sum + neg_sum

    return all_sum

if __name__ == "__main__":
    main()
'''