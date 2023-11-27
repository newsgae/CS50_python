from pyfiglet import Figlet
import sys # take arguments at the command line
import random

'''
    Expects zero or two command-line arguments:
        Zero if the user would like to output text in a random font.
        Two if the user would like to output text in a specific font, in which
            case the first of the two should be -f or --font,
            and the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.
'''

figlet = Figlet()

def main():

    if 0 < len(sys.argv) < 3 or len(sys.argv) > 3:
        sys.exit('Invalid usage')

    elif sys.argv[1] not in ['-f', '--font', 'renders']:
        sys.exit('Invalid usage')

    elif sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')

    elif len(sys.argv) == 1:
        user_str = input('Input: ').strip().lower()
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print(figlet.renderText(user_str))

    else:
        user_str = input('Input: ').strip()
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_str))


if __name__ == '__main__':
    main()

'''
# pip install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])

python say.py David
'''

# check50 cs50/problems/2022/python/figlet
# submit50 cs50/problems/2022/python/figlet
# pip install pyfiglet

'''

python figlet.py test
python figlet.py -a slant
python figlet.py -f invalid_font
python figlet.py -f slant, type CS50
python figlet.py -f rectangles, then type Hello, world
python figlet.py -f alphabet, then type Moo

'''

