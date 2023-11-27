def main():
    name = input("What's your name? ")
    print(hello(name)) # no print in sub function


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()


'''
# bad version
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()
'''