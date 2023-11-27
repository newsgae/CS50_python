from bank import value

# def main():
#     test_value()


def test_value():
    assert value("Hello there") == 0
    assert value("Hey") == 20
    assert value("Greetigs") == 100


def test_case_insensitivity():
    assert value("HELLO") == 0
    assert value("hello") == 0


def test_entire_phrase():
    assert value("Hello, Newman") == 0
    assert value("What's up") == 100


# if __name__ == '__main__':
#     main()


# check50 cs50/problems/2022/python/tests/bank
# submit50 cs50/problems/2022/python/tests/bank
# pytest test_bank.py