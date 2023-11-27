import sys

'''
implement a program called lines.py to
    take one command-line argument and
    return its number of lines

specifically:
    count its number of lines of code (LOC) and
    exclude blank lines and comments, assume that
        any line that starts with # is a comment
        # can optionally preceded by whitespace, such as '   # xxx'
        any line that only contains whitespace is blank
        a docstring is not a comment line

    output is the number of lines of code in that file

expects exactly one command-line argument looks like
        $ python lines.py hello.py
        otherwise, program should instead exit via sys.exit
            if the user does not specify exactly one command-line argument
            if the specified file’s name does not end in .py
            if the specified file does not exist, use FileNotFoundError

'''

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1][-3:] != '.py':
        sys.exit('Not a python file')
    else:
        file_name = sys.argv[1]
        # print(file_name)
        print(count_lines(file_name))


def count_lines(file):
    try:
        loc=0
        with open(file, 'r') as file:
            for line in file:
                if line.lstrip().startswith('#') or line.strip() == '':
                    continue
                else:
                    loc += 1
            return loc

    except FileNotFoundError:
        sys.exit('File does not exist')


if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/lines
# submit50 cs50/problems/2022/python/lines
