import sys
import csv
from tabulate import tabulate

'''
In a file called pizza.py, implement a program that
    expects exactly one command-line argument, looks like
        python pizza.py sicilian.csv or regular.csv
    outputs a table formatted as ASCII art using tabulate,
        a package on PyPI at pypi.org/project/tabulate.
        Format the table using the library’s grid format.

program should instead exit via sys.exit
    if the user does not specify exactly one command-line argument
    if the specified file’s name does not end in .csv,
    if the specified file does not exist

'''

def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif sys.argv[1][-4:] !=  '.csv':
        sys.exit('Not a CSV file')
    else:
        csv_file_name = sys.argv[1]
        print(csv_file_name)
        get_table(csv_file_name)


def get_table(csv_file_name):
    try:
        with open(csv_file_name, 'r') as file:
            table = csv.reader(file)
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit('File does not exist')

if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/pizza
# submit50 cs50/problems/2022/python/pizza
# pip install tabulate
# download csv: wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
# download csv: wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv