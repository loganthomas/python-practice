# Standard Libraries
import itertools

# Third-party libraries
import pytest

# Local libraries
from prep import blackjack


def test_Card_instantiation():
    # Setup - none necessary

    # Exercise
    card = blackjack.Card(2, "hearts")
    face_card = blackjack.Card("King", "diamonds")

    # Verify
    assert hasattr(card, "value")
    assert hasattr(card, "suite")

    assert card.value == 2
    assert card.suite == "hearts"

    assert hasattr(face_card, "value")
    assert hasattr(face_card, "suite")

    assert face_card.value == "King"
    assert face_card.suite == "diamonds"

    # Cleanup - none necessary


def test_Deck_instantiation():
    # Setup - none necessary

    # Exercise
    deck = blackjack.Deck()

    # Verify
    assert deck.suites == ["hearts", "diamonds", "spades", "clubs"]
    assert len(deck.suites) == 4

    assert deck.values == [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    assert len(deck.values) == 13

    assert len(deck.cards) == 52

    # Cleanup - none necessary


def test_Deck_shuffle_raises_error_with_no_cards():
    # Setup
    deck = blackjack.Deck()
    deck.cards.clear()

    # Exercise
    with pytest.raises(ValueError) as error_info:
        deck.shuffle()

    # Verify
    assert str(error_info.value) == "No cards left in deck"

    # Cleanup - none necessary


def test_Deck_shuffle():
    # Setup
    deck = blackjack.Deck()
    ordered_cards = deck.cards.copy()

    # check that ordered cards are ordered by value
    ordered_check = [
        *itertools.chain.from_iterable(
            [
                itertools.repeat(x, 4)
                for x in [*range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
            ]
        )
    ]

    assert [c.value for c in ordered_cards] == ordered_check

    # Exercise
    deck.shuffle()

    # Verify
    assert deck.cards != ordered_cards

    # Cleanup - none necessary


def test_Deck_deal_raises_error_with_no_cards():
    # Setup
    deck = blackjack.Deck()
    deck.cards.clear()

    # Exercise
    with pytest.raises(ValueError) as error_info:
        deck.deal()

    # Verify
    assert str(error_info.value) == "No cards left in deck"

    # Cleanup - none necessary


def test_Deck_deal():
    # Setup
    deck = blackjack.Deck()

    # Exercise
    card1 = deck.deal()
    card2 = deck.deal()
    card3 = deck.deal()
    card4 = deck.deal()

    # Verify
    # Due to creation of deck (WITHOUT SHUFFLING), top 4 cards are all 2's
    assert card1.value == 2
    assert card1.suite == "hearts"

    assert card2.value == 2
    assert card2.suite == "diamonds"

    assert card3.value == 2
    assert card3.suite == "spades"

    assert card4.value == 2
    assert card4.suite == "clubs"

    # Cleanup - none necessary


@pytest.mark.parametrize("dealer", [True, False], ids=["dealer-True", "dealer-False"])
def test_Hand_instantiation(dealer):
    # Setup - none necessary

    # Exercise
    hand = blackjack.Hand(dealer=dealer)

    # Verify
    if dealer:
        assert hand.dealer
    else:
        assert not hand.dealer
    assert hand.cards == []
    assert hand.value == 0

    # Cleanup - none necessary
