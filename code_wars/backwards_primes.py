"""
Backwards Read Primes are primes that when read backwards in base 10 (from right to left)
are a different prime. (This rules out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 31 which is prime too.
Same for the others.

Task:
Find all Backwards Read Primes between two positive given numbers (both inclusive),
the second one always being greater than or equal to the first one.

The resulting array or the resulting string will be ordered following the natural order of
the prime numbers.

Example:
backwardsPrime(2, 100)      => [13, 17, 31, 37, 71, 73, 79, 97]
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
backwardsPrime(501, 599)    => []

Notes:
- The initial commit worked for a few small tests. However, was not efficient
  and took too long to execute for larger number ranges.
- The new solution was adopted from the below sites
  https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
  https://en.wikipedia.org/wiki/Primality_test
- A brief explanation:

  We can do following optimizations:

  Instead of checking till n, we can check till √n because a larger factor of n must be
  a multiple of smaller factor that has been already checked.

  The algorithm can be improved further by observing that all primes are of the form 6k ± 1,
  with the exception of 2 and 3. This is because all integers can be expressed as (6k + i)
  for some integer k and for i = -1, 0, 1, 2, 3, or 4; 2 divides (6k + 0), (6k + 2), (6k + 4);
  and 3 divides (6k + 3).

  So a more efficient method is to test if n is divisible by 2 or 3, then to check through
  all the numbers of form 6k ± 1.
"""


def _is_prime(n):
    # Corner cases (primes should be greater than 1)
    # if (n <= 1) :
    # return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def backwardsPrime(start, stop):
    # Primes where number is not equal to reverse string of number (i.e. not a palindrome)
    potentials = [
        x for x in range(start, stop + 1) if _is_prime(x) and x != int(str(x)[::-1])
    ]

    # Out is potential primes where reverse string of prime is also prime
    out = [x for x in potentials if _is_prime(int(str(x)[::-1]))]

    return out


# A provided solution that mimics the initial commit... a little slower compared to above
# I was close with initial commit!
def _is_prime2(n):
    return all([n % i != 0 for i in range(2, int(n ** 0.5) + 1)])


def backwardsPrime2(start, nd):
    return [
        i
        for i in range(start, nd + 1)
        if i != int(str(i)[::-1]) and _is_prime(i) and _is_prime(int(str(i)[::-1]))
    ]
