def main():

    plate = input("Plate: ").upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if not (s[0:2]. isalpha()):
        return False
    elif not (2<=len(s)<=6):
        return False
    elif invalid_digit(s[2:]):
        return False
    elif has_spe_char(s):
        return False
    else:
        return True

def has_spe_char(str):

    special_char = "!@#$%^&*()_+{}[]:;<>,.?~\\|"
    for char in str:
        if char in special_char:
            return True
        else:
            return False

def invalid_digit(str):

    for idx, char in enumerate(str):
        # if first digital is 0;
        if char.isdigit() and char == '0':
            return True
        # if has digits in the middel;
        elif char.isdigit() and not(str[idx:].isdigit()):
            return True
        else:
            return False


main()
