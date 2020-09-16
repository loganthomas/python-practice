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


def validBraces(string):
    while "()" in string or "[]" in string or "{}" in string:
        string = string.replace("()", "").replace("[]", "").replace("{}", "")
    return string == ""


def validBraces2(string):
    """ Another solution possibility. """
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0
