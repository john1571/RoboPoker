import pack as p
Shorthand = {
    '2h': p.Card('♥', '2'),
    '4h': p.Card('♥', '4'),
    '3h': p.Card('♥', '3'),
    '5h': p.Card('♥', '5'),
    '6h': p.Card('♥', '6'),
    '7h': p.Card('♥', '7'),
    '8h': p.Card('♥', '8'),
    '9h': p.Card('♥', '9'),
    '10h': p.Card('♥', '10'),
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
    '10c': p.Card('♣', '10'),
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
    '10d': p.Card('♦', '10'),
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
    '10s': p.Card('♠', '10'),
    'Js': p.Card('♠', 'J'),
    'Qs': p.Card('♠', 'Q'),
    'Ks': p.Card('♠', 'K'),
    'As': p.Card('♠', 'A'),
}
import hand_helpers
def test_value(name, expected_value, cards):
    hand = hand_helpers.Hand(name)
    for card in cards:
        hand.add_card(Shorthand[card])
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