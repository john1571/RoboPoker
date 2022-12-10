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
        self.card_value_array = []
        self.hand_value = [0] # hand combination value, followed by 5 card values in order

    def add_card(self, card, table=None):
        if card in self.cards:
            return
        self.cards.append(card)
        self.card_value_array.append(card.value)
        if not table:
            self.cards_in_hand.append(card)

    def to_json(self):
        json_array = []
        for card in self.cards_in_hand:
            json_array.append(card.to_json_string())
        return json_array
    
    def log(self):
        string = ''
        for card in self.cards_in_hand:
            string += card.log_string() + " "
        string += ','
        return string

    def show_for_print(self):
        show_string = ""
        for card in self.cards_in_hand:
            show_string += card.get_with_color() + ' '
        return show_string

    def get_hand_string(self):
        if self.has_straight_flush():
            return "Str Flsh"
        elif self.has_four_of_a_kind():
            return "4-o-kind"
        elif self.has_full_house():
            return "fll hous"
        elif self.has_flush():
            return "flush"
        elif self.has_straight():
            return "straight"
        elif self.has_set():
            return "set"
        elif self.has_two_pair():
            return "2 pair"
        elif self.has_pair():
            return "pair"
        else:
            return "hi card"

    def get_value(self):
        value_array =[
            self.has_straight_flush,
            self.has_four_of_a_kind,
            self.has_full_house,
            self.has_flush,
            self.has_straight,
            self.has_set,
            self.has_two_pair,
            self.has_pair,
            self.high_card,
        ]
        hand_multiplier = 1000
        for check_hand in value_array:
            self.hand_value = check_hand()
            if self.hand_value:
                self.hand_value = self.hand_value[:5]
                self.hand_value.insert(0, hand_multiplier)
                return self.hand_value
            hand_multiplier -= 100
        assert False

    def has_straight_flush(self):
        flush_cards = self.has_flush()
        if flush_cards:
            return straight_in_array(flush_cards)
        return None

    def check_count(self, number):
        number_matches = []
        card_value = 14
        while card_value > 1:
            if self.card_value_array.count(card_value) >= number:
                number_matches.append(card_value)
            card_value -= 1
        return number_matches or None

    def has_four_of_a_kind(self):
        return self.check_count(4)

    def has_full_house(self):
        sets = self.has_set()
        if not sets:
            return None
        set_value = max(sets)
        if not self.has_pair():
            return None
        else:
            pair_value = 0
            for value in self.has_pair():
                if value == set_value:
                    continue
                if value > pair_value:
                    pair_value = value
        if set_value == 0 or pair_value == 0:
            return None
        return [set_value, pair_value]

    def has_flush(self):
        hearts = []
        diamonds = []
        clubs = []
        spades = []
        flush_cards = []
        # loop through all cards before deciding on flush. To find potential straight flushes.
        for card in self.cards:
            if card.suit == p.HEART:
                hearts.append(card.value)
            elif card.suit == p.DIAMOND:
                diamonds.append(card.value)
            elif card.suit == p.SPADE:
                spades.append(card.value)
            else:
                clubs.append(card.value)

        if len(spades) > 4:
            flush_cards = spades
        if len(diamonds) > 4:
            flush_cards = diamonds
        if len(clubs) > 4:
            flush_cards = clubs
        if len(hearts) > 4:
            flush_cards = hearts
        if flush_cards:
            return sorted(flush_cards, reverse=True) or None
        return None

    def has_straight(self):
        value_array = []
        for card in self.cards:
            value_array.append(card.value)
        return straight_in_array(value_array)

    def has_set(self):
        return self.check_count(3)

    def has_two_pair(self):
        if not self.has_pair():
            return None
        if len(self.has_pair()) < 2:
            return None
        if len(self.has_pair()) == 2:
            return sorted(self.has_pair(), reverse=True)
        pairs = []
        for pair in self.has_pair():
            if pair != min(self.has_pair()):
                pairs.append(pair)
        assert len(pairs) == 2
        return sorted(pairs, reverse=True)

    def has_pair(self):
        return self.check_count(2)

    def high_card(self):
        card_values = []
        for card in self.cards:
            card_values.append(card.value)
        card_values = sorted(card_values, reverse=True)
        if not card_values:
            return [0]
        return card_values[:5]


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
            return [highend]
    if 5 in array:
        lowstart = march_list(array, [4, 3, 2, 14], False, 5)
        lowend = march_list(array, [6, 7, 8, 9], True, 5)
        if (lowend - lowstart) >= 4:
            return [lowend]
    return None
