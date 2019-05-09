"""
Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a
different prime. (This rules out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 31 which is prime too.
Same for the others.

Task
Find all Backwards Read Primes between two positive given numbers (both inclusive), the second one
always being greater than or equal to the first one.

The resulting array or the resulting string will be ordered following the natural order of the
prime numbers.

Example
backwardsPrime(2, 100)      => [13, 17, 31, 37, 71, 73, 79, 97]
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
backwardsPrime(501, 599)    => []
"""


def _is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


def backwardsPrime(start, stop):
    # Primes where number is not equal to reverse string of number (i.e. not a palindrome)
    potentials = [x for x in range(start, stop+1) if _is_prime(x) and x != int(str(x)[::-1])]

    # Out is potential primes where reverse string of prime is also prime
    out = [x for x in potentials if _is_prime(int(str(x)[::-1]))]

    return out


if __name__ == '__main__':
    """ Simple tests. Consider refactoring with pytest later. """
    assert backwardsPrime(2, 100)      == [13, 17, 31, 37, 71, 73, 79, 97], "fails for start=2, stop=100"
    assert backwardsPrime(9900, 10000) == [9923, 9931, 9941, 9967], "fails for start=9900, stop=10000"
    assert backwardsPrime(501, 599)    == [], "fails for start=501, stop=599"

    # Assuming asserts are never skipped/ignored
    print('Great Success!')

