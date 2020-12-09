"""
FizzBuzz
--------

Write a program that outputs the string representation of numbers from
1 to n. For multiples of 3, it should output "Fizz" instead of the
number and for the multiples of 5 it should output "Buzz". For numbers
which are a multiple of both 3 and 5 it should output "FizzBuzz".


Notes
-----
"""
from typing import List


def fizzbuzz_naive(n: int) -> List[str]:
    out = []

    for num in range(1, n + 1):
        if num % 15 == 0:
            out.append("FizzBuzz")
        elif num % 3 == 0:
            out.append("Fizz")
        elif num % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(num))

    return out


def fizzbuzz_concat(n: int) -> List[str]:
    out = []

    for num in range(1, n + 1):
        num_str = ""

        if num % 3 == 0:
            num_str += "Fizz"
        if num % 5 == 0:
            num_str += "Buzz"
        if not num_str:
            num_str += str(num)

        out.append(num_str)

    return out


def fizzbuzz_hash(n: int) -> List[str]:
    """
    Useful for when conditions grows. For example, if 7 should be Jazz.
    Rather than multiple if statements, use a hash table O(n*m) where
    m is number of conditions so really still O(n).
    """
    out = []

    # conditions = {3: "Fizz", 5: "Buzz", 7: "Jazz"}
    conditions = {3: "Fizz", 5: "Buzz"}

    for num in range(1, n + 1):
        num_str = ""

        for cond_key, cond_val in conditions.items():
            if num % cond_key == 0:
                num_str += cond_val

        if not num_str:
            num_str += str(num)

        out.append(num_str)

    return out
