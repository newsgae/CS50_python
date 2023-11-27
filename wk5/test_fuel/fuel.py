'''

In a file called fuel.py, implement a program that

prompts the user for a fraction, formatted as X/Y,
    wherein each of X and Y is an integer, and then
    outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
        If 0 - 1%, output E
        If 99% - 100%, output F
        and "Z%" otherwise, wherein Z is that same int.

'''

def main():
    while True:
        try:
            response = input('Fraction: ')
            percentage = convert(response)
            print(gauge(percentage))
            break
        except (ValueError, TypeError, ZeroDivisionError):
            continue #re-prompt for input


def convert(fraction):
    x, y = fraction.strip().split('/')
    try:
        if int(x)/int(y) > 1:
            raise ValueError

        elif int(y) == 0:
            raise ZeroDivisionError

        else:
            return int(x)/int(y)*100

    except :
        return #re-prompt for input in main()


def gauge(percentage):

        if 1 < percentage < 99:
            return f'{percentage:.0f}%'
        elif 99 <= percentage <= 100:
            return 'F'
        elif 0 <= percentage <= 1:
            return 'E'
        else:
            return




if __name__ == '__main__':
    main()

# check50 cs50/problems/2022/python/fuel
# submit50 cs50/problems/2022/python/fuel