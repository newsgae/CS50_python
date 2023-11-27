from seasons import get_dates, number_to_words
from datetime import datetime

'''
In a file called test_seasons.py, implement a program that
    Run your tests by executing
        pytest test_seasons.py. pytest
        it should show that all of your tests have passed

To test your tests, run pytest test_seasons.py
    Ensure you have a correct version of seasons.py.
    Run your tests by executing pytest test_seasons.py.
    pytest should show that all of your tests have passed.

Modify one of the functions you’ve implemented in seasons.py and imported into test_seasons.py.
    One of your functions might, for example, fail to raise a ValueError when it should.
    pytest should show that at least one of your tests has failed.

Continue to modify the behavior of seasons.py, creating (predictably) incorrect versions of your implementation.
    Run your tests by executing pytest test_seasons.py. the tests expect to fail

'''

def test_number_to_words():
    assert number_to_words(13046400) == 'Thirteen million, forty-six thousand, four hundred minutes'
    assert number_to_words(10000) == "Ten thousand minutes"
    assert number_to_words(365) == "Three hundred sixty-five minutes"

