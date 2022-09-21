import pack as p
import hand_helpers as hh


def value_of(cards, name='jehosephat'):
    hand = hh.Hand(name)
    for card in cards:
        hand.add_card(hh.Shorthand[card])
    return hand.get_value()


