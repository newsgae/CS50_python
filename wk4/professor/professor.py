import random

'''

In a file called professor.py, implement a program that:

Prompts the user for a level, n
    If the user does not input 1, 2, or 3, the program should prompt again.

Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits.
No need to support operations other than addition (+).

Prompts the user to solve each of those problems.
    If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
    allowing the user up to three tries in total for that problem.
    If the user has still not answered correctly after three tries, the program should output the correct answer.

The program should ultimately output the user’s score: the number of correct answers out of 10.

'''

def main():

    level = get_level()
    # integer = generate_integer(level)

    # print(f'{x} + {y} = {z}')

    eqns = 1
    chcs = 3
    score = 0

    while eqns <= 10:
        # Only generate integer for new equation when chances == 3
        if chcs == 3:
             x, y, z = calculator(level)

        try:
            user_answer = int(input(f'{x} + {y} = ' ))
            if user_answer == z:
                eqns += 1
                score += 1
                chcs = 3
                continue # continue forces the loop to start at the next iteration
            else:
                raise ValueError # wrong answer or answer is cat
        except (ValueError): 
            chcs -= 1
            print('EEE')

            if chcs != 0: # continue to reprompt same equation
                continue
            elif chcs == 0: # Reset chances and generate new equation
                print(f'{x} + {y} = {z}')
                eqns += 1
                chcs = 3
                continue
        except (EOFError):
            break

    print(f'Score: {score}')


def get_level():
    while True:
        try:
            user_input = int(input('Level: '))
            if 1 <= user_input <= 3:
                return user_input
        except:
            pass


def generate_integer(level):
    idx = level - 1
    start = [0, 10, 100]
    end = [9, 99, 999]
    if idx > 2:
        raise ValueError
    else:
        return random.randint(start[idx], end[idx])


def calculator(n):
    x = generate_integer(n)
    y = generate_integer(n)
    return x, y, x + y


if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/professor
# submit50 cs50/problems/2022/python/professor