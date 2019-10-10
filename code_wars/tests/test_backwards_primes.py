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
"""
import pytest
from code_wars import backwards_primes


# (start, stop, expected)
prime_test_cases = [
    (2        , 100,       [ 13, 17, 31, 37, 71, 73, 79, 97]),
    (9900     , 10000,     [ 9923, 9931, 9941, 9967]),
    (7000     , 7100,      [ 7027, 7043, 7057]),
    (70000    , 70245,     [ 70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241]),
    (70485    , 70600,     [ 70489, 70529, 70573, 70589]),
    (109500   , 109700,    [ 109537, 109579, 109583, 109609, 109663]),
    (1095000  , 1095403,   [ 1095047, 1095209, 1095319, 1095403]),
    (100      , 403,       [ 107, 113, 149, 157, 167, 179, 199, 311, 337, 347, 359, 389]),
    (7048500  , 7048600,   [ 7048519, 7048579]),
    (1048500  , 1048600,   [ 1048571, 1048583]),
    (1000001  , 1000100,   [ 1000033, 1000037, 1000039]),
    (700000008, 700000050, [ 700000031]),
]

empty_test_cases = [
    (501  , 599,   [ ]),
    (60000, 70000, [ ]),
    (400  , 503,   [ ]),
]


@pytest.mark.parametrize('start,stop,expected', prime_test_cases)
def test_correct_list_of_primes_backwardsPrime(start,stop,expected):
    """
    Test that backwardsPrime correctly identifies primes within start,stop range
    """
    # Setup
    expected = expected

    # Exercise
    result = backwards_primes.backwardsPrime(start,stop)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('start,stop,expected', empty_test_cases)
def test_correct_empty_list_backwardsPrime(start,stop,expected):
    """
    Test that backwardsPrime correctly identifies no primes within start,stop range
    """
    # Setup
    expected = expected

    # Exercise
    result = backwards_primes.backwardsPrime(start,stop)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('start,nd,expected', prime_test_cases)
def test_correct_list_of_primes_backwardsPrime2(start,nd,expected):
    """
    Test that backwardsPrime correctly identifies primes within start,stop range
    """
    # Setup
    expected = expected

    # Exercise
    result = backwards_primes.backwardsPrime2(start,nd)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('start,nd,expected', empty_test_cases)
def test_correct_empty_list_backwardsPrime2(start,nd,expected):
    """
    Test that backwardsPrime correctly identifies no primes within start,stop range
    """
    # Setup
    expected = expected

    # Exercise
    result = backwards_primes.backwardsPrime2(start,nd)

    # Verify
    assert result == expected

    # Cleanup - none necessary


primes     = [2, 3, 5, 7, 11, 13, 17, 19]
non_primes = [x for x in range(2,21) if x not in primes]


@pytest.mark.parametrize('n', primes)
def test_is_prime_on_primes(n):
    # Setup
    expected = True

    # Exercise
    result = backwards_primes._is_prime(n)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('n', non_primes)
def test_is_prime_on_non_primes(n):
    # Setup
    expected = False

    # Exercise
    result = backwards_primes._is_prime(n)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('n', primes)
def test_is_prime2_on_primes(n):
    # Setup
    expected = True

    # Exercise
    result = backwards_primes._is_prime2(n)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize('n', non_primes)
def test_is_primei2_on_non_primes(n):
    # Setup
    expected = False

    # Exercise
    result = backwards_primes._is_prime2(n)

    # Verify
    assert result == expected

    # Cleanup - none necessary

