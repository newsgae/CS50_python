import sys # take arguments at the command line
import inflect

'''

    implement a program that prompts the user for names,
    one per line, until the user inputs control-d.
    Assume that the user will input at least one name.
    Then bid adieu to those names,
    separating two names with one and,
    three names with two commas and one and, and
    n names with n-1 commas and 1 and, such as

    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

'''


p = inflect.engine()

def main():
    names = []
    while True:
        try:
            user_str = input('Name: ').strip().title()
            names.append(user_str)
            # print(names)
        except EOFError:
            print()
            print('Adieu, adieu, to', p.join(names))
            break



    # if len(names) == 1:
    #     print(f'Adieu, adieu, to {names[0]}')
    # elif len(names) == 2:
    #     print(f'Adieu, adieu, to {names[0]} and {names[1]}')
    # elif len(names) >2:
    #     # print(names[:-1], names[-1])
    #     output_str = names[0]
    #     for name in names[1:-1]:
    #         output_str = output_str + ', ' + name
    #     output_str = output_str + ' and ' + str(names[-1])
    #     print(f'Adieu, adieu, to {output_str}')


if __name__ == '__main__':
    main()


# check50 cs50/problems/2022/python/adieu
# submit50 cs50/problems/2022/python/adieu
# pip install inflect
# https://pypi.org/project/inflect/
