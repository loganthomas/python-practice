"""
Write a function that takes a string as an argument and outputs a
dictionary of matching parentheses and their corresponding indices.

Input:
'mul(add[5,3], sub{7,4})'

Output:
{
    '()': [[3,22]],
    '[]': [[7,11]],
    '{}': [[17,21]]
}

Input:
'mul(add(5,3), sub(7,4))'

Output:
{
    '()': [[3,22], [7,11], [17,21]]
}
"""
# Standard libraries
from collections import defaultdict, namedtuple
from typing import DefaultDict, List

ParenLoc = namedtuple("ParenLoc", ("char", "index"))


def find_matching_parens(string: str) -> DefaultDict[str, List[List]]:
    mapping = {"(": ")", "[": "]", "{": "}"}

    stack = []
    out = defaultdict(list)

    for i, char in enumerate(string):

        if char in mapping.keys():
            stack.append(ParenLoc(char, i))

        if char in mapping.values():
            if not stack:
                raise ValueError(
                    f"Invalid bracket at index {i}. '{char}' has no opening."
                )

            open_paren = stack.pop()
            if mapping[open_paren.char] != char:
                raise ValueError(
                    f"Invalid bracket at index {i}. '{open_paren.char}' is not closed by '{char}'"
                )
            out[open_paren.char + char].append([open_paren.index, i])

    return out
