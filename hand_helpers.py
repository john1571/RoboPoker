import pack as p

STRAIGHT_FLUSH = 1300
FOUR_OF_A_KIND = 900
FULL_HOUSE = 800
FLUSH = 700
STRAIGHT = 600
SET = 500
TWO_PAIR = 400
PAIR = 300


Shorthand = {
    '2h': p.Card('♥', '2'),
    '4h': p.Card('♥', '4'),
    '3h': p.Card('♥', '3'),
    '5h': p.Card('♥', '5'),
    '6h': p.Card('♥', '6'),
    '7h': p.Card('♥', '7'),
    '8h': p.Card('♥', '8'),
    '9h': p.Card('♥', '9'),
    'Th': p.Card('♥', 'T'),
    'Jh': p.Card('♥', 'J'),
    'Qh': p.Card('♥', 'Q'),
    'Kh': p.Card('♥', 'K'),
    'Ah': p.Card('♥', 'A'),
    '2c': p.Card('♣', '2'),
    '3c': p.Card('♣', '3'),
    '4c': p.Card('♣', '4'),
    '5c': p.Card('♣', '5'),
    '6c': p.Card('♣', '6'),
    '7c': p.Card('♣', '7'),
    '8c': p.Card('♣', '8'),
    '9c': p.Card('♣', '9'),
    'Tc': p.Card('♣', 'T'),
    'Jc': p.Card('♣', 'J'),
    'Qc': p.Card('♣', 'Q'),
    'Kc': p.Card('♣', 'K'),
    'Ac': p.Card('♣', 'A'),
    '2d': p.Card('♦', '2'),
    '3d': p.Card('♦', '3'),
    '4d': p.Card('♦', '4'),
    '5d': p.Card('♦', '5'),
    '6d': p.Card('♦', '6'),
    '7d': p.Card('♦', '7'),
    '8d': p.Card('♦', '8'),
    '9d': p.Card('♦', '9'),
    'Td': p.Card('♦', 'T'),
    'Jd': p.Card('♦', 'J'),
    'Qd': p.Card('♦', 'Q'),
    'Kd': p.Card('♦', 'K'),
    'Ad': p.Card('♦', 'A'),
    '2s': p.Card('♠', '2'),
    '3s': p.Card('♠', '3'),
    '4s': p.Card('♠', '4'),
    '5s': p.Card('♠', '5'),
    '6s': p.Card('♠', '6'),
    '7s': p.Card('♠', '7'),
    '8s': p.Card('♠', '8'),
    '9s': p.Card('♠', '9'),
    'Ts': p.Card('♠', 'T'),
    'Js': p.Card('♠', 'J'),
    'Qs': p.Card('♠', 'Q'),
    'Ks': p.Card('♠', 'K'),
    'As': p.Card('♠', 'A'),
}


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
        self.value = 0
        self.value_dictionary = {}
        self.hand_value = [0, 0, 0, 0, 0, 0] # hand combination value, followed by 5 card values in order

    def add_card(self, card, table=None):
        if card in self.cards:
            return
        self.cards.append(card)
        if not table:
            self.cards_in_hand.append(card)

        if card.suit == p.HEART:
            self.hearts.append(card.value)
        elif card.suit == p.DIAMOND:
            self.diamonds.append(card.value)
        elif card.suit == p.SPADE:
            self.spades.append(card.value)
        else:
            self.clubs.append(card.value)
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

    def log(self):
        string = ''
        for card in self.cards_in_hand:
            string += card.log_string() + " "
        string += ','
        return string

    def show(self, table, print_now=False):
        print_string = ""
        print_string += "%s: \t" % self.name
        for card in self.cards_in_hand:
            card.print_with_color()
        for card in get_table_cards(table):
            self.add_card(card, table)
        print_string += str(self.get_value()) + '\t'
        if self.has_flush():
            print_string += "FLUSH"
        elif self.has_straight():
            print_string += "STRAIGHT!"
        elif self.has_set():
            print_string += "THREE!"
        elif len(self.has_pair()) > 1:
            print_string += "TWO PAIR!"
        elif self.has_pair():
            print_string += "PAIR!"
        else:
            print_string += "Hi card"
        if print_now:
            print(print_string)
        return print_string

    def get_value(self):
        other_values = []
        for card in self.cards:
            other_values.append(card.value)
        other_values = sorted(other_values, reverse=True)
        if len(self.cards) <= 0:
            return []
        flush_cards = self.has_flush()
        if flush_cards:
            high_card = straight_in_array(flush_cards)
            if high_card:
                self.hand_value[0] = STRAIGHT_FLUSH
                self.hand_value[1] = high_card
                self.has_straight_flush = True
                return self.hand_value
        if len(self.four) > 0:
            self.hand_value[0] = FOUR_OF_A_KIND
            self.hand_value[1] = self.four[0]
            return self.hand_value
        if self.has_full_house():
            self.hand_value[0] = FULL_HOUSE
            self.hand_value[1] = max(self.has_set())
            return self.hand_value
        if flush_cards:
            self.hand_value = sorted(flush_cards, reverse=True)[:5]
            self.hand_value.insert(0, FLUSH)
            return self.hand_value
        if self.has_straight():
            self.hand_value[0] = STRAIGHT
            self.hand_value[1] = self.has_straight()
            return self.hand_value
        if self.has_set():
            sets = self.has_set()
            high_set_value = max(sets)
            self.hand_value[0] = SET
            self.hand_value[1] = high_set_value
            return self.hand_value
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
                self.hand_value[0] = TWO_PAIR
                self.hand_value[1] = high_pair_value
                self.hand_value[2] = other_pair_value
                for value in other_values:
                    if value in self.hand_value:
                        continue
                    self.hand_value[3] = value
                    break
                return self.hand_value
            self.hand_value[0] = PAIR
            self.hand_value[1] = self.has_pair()[0]
            count = 2
            for value in other_values:
                if count >= len(self.hand_value):
                    break
                if value in self.hand_value or value == 0:
                    continue
                self.hand_value[count] = value
                count += 1
            return self.hand_value
        else:
            count = 0
            for value in other_values:
                if count >= len(self.hand_value):
                    break
                if value in self.hand_value or value == 0:
                    continue
                self.hand_value[count] = value
                count += 1
            return self.hand_value

    def show_for_print(self):
        show_string = ""
        for card in self.cards_in_hand:
            show_string += card.get_with_color() + ' '
        return show_string

    def get_hand_string(self, table):
        for card in get_table_cards(table):
            self.add_card(card, table)
        if self.has_straight_flush:
            return "Str Flsh"
        elif self.has_four():
            return "4-o-kind"
        elif self.has_full_house():
            return "fll hous"
        elif self.has_flush():
            return "flush"
        elif self.has_straight():
            return "straight"
        elif self.has_set():
            return "set"
        elif self.has_pair():
            if len(self.has_pair()) > 1:
                return "2 pair"
            else:
                return "pair"
        else:
            return "hi card"

    def has_full_house(self):
        sets = self.has_set()
        if not sets:
            return False
        if len(sets) > 1:
            set_val = max(sets)
            return set_val
        if not self.has_pair():
            return False
        return sets[0]

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
        if 'T' in self.value_dictionary.keys():
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
    if 10 in array:
        highstart = march_list(array, [9, 8, 7, 6], False, 10)
        highend = march_list(array, [11, 12, 13, 14], True, 10)
        if (highend - highstart) >= 4:
            return highend
    if 5 in array:
        lowstart = march_list(array, [4, 3, 2, 14], False, 5)
        lowend = march_list(array, [6, 7, 8, 9], True, 5)

        if (lowend - lowstart) >= 4:
            return lowend
    return None


def get_table_cards(table):
    table_cards = []
    for card in table.cards_on_table:
        table_cards.append(card)
    return table_cards
