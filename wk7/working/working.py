import re
import sys


'''
conver AM/PM to 24-hour clock

In a file called working.py, implement a function called convert that
     expects a str in either of the 12-hour formats below and
     returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
     Expect that AM and PM will be capitalized (with no periods therein) and
     that there will be a space before each.

    Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
        (e.g., 12:60 AM, 13:00 PM, etc.).
    do not assume that someone’s hours will start ante meridiem AM and end post meridiem PM;
        someone might work late and even long hours
        (e.g., 5:00 PM to 9:00 AM).

Example:
input:  9:00 AM to 5:00 PM
output: 9:00 to 17:00

input:  9 AM to 5 PM
output: 9:00 to 17:00

input:  9 AM to 5:30 PM
output: 9:00 to 17:300

Background:
    Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock.
    Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”),
        wherein “AM” is an abbreviation for “ante meridiem”
        and “PM” is an abbreviation for “post meridiem”,
        wherein “meridiem” means midday (i.e., noon).

Hint:
    can format an int with leading zeroes with code like
        print(f"{n:02}")
        wherein, if n is a single digit, it will be prefixed with one 0,
        per docs.python.org/3/library/string.html#format-string-syntax.

'''


def main():

    if len(sys.argv)>2 :
        print('too many input')
    elif len(sys.argv)<1:
        print('too few input')
    else:
        print(convert(input("Hours: ")))


def convert(s):

    regex = "(0?[0-9]|1[0-2]):?([0-5][0-9])? (PM|AM)"
    match = re.search(r"^" + regex + " to " + regex +"$", s)
    # print(match)

    if match:
       time_from = time_convert(match.group(1), match.group(2), match.group(3))
       time_to = time_convert(match.group(4), match.group(5), match.group(6))
       return f"{time_from} to {time_to}"
    else:
       raise ValueError('Invalid input')


def time_convert(hh, mm, suffix):
    try:
        if hh == "12":
            if suffix == 'PM':
                hour = "12"
            else:
                hour = "00"
        else:
            if suffix == 'AM':
                hour = f"{int(hh):02}"
            else:
                hour = f"{int(hh) + 12}"

        if mm == None:
            minute = "00"
        else:
            minute = f"{int(mm):02}"

        return f"{hour}:{minute}"

    except ValueError:
        raise ValueError


if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/working
# submit50 cs50/problems/2022/python/working

