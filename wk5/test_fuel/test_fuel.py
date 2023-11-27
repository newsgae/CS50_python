import pytest
from fuel import gauge, convert


# “All vanity plates must start with at least two letters.”
def test_convert():
    assert convert("0/1") == 0
    assert convert("1/4") == 25
    assert convert("5/10") == 50
    assert convert("3/4") == 75
    assert convert("5/5") == 100


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(5) == '5%'
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

# The denominator cannot be a ‘0’.”
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('3/0')

# “No periods, spaces, or punctuation marks are allowed.”
def test_value_error_slash():
    with pytest.raises(ValueError):
        convert("x/y")


# check50 cs50/problems/2022/python/tests/fuel
# submit50 cs50/problems/2022/python/tests/fuel
# pytest test_fuel.py