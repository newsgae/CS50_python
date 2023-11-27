def main():
    user_answer = input('Greeting: ').strip().lower()

    # or use user_answer.startswith('hello')
    if user_answer[0:5] == 'hello':
        print('$0')
    elif user_answer.startswith('h'):
    # elif user_answer[0] == 'h':
        print('$20')
    else:
        print('$100')

main()