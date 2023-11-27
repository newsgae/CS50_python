def main():
    user_answer = input('Please enter the answer to the great question of \
           Life, the Universe and Everything. ').strip().lower()

    if user_answer in ['42', 'forty-two', 'forty two']:
        print('Yes')
    else:
        print('No')

main()