"""
Write a function that takes a string of braces, and determines if the order of the braces is valid.
It should return true if the string is valid, and false if it's invalid.

This exercise is similar to the Valid Parentheses exercise, but introduces new characters:
    brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces:
    ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""

import pytest

from code_wars import valid_braces

vaild_examples = [
    '()',
    '[]',
    '{}',
    '{}()[]',
    '([{}])',
    '{}({})[]',
    '(({{[[]]}}))',
]

invalid_examples = [
    '[(])',
    '()[}[]{}',
    '(([[))]]',
    '(([[{{}}]])){)',
]


@pytest.mark.parametrize('string', vaild_examples)
def test_validBraces_with_valid_examples(string):
    # Setup
    expected = True

    # Exercise
    result = valid_braces.validBraces(string)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('string', invalid_examples)
def test_validBraces_with_invalid_examples(string):
    # Setup
    expected = False

    # Exercise
    result = valid_braces.validBraces(string)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('string', vaild_examples)
def test_validBraces2_with_valid_examples(string):
    # Setup
    expected = True

    # Exercise
    result = valid_braces.validBraces2(string)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('string', invalid_examples)
def test_validBraces2_with_invalid_examples(string):
    # Setup
    expected = False

    # Exercise
    result = valid_braces.validBraces2(string)

    # Verify
    assert result == expected

    # Cleanup - none necessary
