"""
Object Oriented Programming
---------------------------

How would you design a card game (blackjack) using OOP techniques?
What classes, methods, and attributes do you need for the game?
"""

# Standard libraries
import random
from collections import namedtuple
from typing import List

# Third-party libraries
from colorama import Fore, Style

Card = namedtuple('Card', ('value', 'suite'))


class Deck:
    def __init__(self) -> None:
        self.suites = ['hearts', 'diamonds', 'spades', 'clubs']
        self.values = [*range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(v, s) for v in self.values for s in self.suites]

    def shuffle(self) -> None:
        if len(self.cards) > 1:
            random.shuffle(self.cards)
        else:
            raise ValueError('No cards left in deck')

    def deal(self) -> Card:
        """Treat deck like stack and remove top card."""
        if len(self.cards) > 1:
            return self.cards.pop(0)
        else:
            raise ValueError('No cards left in deck')


class Hand:
    def __init__(self, dealer: bool = False) -> None:
        self.dealer = dealer
        self.cards: List[Card] = []
        self.value = 0

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def calculate_value(self) -> None:
        self.value = 0
        has_ace = False

        for card in self.cards:
            if isinstance(card.value, int):
                self.value += card.value
            else:
                if card.value == 'Ace':
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10

        # Ace can be treated as 11 or 1 depending on other cards
        if (self.value > 21) & (has_ace):
            self.value -= 10

    def get_value(self) -> int:
        self.calculate_value()
        return self.value

    def display(self) -> None:
        for i, card in enumerate(self.cards, 1):
            if (i == 1) & (self.dealer):
                print(f'Card 1: {Fore.BLUE}hidden{Style.RESET_ALL}')
            else:
                print(f'Card {i}: {card.value} of {card.suite}')
        if not self.dealer:
            print(f'Hand Total: {self.get_value()}')


class BlackJack:
    def __init__(self) -> None:
        self.games_played = 0
        self.wins = 0

    @staticmethod
    def check_for_blackjack(hand: Hand) -> bool:
        return hand.get_value() == 21

    @staticmethod
    def display_if_blackjack(player_has_blackjack: bool, dealer_has_black_jack: bool) -> None:
        if player_has_blackjack & dealer_has_black_jack:
            print("\nIt's a draw! Both you and the dealer have blackjack!")
        elif player_has_blackjack:
            print(f'\n{Fore.GREEN}You have blackjack! You Win!{Style.RESET_ALL}')
        else:
            print(
                f'\n{Fore.RED}Dealer has blackjack! Dealer Wins! Better luck next time...{Style.RESET_ALL}'
            )

    def check_player_bust(self) -> bool:
        return self.player_hand.get_value() > 21

    def play(self) -> None:
        playing = True

        while playing:
            self.games_played += 1
            print(f'\n### Game {self.games_played} ###')

            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for _ in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print('\n--- Your hand ---')
            self.player_hand.display()

            print('\n--- Dealer hand ---')
            self.dealer_hand.display()

            game_over = False

            while not game_over:
                player_has_blackjack = self.check_for_blackjack(self.player_hand)
                dealer_has_blackjack = self.check_for_blackjack(self.dealer_hand)

                if player_has_blackjack | dealer_has_blackjack:
                    game_over = True
                    self.display_if_blackjack(player_has_blackjack, dealer_has_blackjack)
                    if player_has_blackjack:
                        self.wins += 1

                    # Break out of game_over loop
                    # continue starts another loop of the while not game_over loop
                    # since game_over set to True, it will break out of loop.
                    continue

                print()
                choice = input('Choose hit (h) or stay (s): ').lower()

                while choice not in ('h', 's'):
                    choice = input('Options are h (hit) or s (stay): ').lower()

                if choice == 'h':
                    self.player_hand.add_card(self.deck.deal())

                    print('\n--- Your hand ---')
                    self.player_hand.display()

                    print('\n--- Dealer hand ---')
                    self.dealer_hand.display()

                    if self.check_player_bust():
                        game_over = True
                        print(f'\n{Fore.RED}Bust! Better luck next time...{Style.RESET_ALL}')

                else:
                    game_over = True

                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()

                    print('\n--- Final Results ---')
                    print(f'Player hand: {player_hand_value}')
                    print(f'Dealer hand: {dealer_hand_value}')

                    if player_hand_value > dealer_hand_value:
                        print(f'\n{Fore.GREEN}You Win! Congrats!{Style.RESET_ALL}')
                        self.wins += 1
                    elif player_hand_value == dealer_hand_value:
                        print("\nIt's a draw! Almost...")
                    else:
                        print(f'\n{Fore.RED}Dealer Wins! Better luck next time...{Style.RESET_ALL}')

            print()
            play_again = input('Would you like to play again? [y/n]: ').lower()

            while play_again not in ('y', 'n'):
                play_again = input('Options are y (yes) or n (no): ').lower()

            if play_again == 'n':
                playing = False
                print(f'{Fore.BLUE}\n### Final Stats ###{Style.RESET_ALL}')
                print(f'Games Played  : {self.games_played}')
                print(f'Games Won     : {self.wins}')
                print(f'Win Percentage: {self.wins/self.games_played*100:.2f}%')
                print('\nThanks for playing!')


if __name__ == '__main__':
    game = BlackJack()
    game.play()
