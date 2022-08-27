# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'J': 11, 'Q': 12, 'K': 13, 'A': 14,
}
def rank_to_value(string):
    return values[string]

STRAIGHT_FLUSH = 1000
FOUR_OF_A_KIND = 900
FULL_HOUSE = 800
FLUSH = 700
STRAIGHT = 600
SET = 500
TWO_PAIR = 400
PAIR = 300

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



class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.cards_in_hand = []
        self.hearts = []
        self.diamonds = []
        self.spades = []
        self.clubs = []
        self.four = []
        self.set = []
        self.pair = []
        self.singles = []
        self.has_straight_flush = False
        self.has_four_of_a_kind = False
        self.has_full_house = False
        self.value = 0
        self.value_dictionary = {}

    def add_card(self, card, table=None):
        if card in self.cards:
            return
        self.cards.append(card)
        if not table:
            self.cards_in_hand.append(card)

        if card.suit == HEART:
            self.hearts.append(card.rank)
        elif card.suit == DIAMOND:
            self.diamonds.append(card.rank)
        elif card.suit == SPADE:
            self.spades.append(card.rank)
        else:
            self.clubs.append(card.rank)
        if card.value not in self.singles:
            self.singles.append(card.value)
        elif card.value not in self.pair:
            self.pair.append(card.value)
        elif card.value not in self.set:
            self.set.append(card.value)
        else:
            self.four.append(card.value)

        if self.value_dictionary.get(card.rank):
            self.value_dictionary[card.rank] += 1
        else:
            self.value_dictionary[card.rank] = 1


    def show(self, table):
        print("%s: " % self.name, end='\t')
        for card in self.cards_in_hand:
            card.print_with_color()
        for card in get_table_cards(table):
            self.add_card(card, table)
        print(self.get_value(table), end='\t')
        if self.has_flush():
            print("FLUSH:", end='\t')
            print(self.has_flush())
        elif self.has_straight():
            print("STRAIGHT!")
            #print(self.has_straight())
        elif self.has_set():
            print("THREE!")
            #print(self.has_set())
        elif len(self.has_pair()) > 1:
            print("TWO PAIR!")
        elif self.has_pair():
            print("PAIR!")
            #print(self.has_pair())
        else:
            print("Hi card")

    def get_value(self, table):
        self.value = 0
        table_cards = get_table_cards(table)
        for card in table_cards:
            self.cards.append(card)
        flush_cards = self.has_flush()
        if flush_cards:
            self.value += FLUSH
            if straight_in_array(flush_cards):
                self.value += STRAIGHT
                self.has_full_house = True
            for value in flush_cards:
                self.value += rank_to_value(value)
            return self.value
        if self.has_straight():
            self.value += STRAIGHT
            self.value += self.has_straight()
            return self.value
        if self.has_set():
            sets = self.has_set()
            high_set_value = max(sets)
            if len(sets) > 1:
                self.has_full_house = True
                self.value += FULL_HOUSE
                self.value += high_set_value
                return self.value
            elif self.has_pair():
                pairs = self.has_pair()
                other_pair_values = []
                for x in pairs:
                    if x != high_set_value:
                        other_pair_values.append(x)
                if other_pair_values:
                    self.has_full_house = True
                    self.value += FULL_HOUSE
                    self.value += high_set_value
                    return self.value
            self.value += SET
            self.value += high_set_value
            return self.value
        if self.has_pair():
            pairs = self.has_pair()
            if len(pairs) > 1:
                high_pair_value = max(pairs)
                other_pair_value = min(pairs)
                if len(pairs) > 2:
                    for x in pairs:
                        if x != other_pair_value and x != high_pair_value:
                            other_pair_value = x
                            break
                self.value += TWO_PAIR
                self.value += high_pair_value
                self.value += other_pair_value
                return self.value
            self.value = PAIR
            self.value += self.has_pair()[0]
            return self.value
        else:
            return max(x.value for x in self.cards)


    def has_flush(self):
        if len(self.hearts) > 4:
            return self.hearts
        if len(self.diamonds) > 4:
            return self.diamonds
        if len(self.spades) > 4:
            return self.spades
        if len(self.clubs) > 4:
            return self.clubs
        return None

    def has_pair(self):
        pairs = []
        for rank in self.pair:
            if rank in self.set or self.four:
                if len(self.set) > 1:
                    pairs.append(min(self.set))
                continue
            pairs.append(rank)
        return pairs

    def has_set(self):
        sets = []
        for value in self.set:
            if value in self.four:
                continue
            if len(self.set) > 1:
                sets.append(max(self.set))
            else:
                sets.append(value)
        return sets

    def has_four(self):
        if self.four:
            return self.four[0]
        return None

    def has_straight(self):
        if '10' in self.value_dictionary.keys():
            highstart = self.march_list(['9', '8', '7', '6'], False, 10)
            highend = self.march_list(['J', 'Q', 'K', 'A'], True, 10)
            if (highend - highstart) >= 4:
                return highend
        if '5' in self.value_dictionary.keys():
            lowstart = self.march_list(['4', '3', '2', 'A'], False, 5)
            lowend = self.march_list(['6', '7', '8', '9'], True, 5)
            if (lowend - lowstart) >= 4:
                return lowend
        return None

    def march_list(self, list, up, start):
        found = start
        for value in list:
            if value in self.value_dictionary.keys():
                if up:
                    found += 1
                else:
                    found -= 1
            else:
                return found
        return found

    def has_all_values(self, values):
        for val in values:
            if val not in self.value_dictionary.keys():
                return False
        return True

