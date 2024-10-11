"""
Your colleagues have been looking over you shoulder. When you should have been doing your boring
real job, you've been using the work computers to smash in endless hours of code_wars.

In a team meeting, a terrible, awful person declares to the group that you aren't working.
You're in trouble. You quickly have to gauge the feeling in the room to decide whether or not you
should gather your things and leave.

Given an object (meet) containing team member names as keys, and their happiness rating out of 10
as the value, you need to assess the overall happiness rating of the group.

If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.

Happiness rating will be total score / number of people in the room.

Note that your boss is in the room (boss), their score is worth double it's face value
(but they are still just one person!).
"""

import pytest

from code_wars import office_outed


@pytest.mark.parametrize(
    'meet,boss,expected',
    [
        (
            {
                'tim': 0,  # meet
                'jim': 2,
                'randy': 0,
                'sandy': 7,
                'andy': 0,
                'katie': 5,
                'laura': 1,
                'saajid': 2,
                'alex': 3,
                'john': 2,
                'mr': 0,
            },
            'laura',  # boss
            'Get Out Now!',  # expected
        ),
        (
            {
                'tim': 1,
                'jim': 3,
                'randy': 9,
                'sandy': 6,
                'andy': 7,
                'katie': 6,
                'laura': 9,
                'saajid': 9,
                'alex': 9,
                'john': 9,
                'mr': 8,
            },
            'katie',
            'Nice Work Champ!',
        ),
        (
            {
                'tim': 2,
                'jim': 4,
                'randy': 0,
                'sandy': 5,
                'andy': 8,
                'katie': 6,
                'laura': 2,
                'saajid': 2,
                'alex': 3,
                'john': 2,
                'mr': 8,
            },
            'john',
            'Get Out Now!',
        ),
    ],
)
def test_office_outed(meet, boss, expected):
    """
    Test if outed works correctly.
    """
    # Setup
    expected = expected

    # Exercise
    result = office_outed.outed(meet, boss)

    # Verify
    assert result == expected

    # Cleanup - none necessary
