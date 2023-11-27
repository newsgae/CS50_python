from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

'''
In a file called seasons.py, implement a program that
    prompts the user for their date of birth in YYYY-MM-DD format, looks like
        1999-05-12
    prints how old they are in minutes, rounded to the nearest integer,
    display using English words instead of numerals, without any and between words. such as
        Five hundred twenty-five thousand, six hundred minutes
        convert numbers to words using inflect module
            words = p.number_to_words(1234, wantlist=True) -> # ("one thousand","two hundred and thirty-four")
    assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date.
    assume that the current time is also midnight.
        In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date.

Additionally in another file called test_seasons.py, implement a program
    have one or more functions that
        test your implementation of any functions besides main in seasons.py thoroughly,
        each of whose names should begin with test_
        so that you can execute your tests with: pytest test_seasons.py

Use datetime.date.today to get today’s date,
    per docs.python.org/3/library/datetime.html#datetime.date.today

first must done:
    pip install inflect

'''


def main():
    if len(sys.argv) > 1:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 1:
        sys.exit('Too few command-line arguments')
    else:
        minutes = get_dates()
        words = number_to_words(minutes)
        print(f'{words}')


def get_dates():
    format='%Y-%m-%d'
    dob: str = str(input('Date of Birth: '))
    try:
        # get birthday date
        brth_date: date = datetime.strptime(dob, format).date()
        # print(f'{brth_date} is in type of {type(brth_date)}')

        # get today date
        tdy_date: date = date.today()
        # print(f'{tdy_date} is in type of {type(tdy_date)}')

        # get difference
        minute_delta: int =  (tdy_date - brth_date).days *24 *60
        # print(f'{minute_delta} is in type of {type(minute_delta)}')

        return minute_delta

    except ValueError:
        sys.exit('Invalid date')

def number_to_words(num):
    try:
        words = p.number_to_words(num, andword='').capitalize() + ' minutes'
        return words
    except (ValueError, TypeError):
        sys.exit('Invalid date')

if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/seasons
# submit50 cs50/problems/2022/python/seasons

