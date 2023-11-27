from working import convert
import pytest

'''

implement, in a file called test_numb3rs.py,
    Ensure you have a correct version of working.py.
    Run your tests by executing pytest test_working.py. pytest should show that all of your tests have passed.
    Modify the correct version of working.py, particularly its function convert.
        Your program might, for example, fail to raise a ValueError when it should.
        Run your tests by executing pytest test_working.py. pytest should show that at least one of your tests has failed.
    Similarly, modify the correct version of working.py,
        changing the return values of convert.
        Your program might, for example, mistakenly omit minutes.
        Run your tests by executing pytest test_working.py.
        pytest should show that at least one of your tests has failed.

'''

def test_convert():
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'


def test_false():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60")      # missing PM
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")   # 60 in min
    with pytest.raises(ValueError):
        convert("09:00 AM to 5:1 PM")   # incorrect PM time
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")          # not use " to"
    with pytest.raises(ValueError):
        convert("09AM to 17:00 PM")      # missing space between 9 and AM

# can't let it == ValueError, such as  assert convert('09:60 AM to 17:00') == ValueError
