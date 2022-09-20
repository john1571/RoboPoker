import pack as p

import hand_helpers
def test_value(name, expected_value, cards):
    hand = hand_helpers.Hand(name)
    for card in cards:
        hand.add_card(hand_helpers.Shorthand[card])
    if expected_value != hand.get_value():
        print("expected: %i" % expected_value)
        print("actual: %i" % hand.get_value())
        print(i)
        return False
    return True


def run_tests():
    test_value('pair_twos', 302, ['2h', '2c'])
    test_value('3-high', 3, ['3h', '2h'])
    test_value('4-high', 4, ['4h', '2h'])
    test_value('flush', 730, ['3h', '2h', 'Qh', '4d', '6h', '10s', '7h'])
    test_value('straight', 606, ['3h', '2h', '4c', '5d', '6d'])
    test_value('set', 503, ['3h', '2h', '3d', '4c', '3s'])



HEART = '♥'
CLUB = '♣'
DIAMOND = '♦'
SPADE = '♠'

if __name__ == '__main__':
    run_tests()