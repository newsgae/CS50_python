from numb3rs import validate

'''
implement, in a file called test_numb3rs.py,
    test two or more functions that collectively test your implementation of validate thoroughly,
        each of whose names should begin with test_ so that you can execute your tests with:
        pytest test_numb3rs.py

'''

def test_true():
    assert validate('12.115.125.125') == True       # typical case of normal IP address
    assert validate('0.0.0.0') == True              # special case of the all-zeroes IP address
    assert validate('255.255.255.255') == True      # special case of the all-maximum IP address
    assert validate('12.25.125.125') == True        # typical case of normal IP address


def test_false():
    assert validate('cat') == False                 # text IP
    # assert validate('f05.1.5.249') == False       # test a mix of text and number, but not pass cs50 check
    assert validate('255.255.255.255.255') == False # more then four parts
    assert validate('00.515.125.125') == False      # cannot have leading zeros
