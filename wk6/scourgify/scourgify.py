import sys
import csv

'''
In a file called scourgify.py, implement a program that:

    Expects the user to provide two command-line arguments, looks like:
        python scourgify.py before.csv after.csv
            before.csv = the name of an existing CSV file to read as input,
                         whose columns are assumed to be, in order, name and house
                         e.g. "Abbott, Hannah",Hufflepuff
            after.csv = the name of a new CSV to write as output,
                        whose columns should be, in order, first, last, and house
                        e.g. Abbott,Hannah,Hufflepuff

    Converts that input to that output by
        splitting each name into a first name and last name.
        assume that each student will have both a first name and last name.

program should instead exit via sys.exit with an error message
    if the user does not specify exactly two command-line arguments
    if the the first cannot be read,
    if the specified file does not exist

before.csv looks like

    "Edgecombe, Marietta",Ravenclaw
    "Finch-Fletchley, Justin",Hufflepuff
    "Finnigan, Seamus",Gryffindor
    ...

'''

def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif sys.argv[1][-4:] !=  '.csv':
        sys.exit('Not a CSV file')
    else:
        input_csv_file = sys.argv[1]
        output_csv_file = sys.argv[2]
        clean_table(input_csv_file, output_csv_file)


def clean_table(input_csv_file, output_csv_file):
    try:
        with open(input_csv_file, 'r') as csvin:
            csv_table = csv.DictReader(csvin)
            with open(output_csv_file, 'w') as csvout:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(csvout, fieldnames=fieldnames)
                writer.writeheader()
                for row in csv_table:
                    # read data
                    # print(f'{row}')
                    house = row['house']
                    last, first = row['name'].split(', ') # not ',' it is "last, first", to swith order
                    # print(f'{first}, {last}, {house}')
                    # write data
                    writer.writerow({'first': first, 'last': last, 'house': house})
    except FileNotFoundError:
        sys.exit(f'Could not read {input_csv_file}')


if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/scourgify
# submit50 cs50/problems/2022/python/scourgify
# download csv: wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv
# Create empty files 1.csv, 2.csv, and 3.csv via touch 1.csv 2.csv 3.csv
# from https://cs50.harvard.edu/python/2022/psets/6/scourgify/
