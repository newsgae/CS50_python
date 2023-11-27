'''
In a file called twttr.py, implement a program that
    prompts the user for a str of text and
    then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
    whether inputted in uppercase or lowercase.

'''

def main():

    word = input('Input: ')
    abbv_word = shorten(word)
    print(abbv_word)


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    abbv_str = ''

    for char in word:
        if char.casefold() not in vowels: # ommit vowels
             abbv_str += char
    return abbv_str
'''


# omit lowercase
def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    abbv_str = ''

    for char in word:
        if char not in vowels: # ommit vowels
             abbv_str += char
    return abbv_str
'''


if __name__ == '__main__':
    main()