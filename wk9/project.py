import random
import time
from pyfiglet import Figlet


def main():

    player_name = input('Enter your name: ').title()

    total_questions = 10
    num_wrong = 0

    # start game
    figlet = Figlet()
    figlet.setFont(font='slant')
    print(figlet.renderText(f'Math Game'))
    input(f'Welcome to the Math Challenge, {player_name}! Press Enter to start.')
    print(60*'-')

    # start timer
    start_time = time.time()

    # start question
    for i in range(total_questions):
        # generate question
        left, right, operator, expr = get_question()

        key :int = get_answer(left, right, operator)

        # check until get answer right
        while True:
            user_answer = input('Question' + str(i+1) + ': ' + expr).lower()
            if user_answer == str(key):
                break
            else:
                num_wrong += 1

    print(60*'-')
    figlet.setFont(font='slant')
    print(figlet.renderText(f'Completed, {player_name}!'))
    print(60*'-')

    # end timer
    end_time = time.time()
    total_time = round(end_time - start_time, 1)

    accuracy = get_accuracy(total_questions, num_wrong)
    if accuracy == 100:
        print(f'You did it in {total_time} seconds and your accuracy is {accuracy}%. 💯')
    elif accuracy <=60:
        print(f'You did it in {total_time} seconds and your accuracy is {accuracy}%. 😥')
    else:
        print(f'You did it in {total_time} seconds and your accuracy is {accuracy}%. 👍')


def get_question():

    # define baics
    operators = ['+', '-', '*']
    min_operand = 1
    max_operand = 12

    # create random values
    left_num :int = random.randint(min_operand, max_operand)
    right_num :int = random.randint(min_operand, max_operand)
    operator :str = random.choice(operators)

    if left_num < right_num and operator == '-':
        # swap to avoid negative number arithmetic
        expr :str = f'{right_num} {operator} {left_num} = '
    else:
        expr :str = f'{left_num} {operator} {right_num} = '

    return left_num, right_num, operator, expr


def get_answer(left_num, right_num, operator):

    try:
        if operator == '+':
            return left_num + right_num
        elif operator == '-':
            # no negative number arithmetic
            if left_num < right_num:
                 left_num, right_num = right_num, left_num
            return left_num - right_num
        elif operator == '*':
            return left_num * right_num

    except (ValueError, TypeError):
        print('Make sure number follows arithmetic rules')


def get_accuracy(total_questions, num_wrong):

    accuracy = (total_questions - num_wrong)/total_questions*100
    return accuracy


if __name__ == "__main__":
    main()


# submit50 cs50/problems/2022/python/project
