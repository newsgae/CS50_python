'''
# version 1
from hello import hello


def test_hello():
    assert hello("David") == "hello, David"
    assert hello() == "hello, world"

'''

# version 2: break out our tests separately
from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"


# pytest test_hello.py