from advent_of_code.year_2017 import day1
import pytest


# Post solution tests (given after submission)
sol_1_tests = [
    ('1122'     , 3),
    ('1111'     , 4),
    ('1234'     , 0),
    ('91212129' , 9),
]


# Solution 2 Testing
sol_2_tests = [
    ('1212'     , 6),
    ('1221'     , 0),
    ('123425'   , 4),
    ('123123'   , 12),
    ('12131415' , 4),
]


def test_captcha1_on_provided_data():
    """
    Tests Part 1 Solution works for provided input data
    """
    # Setup
    # Provided test data
    data = day1.load_data()
    expected = 1251

    # Exercise
    result = day1.captcha1(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


def test_captcha2_on_provided_data():
    """
    Tests Part 2 Solution works for provided input data
    """
    # Setup
    # Provided test data
    data = day1.load_data()
    expected = 1244

    # Exercise
    result = day1.captcha2(data)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('data,expected', sol_1_tests)
def test_captcha1_on_post_submission_tests(data, expected):
    """
    Test Part 1 Solution works for tests provided after submission.
    """
    # Setup
    expected = expected

    # Exercise
    result = day1.captcha1(data)

    # Verify
    assert result == expected

    # Cleanup -  none necessary


@pytest.mark.parametrize('data,expected', sol_2_tests)
def test_captcha2_on_post_submission_tests(data, expected):
    """
    Test Part 2 Solution works for tests provided after submission.
    """
    # Setup
    expected = expected

    # Exercise
    result = day1.captcha2(data)

    # Verify
    assert result == expected

    # Cleanup -  none necessary

