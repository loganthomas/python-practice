# Standard Libraries
import itertools

import pytest

# Third-party libraries
from colorama import Fore, Style

# Local libraries
from prep import blackjack


def test_Card_instantiation():
    # Setup - none necessary

    # Exercise
    card = blackjack.Card(2, 'hearts')
    face_card = blackjack.Card('King', 'diamonds')

    # Verify
    assert hasattr(card, 'value')
    assert hasattr(card, 'suite')

    assert card.value == 2
    assert card.suite == 'hearts'

    assert hasattr(face_card, 'value')
    assert hasattr(face_card, 'suite')

    assert face_card.value == 'King'
    assert face_card.suite == 'diamonds'

    # Cleanup - none necessary


def test_Deck_instantiation():
    # Setup - none necessary

    # Exercise
    deck = blackjack.Deck()

    # Verify
    assert deck.suites == ['hearts', 'diamonds', 'spades', 'clubs']
    assert len(deck.suites) == 4

    assert deck.values == [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
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
    assert str(error_info.value) == 'No cards left in deck'

    # Cleanup - none necessary


def test_Deck_shuffle():
    # Setup
    deck = blackjack.Deck()
    ordered_cards = deck.cards.copy()

    # check that ordered cards are ordered by value
    ordered_check = [
        *itertools.chain.from_iterable(
            [itertools.repeat(x, 4) for x in [*range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']]
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
    assert str(error_info.value) == 'No cards left in deck'

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
    assert card1.suite == 'hearts'

    assert card2.value == 2
    assert card2.suite == 'diamonds'

    assert card3.value == 2
    assert card3.suite == 'spades'

    assert card4.value == 2
    assert card4.suite == 'clubs'

    # Cleanup - none necessary


@pytest.mark.parametrize('dealer', [True, False], ids=['dealer-True', 'dealer-False'])
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


@pytest.mark.parametrize('card', [1, 'a', 'b', 0.59])
def test_Hand_add_single_card(card):
    # Setup
    hand = blackjack.Hand()

    # Exercise
    hand.add_card(card)

    # Verify
    assert hand.cards == [card]

    # Cleanup - none necessary


@pytest.mark.parametrize('cards', [('a', 'b'), (1, 0.59)])
def test_Hand_add_multi_cards(cards):
    # Setup
    hand = blackjack.Hand()

    # Exercise
    for card in cards:
        hand.add_card(card)

    # Verify
    assert hand.cards == list(cards)

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'card_values, expected_hand_value',
    [
        ([1, 5], 6),
        ([7, 10], 17),
        ([5, 'Jack'], 15),
        ([2, 'Quenn'], 12),
        ([7, 'King'], 17),
        ([10, 'Ace'], 21),
        ([30, 'Ace'], 31),  # To check for Ace as value of 1
    ],
)
def test_Hand_calculate_value(card_values, expected_hand_value):
    # Setup
    card_1 = blackjack.Card(card_values[0], 'diamonds')
    card_2 = blackjack.Card(card_values[1], 'diamonds')

    hand = blackjack.Hand()
    hand.add_card(card_1)
    hand.add_card(card_2)

    # Exercise
    hand.calculate_value()

    # Verify
    assert hand.value == expected_hand_value

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'card_values, expected_hand_value',
    [
        ([3, 5], 8),
        ([9, 10], 19),
        ([10, 'Jack'], 20),
        ([5, 'Quenn'], 15),
        (['Ace', 'King'], 21),
        ([10, 'Ace'], 21),
        ([30, 'Ace'], 31),  # To check for Ace as value of 1
    ],
)
def test_Hand_get_value(card_values, expected_hand_value):
    # Setup
    card_1 = blackjack.Card(card_values[0], 'diamonds')
    card_2 = blackjack.Card(card_values[1], 'diamonds')

    hand = blackjack.Hand()
    hand.add_card(card_1)
    hand.add_card(card_2)

    # Exercise
    result = hand.get_value()

    # Verify
    assert result == expected_hand_value
    assert result == hand.value

    # Cleanup - none necessary


@pytest.mark.parametrize('dealer', [True, False], ids=['dealer-True', 'dealer-False'])
def test_Hand_display(dealer, capsys):
    # Setup
    card_1 = blackjack.Card(5, 'diamonds')
    card_2 = blackjack.Card('King', 'diamonds')

    hand = blackjack.Hand(dealer=dealer)
    hand.add_card(card_1)
    hand.add_card(card_2)

    expected_out = 'Card 1: 5 of diamonds\nCard 2: King of diamonds\nHand Total: 15\n'

    if dealer:
        expected_out = f'Card 1: {Fore.BLUE}hidden{Style.RESET_ALL}\nCard 2: King of diamonds\n'

    # Exercise
    hand.display()

    # Verify
    captured = capsys.readouterr()
    assert captured.out == expected_out

    # Cleanup - none necessary


def test_BlackJack_instantiation():
    # Setup - none necessary

    # Exercise
    game = blackjack.BlackJack()

    # Verify
    assert game.games_played == 0
    assert game.wins == 0

    # Cleanup - none necessary


def test_BlackJack_check_for_blackjack():
    # Setup
    hand_non_blackjack = blackjack.Hand()
    hand_non_blackjack.add_card(blackjack.Card(10, 'diamonds'))
    hand_non_blackjack.add_card(blackjack.Card(5, 'hearts'))

    hand_blackjack = blackjack.Hand()
    hand_blackjack.add_card(blackjack.Card(10, 'diamonds'))
    hand_blackjack.add_card(blackjack.Card('Ace', 'hearts'))

    game = blackjack.BlackJack()

    # Exercise
    result_non_blackjack = game.check_for_blackjack(hand_non_blackjack)
    result_blackjack = game.check_for_blackjack(hand_blackjack)

    # Verify
    assert not result_non_blackjack
    assert result_blackjack

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'player_has_blackjack, dealer_has_blackjack',
    [
        (True, True),
        (True, False),
        (False, True),
        # display_if_blackjack() is only called when either dealer or player has blackjack
        # (False, False),
    ],
    ids=[
        'player-True_dealer-True',
        'player-True_dealer-False',
        'player-False_dealer-True',
        # 'player-False_dealer-False',
    ],
)
def test_BlackJack_display_if_blackjack(player_has_blackjack, dealer_has_blackjack, capsys):
    # Setup
    game = blackjack.BlackJack()

    if player_has_blackjack & dealer_has_blackjack:
        expected_out = "\nIt's a draw! Both you and the dealer have blackjack!\n"

    if player_has_blackjack & (not dealer_has_blackjack):
        expected_out = f'\n{Fore.GREEN}You have blackjack! You Win!{Style.RESET_ALL}\n'

    if dealer_has_blackjack & (not player_has_blackjack):
        expected_out = f'\n{Fore.RED}Dealer has blackjack! Dealer Wins! Better luck next time...{Style.RESET_ALL}\n'

    # Exercise
    game.display_if_blackjack(player_has_blackjack, dealer_has_blackjack)

    # Verify
    captured = capsys.readouterr()
    assert captured.out == expected_out

    # Cleanup - none necessary


@pytest.mark.parametrize(
    'cards, expected_bust',
    [
        (
            [
                blackjack.Card(5, 'hearts'),
                blackjack.Card('Ace', 'diamonds'),
                blackjack.Card(5, 'spades'),
            ],
            False,
        ),
        (
            [
                blackjack.Card(10, 'clubs'),
                blackjack.Card(10, 'spades'),
                blackjack.Card(5, 'diamonds'),
            ],
            True,
        ),
    ],
    ids=['player-non-bust', 'player-bust'],
)
def test_BlackJack_check_player_bust(cards, expected_bust):
    # Setup
    game = blackjack.BlackJack()

    game.player_hand = blackjack.Hand()

    for card in cards:
        game.player_hand.add_card(card)

    # Exercise
    result = game.check_player_bust()

    # Verify
    assert result is expected_bust

    # Cleanup - none necessary
