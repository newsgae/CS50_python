from project import get_question, get_answer, get_accuracy
import random

# Set the seed to a known value

def test_get_question():

    # Capture the current state of the random number generator
    original_state = random.getstate()

    # Call get_question to get the first expression
    returned_left, returned_right, returned_operator, returned_expr = get_question()

    # Restore the state of the random number generator
    random.setstate(original_state)

    # Call get_question again to get the second expression
    left, right, operator, expr = get_question()

    assert returned_left == left
    assert returned_right == right
    assert returned_operator == operator
    assert returned_expr == expr


def test_get_answer():
    assert get_answer(2, 4, '+') == 6
    assert get_answer(2, 8, '-') == 6
    assert get_answer(8, 8, '*') == 64

def test_get_accuracy():

    assert get_accuracy(12, 12) == 0
    assert get_accuracy(12, 6) == 50
    assert get_accuracy(12, 0) == 100

# pip install pytest
# pytest test_project.py

