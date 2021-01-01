# Third-party libraries
import pytest
from typing import Tuple

# Local libraries
from prep import anagram


ANAGRAMS = [
    ("tar", "rat"),
    ("arc", "car"),
    ("elbow", "below"),
    ("state", "taste"),
    ("cider", "cried"),
    ("dusty", "study"),
    ("night", "thing"),
    ("inch", "chin"),
    ("brag", "grab"),
    ("cat", "act"),
    ("bored", "robed"),
    ("save", "vase"),
    ("angel", "glean"),
    ("stressed", "desserts"),
    ("dormitory", "dirtyroom"),
    ("school master", "the classroom"),
    ("conversation", "voicesranton"),
    ("listen", "silent"),
    ("astronomer", "moonstarer"),
    ("the eyes", "they see"),
    ("a gentleman", "elegant man"),
    ("funeral", "realfun"),
    ("the morse code", "here come dots"),
    ("eleven plus two", "twelve plus one"),
    ("slotmachines", "cashlostinme"),
    ("fourthofjuly", "joyfulfourth"),
]

NON_ANAGRAMS = [
    ("tar", "trogdor"),
    ("arc", "allie"),
    ("elbow", "logan"),
    ("state", "tasty"),
    ("a", "c"),
    ("aa", "ab"),
    ("ccbbcc", "cbc"),
    ("logan", "logann"),
]


@pytest.mark.parametrize("string_pairs", ANAGRAMS, ids=[str(sp) for sp in ANAGRAMS])
def test_is_anagram_sort_on_anagrams(string_pairs: Tuple[str, str]) -> None:
    # Setup
    string_1, string_2 = string_pairs

    # Exercise
    result = anagram.is_anagram_sort(string_1, string_2)

    # Verify
    assert result

    # Cleanup - none necessary


@pytest.mark.parametrize(
    "string_pairs", NON_ANAGRAMS, ids=[str(sp) for sp in NON_ANAGRAMS]
)
def test_is_anagram_sort_on_non_anagrams(string_pairs: Tuple[str, str]) -> None:
    # Setup
    string_1, string_2 = string_pairs

    # Exercise
    result = anagram.is_anagram_sort(string_1, string_2)

    # Verify
    assert not result

    # Cleanup - none necessary


@pytest.mark.parametrize("string_pairs", ANAGRAMS, ids=[str(sp) for sp in ANAGRAMS])
def test_is_anagram_count_on_anagrams(string_pairs: Tuple[str, str]) -> None:
    # Setup
    string_1, string_2 = string_pairs

    # Exercise
    result = anagram.is_anagram_count(string_1, string_2)

    # Verify
    assert result

    # Cleanup - none necessary


@pytest.mark.parametrize(
    "string_pairs", NON_ANAGRAMS, ids=[str(sp) for sp in NON_ANAGRAMS]
)
def test_is_anagram_count_on_non_anagrams(string_pairs: Tuple[str, str]) -> None:
    # Setup
    string_1, string_2 = string_pairs

    # Exercise
    result = anagram.is_anagram_count(string_1, string_2)

    # Verify
    assert not result

    # Cleanup - none necessary
