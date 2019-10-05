# WAR

# The deck is divided evenly, with each player receiving 26 cards,
# dealt one at a time, face down. Anyone may deal first. Each player
# places his stack of cards face down, in front of him.
#
# The Play:
# Each player turns up a card at the same time and the player with the
# higher card takes both cards and puts them, face down, on the bottom
# of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three
# cards face down and one card face up. The player with the higher cards
# takes both piles (six cards). If the turned-up cards are again the same
# rank, each player places another card face down and turns another card
# face up. The player with the higher card takes all 10 cards, and so on.
# Ignore "double" wars.

from random import shuffle

suites = '\u2660 \u2663 \u2665 \u2666'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This class will create a deck of cards to initiate play. It will use
    SUITE and RANKS to create the deck. It then splits that deck in half
    and give to the players. It also has a method for splitting the deck
    in half and Shuffling it.
    """

    def __init__(self):
        self.cards = [r+s for r in ranks for s in suites]

    def shuffle_cards(self):
        return shuffle(self.cards)

    def split(self):
        return [self.cards[26:], self.cards[:26]]


class Hand:
    """
    This class tracks the cards drawn from the deck into the hand.
    """

    def __init__(self):
        self.cards = []

    def draw(self, deck):
        self.cards.append(deck.pop())


def current_hands(players_hand, computers_hand):
    print(f"Player's Hand: {players_hand.cards[-1]}.")
    print(f"Computer's Hand: {computers_hand.cards[-1]}.")


def spoils(deck_winner, hand_winner, hand_loser):
    """
    This function adds the spoils of the war turn to the winners deck.
    """
    hand_spoils = hand_winner + hand_loser
    shuffle(hand_spoils)
    deck_winner += hand_spoils


def hand_win_check(players_hand, computers_hand):
    """
    This function finds the winner of the war turn and
    calls the spoils function for the winner.
    """
    if ranks.index(players_hand.cards[-1][:-1]) < \
            ranks.index(computers_hand.cards[-1][:-1]):
        spoils(deck_computer, computers_hand.cards, players_hand.cards)
    else:
        spoils(deck_player, players_hand.cards, computers_hand.cards)


def game_win_check(players_deck, computers_deck):
    """
    This function prints the winner of the game, turn count and war count.
    """
    if len(players_deck) < len(computers_deck):
        print("Computer wins! The turn count is " +
              f"{turn_count} and the war count is {war_count}.")
    else:
        print("Player wins! The turn count is " +
              f"{turn_count} and the war count is {war_count}.")


print("Welcome to War, let's begin...")

# Create player and computer decks
d = Deck()
d.shuffle_cards()
deck_computer, deck_player = d.split()
print(deck_computer)
print(deck_player)

turn_count = 0
war_count = 0

while len(deck_computer) != 0 or len(deck_player) != 0:
    turn_count += 1
    print(f"Turn count: {turn_count}.")

    hand_player = Hand()
    hand_computer = Hand()

    try:
        hand_player.draw(deck_player)
        hand_computer.draw(deck_computer)
    except IndexError:
        break

    current_hands(hand_player, hand_computer)

    while ranks.index(hand_player.cards[-1][:-1]) == \
            ranks.index(hand_computer.cards[-1][:-1]):
        war_count += 1
        print(f"War count: {war_count}.")

        for i in range(4):
            try:
                hand_player.draw(deck_player)
                hand_computer.draw(deck_computer)
            except IndexError:
                break

        current_hands(hand_player, hand_computer)

    hand_win_check(hand_player, hand_computer)

    print(f"Player's Deck: {len(deck_player)} cards.")
    print(f"Computer's Deck: {len(deck_computer)} cards.")

game_win_check(deck_player, deck_computer)
