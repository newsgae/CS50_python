import re
import sys


'''
In a file called numb3rs.py, implement a function called validate that
    expects an IPv4 address as input as a str and then
    returns True or False, respectively, if that input is a valid IPv4 address or not.

background:
    An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet,
    format: #.#.#.#, # is in [0, 255]

first must done:

hint:
    re.search
    re special characters
    reference: https://stackoverflow.com/questions/5284147/validating-ipv4-addresses-with-regexp

'''


def main():

    if len(sys.argv)>2 :
        print('too many input')
    elif len(sys.argv)<1:
        print('too few input')
    else:
        print(validate(input("IPv4 Address: ")))


# method 1
def validate_1(ip):
    gp = ip.strip().split('.')
    print(f'{gp}')
    for i in range(4):
        if 0<=int(gp[i])<=255:
            pass
        else:
            return False
    return True

# method 2
def validate_2(ip):
    try:
        matches = re.search(r"^([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)$", ip)
        # [v1, v2, v3, v4] =  matches.groups()
        # print(type({v1}))
        for i in range(4):
            if 0 > int(str(matches.group(i+1))) or int(str(matches.group(i+1))) > 255:
                return False
        return True
    except AttributeError:
        return False





# method 3
def validate(ip):
    # regex = r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$"
    regex = r"^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$"
    match = re.search(regex, ip)
    if match:
        return True
    else:
        return False



if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/numb3rs
# submit50 cs50/problems/2022/python/numb3rs
