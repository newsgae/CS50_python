'''
In a file called twttr.py, implement a program that
    prompts the user for a str of text and
    then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
    whether inputted in uppercase or lowercase.
    
'''


'''
# method 1

def main():

    response = input('Input: ')
    for c in response:
        if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            c = c.replace(c, '')
            print(c, end='')
        else:
            print(c, end='')
    print('')

main()

'''
# better method

def main():

    response = input('Input: ')
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = print("Output: ", end="")

    for c in response:
        # ommit vowels
        if c.lower() not in vowels:
            print(c, end='')
    print()

if __name__ == '__main__':
    main()