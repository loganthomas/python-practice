from advent_of_code.year_2017 import day2
import numpy as np


def test_captcha1_on_provided_data():
    """
    Tests Part 1 Solution works for provided input data
    """
    # Setup
    # Provided test data
    data     = day2.load_data()
    expected = 41887

    # Exercise
    result = day2.captcha1(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_captcha2_on_provided_data():
    """
    Tests Part 2 Solution works for provided input data
    """
    # Setup
    # Provided test data
    data     = day2.load_data()
    expected = 226

    # Exercise
    result = day2.captcha2(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_captcha1_on_post_submission_test():
    """
    Test Part 1 Solution works for tests provided after submission.
    """
    # Setup
    data     = np.array( [[5,1,9,5], [7,5,3,4], [2,4,6,8]] )
    expected = 18

    # Exercise
    result = day2.captcha1(data)

    # Verify
    assert result == expected

    # Cleanup -  none necessary


def test_captcha2_on_post_submission_tests():
    """
    Test Part 2 Solution works for tests provided after submission.
    """
    # Setup
    data     = np.array( [[5,9,2,8], [9,4,7,3], [3,8,6,5]] )
    expected = 9

    # Exercise
    result = day2.captcha2(data)

    # Verify
    assert result == expected

    # Cleanup -  none necessary

