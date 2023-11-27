'''

In a file called bank.py, implement a program that prompts the user for a greeting.

If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20.
Otherwise, output $100.

Ignore any leading whitespace in the users greeting, and
treat the users greeting case-insensitively.

'''

def main():
    user_answer = input('Greeting: ').strip().lower()
    print(f'${value(user_answer)}')


def value(str):

    # or use user_answer.startswith('hello')
    if str[0:5].lower() == 'hello':
        return 0
    elif str.lower().startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()