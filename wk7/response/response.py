import sys
import validators

'''
In a file called response.py, using either validator-collection or validators from PyPI,
    implement a program that prompts the user for an email address via input
    prints Valid or Invalid as output

        if the input is a syntatically valid email address.
        And do not validate whether the email address’s domain name actually exists.

Example
    What's your email address? malan
    Invalid

    What's your email address? malan at harvard dot edu
    Invalid

    What's your email address? malan@harvard.edu
    Valid

Hint:
    pip install validator-collection
    pip install validators
'''


def main():

    if len(sys.argv)>2 :
        print('too many input')
    elif len(sys.argv)<1:
        print('too few input')
    else:
        user_response = input("What's your email address? ").strip().lower()
        if validators.email(user_response):
            print('Valid')
        else:
            print('Invalid')


if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/response
# submit50 cs50/problems/2022/python/response

