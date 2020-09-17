import pytest
from code_forces import way_too_long_words as wtlw


@pytest.mark.parametrize("expected", ["word", "logan", "becca", "python", "dece"])
def test_abbreviate_returns_short_word(expected):
    """Test that a word less than 10 chars is returned."""
    # Setup - none necessary

    # Exercise
    result = wtlw.abbreviate(expected)

    # Verify
    assert result == expected

    # Cleanup - none


@pytest.mark.parametrize(
    "input_, expected",
    [
        ("word", "word"),
        ("localization", "l10n"),
        ("internationalization", "i18n"),
        ("pneumonoultramicroscopicsilicovolcanoconiosis", "p43s"),
    ],
)
def test_abbreviate_on_provided_examples(input_, expected):
    """Test expected output returned from provided examples."""
    # Setup - none necessary

    # Exercise
    result = wtlw.abbreviate(input_)

    # Verify
    assert result == expected

    # Cleanup - none necessary


@pytest.mark.parametrize(
    "input_, expected",
    [
        ("abcdefgh", "abcdefgh"),
        ("abcdefghi", "abcdefghi"),
        ("abcdefghij", "abcdefghij"),
        ("abcdefghijk", "a9k"),
        ("abcdefghijklm", "a11m"),
        ("njfngnrurunrgunrunvurn", "n20n"),
        ("jfvnjfdnvjdbfvsbdubruvbubvkdb", "j27b"),
        ("ksdnvidnviudbvibd", "k15d"),
        ("tcyctkktcctrcyvbyiuhihhhgyvyvyvyvjvytchjckt", "t41t"),
        ("you", "you"),
        ("are", "are"),
        ("registered", "registered"),
        ("for", "for"),
        ("practice", "practice"),
        ("you", "you"),
        ("can", "can"),
        ("solve", "solve"),
        ("problems", "problems"),
        ("unofficially", "u10y"),
        ("results", "results"),
        ("can", "can"),
        ("be", "be"),
        ("found", "found"),
        ("in", "in"),
        ("the", "the"),
        ("contest", "contest"),
        ("status", "status"),
        ("and", "and"),
        ("in", "in"),
        ("the", "the"),
        ("bottom", "bottom"),
        ("of", "of"),
        ("standings", "standings"),
        ("lkpmx", "lkpmx"),
        ("kovxmxorlgwaomlswjxlpnbvltfv", "k26v"),
        ("hykasjxqyjrmybejnmeumzha", "h22a"),
        ("tuevlumpqbbhbww", "t13w"),
        ("qgqsphvrmupxxc", "q12c"),
        ("trissbaf", "trissbaf"),
        ("qfgrlinkzvzqdryckaizutd", "q21d"),
        ("zzqtoaxkvwoscyx", "z13x"),
        ("oswytrlnhpjvvnwookx", "o17x"),
        ("lpuzqgec", "lpuzqgec"),
        ("gyzqfwxggtvpjhzmzmdw", "g18w"),
        ("rlxjgmvdftvrmvbdwudra", "r19a"),
        ("vsntnjpepnvdaxiporggmglhagv", "v25v"),
        ("xlvcqkqgcrbgtgglj", "x15j"),
        ("lyxwxbiszyhlsrgzeedzprbmcpduvq", "l28q"),
        ("yrmqqvrkqskqukzqrwukpsifgtdc", "y26c"),
        ("xpuohcsjhhuhvr", "x12r"),
        ("vvlfrlxpvqejngwrbfbpmqeirxlw", "v26w"),
        ("svmasocxdvadmaxtrpakysmeaympy", "s27y"),
        ("yuflqboqfdt", "y9t"),
    ],
)
def test_abbreviate_on_extisive_test_suite(input_, expected):
    """Test expected output returned from provided examples."""
    # Setup - none necessary

    # Exercise
    result = wtlw.abbreviate(input_)

    # Verify
    assert result == expected

    # Cleanup - none necessary
