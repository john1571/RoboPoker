import random

HEART = '♥'
CLUB = '♣'
DIAMOND = '♦'
SPADE = '♠'

class bcolors:
    cDIAMOND = '\033[94m'
    cCLUB = '\033[93m'
    cSPADE = '\033[92m'
    cHEART = '\033[91m'
    ENDC = '\033[0m'


suits = ['♥', '♣', '♦', '♠']
suits_printable = {'♥': 'Hearts', '♣': 'Clubs', '♦': 'Diamonds', '♠': 'Spades'}
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'J': 11, 'Q': 12, 'K': 13, 'A': 14,
}


def getDeck():
    deck = []
    for suit in suits:
        for value in values.keys():
            deck.append(Card(suit, value))
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    return deck


def rank_to_value(string):
    return values[string]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = rank_to_value(rank)
        self.color = ""

        if self.suit == HEART:
            self.color = bcolors.cHEART
        elif self.suit == CLUB:
            self.color = bcolors.cCLUB
        elif self.suit == DIAMOND:
            self.color = bcolors.cDIAMOND
        else:
            self.color = bcolors.cSPADE

    def print_with_color(self):
        print(self.color + self.rank + self.suit + bcolors.ENDC, end='\t')

    def get_with_color(self):
        return self.color + self.rank + self.suit + bcolors.ENDC

    def log_string(self):
        return self.rank + suits_printable[self.suit]
