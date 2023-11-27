from twttr import shorten


def test_lower_vowel_replace():
    assert shorten('twitter') == 'twttr'

def test_upper_vowel_replace():
    assert shorten('aEioU') == ''

def test_no_vowel():
    assert shorten("wrd") == "wrd"

def test_capital_case():
    assert shorten('Twitter') == 'Twttr'

def test_upper_case():
    assert shorten('TWITTER') == 'TWTTR'

def test_special_char():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_omit_numbers():
    assert shorten('CS50') == 'CS50'

def test_omit_punctuation():
    assert shorten('PYTHON50!') == 'PYTHN50!'


# check50 cs50/problems/2022/python/tests/twttr
# submit50 cs50/problems/2022/python/tests/twttr
# pytest test_twttr.py

'''
# version 2
from twttr import shorten


def test_no_vowel():
    assert shorten("wrd") == "wrd"


def test_capital_vowel():
    assert shorten("Assert") == "ssrt"


def test_lower_vowel():
    assert shorten("assert") == "ssrt"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_upper_vowel():
    assert shorten("ASSERT") == "SSRT"


def test_punctuation():
    assert shorten("CS50!") == "CS50!"
'''