# Third-party libraries
import pytest

# Local libraries
from prep import palindrome


PALINDROMES = [
    "anna",
    "civic",
    "kayak",
    "level",
    "madam",
    "mom",
    "noon",
    "racecar",
    "radar",
    "redder",
    "refer",
    "repaper",
    "rotator",
    "rotor",
    "sagas",
    "solos",
    "stats",
    "tenet",
    "wow",
    "dontnod",
    "ididdidi",
    "mygym",
    "redrumsirismurder",
    "steponnopets",
    "topspot",
    "wasitacatisaw",
    "evacaniseebeesinacave",
    "nolemonnomelon",
    "madamimadam",
    "ablewasiereisawelba",
]

NON_PALINDROMES = [
    "ab",
    "bv",
    "ca",
    "logan",
    "testing",
    "palindrome",
    "ccaabb",
    "ccaac",
    "aaaab",
    "bacdab",
]


# Proposal for pytest to include "fixture_request()" not available yet.
# pytest.fixture_request("list_of_palindromes")
@pytest.mark.parametrize("s", PALINDROMES)
def test_is_palindrome_index_on_palindrome(s: str) -> None:
    # Setup - None necessary

    # Exercise
    result = palindrome.is_palindrome_index(s)

    # Verify
    assert result

    # Cleanup - none necessary


# Proposal for pytest to include "fixture_request()" not available yet.
# pytest.fixture_request("list_of_palindromes")
@pytest.mark.parametrize("s", NON_PALINDROMES)
def test_is_palindrome_index_on_non_palindrome(s: str) -> None:
    # Setup - None necessary

    # Exercise
    result = palindrome.is_palindrome_index(s)

    # Verify
    assert not result


# Proposal for pytest to include "fixture_request()" not available yet.
# pytest.fixture_request("list_of_palindromes")
@pytest.mark.parametrize("s", PALINDROMES)
def test_is_palindrome_ij_on_palindrome(s: str) -> None:
    # Setup - None necessary

    # Exercise
    result = palindrome.is_palindrome_ij(s)

    # Verify
    assert result

    # Cleanup - none necessary


# Proposal for pytest to include "fixture_request()" not available yet.
# pytest.fixture_request("list_of_palindromes")
@pytest.mark.parametrize("s", NON_PALINDROMES)
def test_is_palindrome_ij_on_non_palindrome(s: str) -> None:
    # Setup - None necessary

    # Exercise
    result = palindrome.is_palindrome_ij(s)

    # Verify
    assert not result


# Proposal for pytest to include "fixture_request()" not available yet.
# pytest.fixture_request("list_of_palindromes")
@pytest.mark.parametrize("s", PALINDROMES)
def test_is_palindrome_mid_on_palindrome(s: str) -> None:
    # Setup - None necessary

    # Exercise
    result = palindrome.is_palindrome_mid(s)

    # Verify
    assert result

    # Cleanup - none necessary


# Proposal for pytest to include "fixture_request()" not available yet.
# pytest.fixture_request("list_of_palindromes")
@pytest.mark.parametrize("s", NON_PALINDROMES)
def test_is_palindrome_mid_on_non_palindrome(s: str) -> None:
    # Setup - None necessary

    # Exercise
    result = palindrome.is_palindrome_mid(s)

    # Verify
    assert not result
