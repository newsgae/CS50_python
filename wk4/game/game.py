from random import randint

'''

In a file called game.py, implement a program that:

Prompts the user for a level, n
If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.

'''

# method 1
def main():

    while True:
        try:

            frst_n = int(input('Level: ').strip())
            if frst_n <= 0:
                pass
            else:
                answer = randint(1, frst_n)
                # print(answer)
                break

        except ValueError:
            continue

    while True:
        try:

            guess = int(input('Guess: ').strip())
            if guess <=0:
                pass
            else:
                if guess < answer:
                    print('Too small!')
                    pass
                elif guess > answer:
                    print('Too large!')
                    pass
                else:
                    print('Just right!')
                    break

        except ValueError:
            continue


if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/game
# submit50 cs50/problems/2022/python/game