def march_list(array, list, up, start):
    found = start
    for value in list:
        if value in array:
            if up:
                found += 1
            else:
                found -= 1
        else:
            return found
    return found

def straight_in_array(array):
    if '10' in array:
        highstart = march_list(array, ['9', '8', '7', '6'], False, 10)
        highend = march_list(array, ['J', 'Q', 'K', 'A'], True, 10)
        if (highend - highstart) >= 4:
            return highend
    if '5' in array:
        lowstart = march_list(array, ['4', '3', '2', 'A'], False, 5)
        lowend = march_list(array, ['6', '7', '8', '9'], True, 5)
        if (lowend - lowstart) >= 4:
            return lowend
    return None


def get_table_cards(table):
    table_cards = []
    if table.flop1:
        table_cards.append(table.flop1)
    if table.flop2:
        table_cards.append(table.flop2)
    if table.flop3:
        table_cards.append(table.flop3)
    if table.turn:
        table_cards.append(table.turn)
    if table.river:
        table_cards.append(table.river)
    return table_cards


class Table:
    def __init__(self, deck):
        self.deck = deck
        self.burned = []
        self.flop1 = None
        self.flop2 = None
        self.flop3 = None
        self.turn = None
        self.river = None

    def _turn(self):
        print("\nTURN:", end="\t")
        self.burned = self.deck.pop(0)
        self.turn = self.deck.pop(0)
        self.flop1.print_with_color()
        self.flop2.print_with_color()
        self.flop3.print_with_color()
        self.turn.print_with_color()
        print("******")

    def flop(self):
        print("\nFLOP:", end="\t")
        self.burned = self.deck.pop(0)
        self.flop1 = self.deck.pop(0)
        self.flop2 = self.deck.pop(0)
        self.flop3 = self.deck.pop(0)
        self.flop1.print_with_color()
        self.flop2.print_with_color()
        self.flop3.print_with_color()
        print("******")

    def _river(self):
        print("\nRIVER:", end="\t")
        self.burned = self.deck.pop(0)
        self.river = self.deck.pop(0)
        self.flop1.print_with_color()
        self.flop2.print_with_color()
        self.flop3.print_with_color()
        self.turn.print_with_color()
        self.river.print_with_color()
        print("******")


def getDeck():
    unshuffled = []
    iPos = 0
    order = []
    for suit in suits:
        for value in values.keys():
            unshuffled.append(Card(suit, value))
            order.append(iPos)
            iPos += 1
    random.shuffle(unshuffled)
    random.shuffle(unshuffled)
    random.shuffle(unshuffled)
    return unshuffled

names = ['Adam', 'Ben', 'Caleb', 'Dan', 'Eli', 'Frank', 'Gad', 'Huz', 'Isiah', 'John']

def deal(num_players):
    winning = "", 0
    deck = getDeck()
    print(deck.pop(0))
    if num_players > 12:
        return
    hands = []
    for i in range(0, num_players*2):
        if(i < num_players):
            hands.append(Hand(names[i]))
            hands[i].add_card(deck.pop(0))

        if(i >= num_players):
            hands[i-num_players].add_card(deck.pop(0))
        i += 1
    table = Table(deck)
    for hand in hands:
        hand.show(table)
        if hand.value >= winning[1]:
            winning = hand.name, hand.value
    print(winning)

    table.flop()
    for hand in hands:
        hand.show(table)
        if hand.value >= winning[1]:
            winning = hand.name, hand.value
    print(winning)

    table._turn()
    for hand in hands:
        hand.show(table)
        if hand.value >= winning[1]:
            winning = hand.name, hand.value
    print(winning)

    table._river()
    for hand in hands:
        hand.show(table)
        if hand.value >= winning[1]:
            winning = hand.name, hand.value
    print("WON: ", winning)


class Actions:
    fold = 0
    call = 1
    bet = 2
    check = 3

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = Hand(self.name)

    def add_card(self, card, table=None):
        if not self.hand:
            self.hand.add_card(card, table)

    def act(self, actions, bet):  # actions = dictionary: name:(action, amount)
        if bet > 5:
            return Actions.fold, 0
        else:
            return Actions.call, bet




def print_hi(name):
    deal(5)
    # Use a breakpoint in the code line below to debug your script.
    print("LETS GO")  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
