import re
import sys


'''
count 'um'

In a file called um.py, implement a function called count that
    expects a line of text as input as a str and
    returns, as an int, the number of times that “um” appears in that text, case-insensitively,
    as a word unto itself, not as a substring of some other word.

For instance,
        given text like hello, um, world,
            the function should return 1.
        Given text like yummy, though,
            the function should return 0.

Hint:
    \b boundary

'''


def main():

    if len(sys.argv)>2 :
        print('too many input')
    elif len(sys.argv)<1:
        print('too few input')
    else:
        print(count(input("Text: ")))


def count(s):

    regex = r"\b\.*um\.*\b"
    match = re.findall(regex, s, re.IGNORECASE)
    return len(match)



if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/um
# submit50 cs50/problems/2022/python/um

