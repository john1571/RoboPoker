import random
import globals

if globals.USE_COLORS:
    class Colors:
        cDIAMOND = '\033[94m'
        cCLUB = '\033[93m'
        cSPADE = '\033[92m'
        cHEART = '\033[91m'
        ENDC = '\033[0m'
else:
    class Colors:
        cDIAMOND = ''
        cCLUB = ''
        cSPADE = ''
        cHEART = ''
        ENDC = ''

suits_printable = {}
if globals.USE_SUIT_SYMBOLS:
    HEART = '♥'
    CLUB = '♣'
    DIAMOND = '♦'
    SPADE = '♠'
    suits = ['♥', '♣', '♦', '♠']
    suits_printable = {'♥': 'h', '♣': 'c', '♦': 'd', '♠': 's'}
else:
    HEART = 'h'
    CLUB = 'c'
    DIAMOND = 'd'
    SPADE = 's'
    suits = ['h', 'c', 'd', 's']


values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
          'J': 11, 'Q': 12, 'K': 13, 'A': 14, }


def get_deck():
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
            self.color = Colors.cHEART
        elif self.suit == CLUB:
            self.color = Colors.cCLUB
        elif self.suit == DIAMOND:
            self.color = Colors.cDIAMOND
        else:
            self.color = Colors.cSPADE

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


    def print_with_color(self):
        print(self.color + self.rank + self.suit + Colors.ENDC, end='\t')

    def get_with_color(self):
        return self.color + self.rank + self.suit + Colors.ENDC

    def log_string(self):
        return self.rank + suits_printable[self.suit]

    def to_json_string(self):
        suit = self.suit if not suits_printable else suits_printable[self.suit]
        return self.rank + suit
