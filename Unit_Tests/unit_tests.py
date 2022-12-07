import pack as p
import Bots.bot_helpers as b
import Bots.base_player as bp
import hand_helpers
import game_play as gp
import Test_cases as tc

def test_value(name, expected_value, cards):
    hand = hand_helpers.Hand(name)
    for card in cards:
        hand.add_card(hand_helpers.Shorthand[card])
    if expected_value != hand.get_value():
        print("expected: ", end="")
        print(expected_value)
        print("actual: ", end="")
        print(hand.get_value())
        print(i)
        return False
    return True



def test_round(player_dictionary, betting, ending_chips):  # player {name:{cards:[],chips:1000}
    players = {}
    player_array = []
    for player_name, initial_values in player_dictionary.items():
        player = bp.Player(player_name, initial_values['chips'])
        for card in initial_values['cards']:
            card_full = hand_helpers.Shorthand[card]
            player.add_card(card_full)
        players[player.name] = player
        player_array.append(player)
    for round in betting.keys():
        for name, bet in betting[round]:
            under_gun = players[name]
            if under_gun.busted or under_gun.folded or under_gun.all_in:
                continue
            if bet is None:
                under_gun.fold()
                continue
            under_gun.outer_act(player_array, bet)
    gp.payout_new(player_array)
    for name, chips in ending_chips:
        if players[name].chips != chips:
            print("****Ending chip discrepency****")
            print('PLayer name: %s' % name)
            print('Value expected from input: %s' % str(chips))
            print('Value from simulated play: %s' % str(players[name].chips))
            assert False

def test_rounds():
    for dict, betting, expected in tc.test_round_cases():
        test_round(dict, betting, expected)


def hands_equal(hand1_value, hand2_value):
    if hand1_value > hand2_value:
        print("hand 1:")
        print(hand1_value)
        print("is greater than hand 2:")
        print(hand2_value)
        return False
    elif hand2_value > hand1_value:
        print("hand 2:")
        print(hand2_value)
        print("is greater than hand 1:")
        print(hand1_value)
        return False
    else:
        return True


def run_tests():
    test_rounds()
    test_value('3-high', [3, 2, 0, 0, 0, 0], ['3h', '2h'])
    test_value('4-high', [4, 2, 0, 0, 0, 0], ['4h', '2h'])
    test_value('pair_twos', [300, 2, 0, 0, 0, 0], ['2h', '2c'])
    test_value('two_pair', [400, 3, 2, 0, 0, 0], ['2h', '2c', '3d', '3h'])
    test_value('set', [500, 3, 0, 0, 0, 0], ['3h', '2h', '3d', '4c', '3s'])
    test_value('straight', [600, 6, 0, 0, 0, 0], ['3h', '2h', '4c', '5d', '6d'])
    test_value('straight', [600, 14, 0, 0, 0, 0], ['Ah', 'Kh', 'Qc', 'Jd', 'Td', '9s', '8d'])
    test_value('flush', [700, 12, 7, 6, 3, 2], ['3h', '2h', 'Qh', '4d', '6h', 'Ts', '7h'])
    test_value('fll house', [800, 3, 3, 3, 2, 2], ['3h', '2h', '3d', '3c', '2d', 'Ts', '7h'])
    test_value('fll house', [800, 11, 11, 11, 14, 14], ['Jh', 'Ah', 'Jd', 'Jc', 'Ad', 'Ks', 'Kh'])
    test_value('fll house', [800, 12, 12, 12, 10, 10], ['Qh', 'Th', 'Qd', 'Qc', 'Td', 'Ts', '7h'])
    test_value('four-of-a-kind', [900, 7, 0, 0, 0, 0], ['7h', '7d', '7c', '4d', '6h', 'Ts', '7s'])
    test_value('four-of-a-kind', [900, 7, 0, 0, 0, 0], ['7h', '7d', '7c', '4d', '4h', 'Ts', '7s'])
    test_value('Straight flush', [1300, 9, 0, 0, 0, 0], ['8h', '7h', '6h', '5h', '9h', 'Ts', '7s'])
    test_value('Straight flush', [1300, 14, 0, 0, 0, 0], ['Kh', 'Qh', 'Jh', 'Th', 'Ah', 'Ts', '7s'])
    test_value('Straight flush', [1300, 5, 0, 0, 0, 0], ['Ah', '5h', '4h', '3h', '2h', 'Ts', '7s'])
    test_value('Straight flush', [1300, 12, 0, 0, 0, 0], ['Ah', 'Kd', 'Qh', 'Jh', 'Th', '9h', '8h'])

    assert hands_equal(b.value_of(['9h', '2h', 'Qh', '4d', '6h', 'Th', '7h']),
                       b.value_of(['9h', '3h', 'Qh', 'Ad', '6h', 'Th', '7h']))
    flush_Q_7_6_3_2 = b.value_of(['3h', '2h', 'Qh', '4d', '6h', 'Ts', '7h'])
    flush_Q_6_4_3_2 = b.value_of(['3h', '2h', 'Qh', '4h', '6h', 'Ts', '7d'])
    assert flush_Q_7_6_3_2 > flush_Q_6_4_3_2
    four_value = b.value_of(['7h', '7d', '7c', '4d', '6h', 'Ts', '7s'])
    flush_value = b.value_of(['3h', '2h', 'Qh', '4h', '6h', 'Ts', '7d'])
    assert four_value > flush_value
    assert flush_Q_7_6_3_2 == flush_Q_7_6_3_2
    low_straight = b.value_of(['5h', '4d', '3c', '2s', 'Ah', '8h'])
    straight_six_to_two = b.value_of(['5h', '4d', '3c', '2s', '6h', '8h'])
    high_straight = b.value_of(['Ah', 'Kd', 'Qh', 'Jd', 'Ts', '8h'])
    full_house_kickers = b.value_of(['Kh', '6s', '3d', '3s', '4c', '4s', '4d'])
    full_house_better = b.value_of(['5h', '5d', '3d', '3s', '4c', '4s', '4d'])
    assert full_house_better > full_house_kickers
    assert straight_six_to_two > low_straight
    assert high_straight > straight_six_to_two
    assert high_straight > low_straight


HEART = '♥'
CLUB = '♣'
DIAMOND = '♦'
SPADE = '♠'

if __name__ == '__main__':
    run_tests()
