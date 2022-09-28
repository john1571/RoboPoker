import pack as p
import hand_helpers as hh
import math

def value_of(cards, name='jehosephat'):
    hand = hh.Hand(name)
    for card in cards:
        hand.add_card(hh.Shorthand[card])
    return hand.get_value()


def call(bet, my_bet):
    return bet - my_bet

def average(array):
    if len(array) < 1:
        return 0
    return round(sum(array)/len(array))

class Stats:
    def __init__(self, chips):
        self.winnings = []
        self.losses = []
        self.rounds = 0
        self.losses_when_folded = []
        self.last_chips = chips
        self.busted = False

    def folded(self, chips):
        self.rounds += 1
        self.losses.append(self.last_chips - chips)
        self.losses_when_folded.append(self.last_chips - chips)
        self.last_chips = chips

    def update(self, chips):
        self.rounds += 1
        if chips == self.last_chips:
            return
        if chips > self.last_chips:
            self.winnings.append(chips - self.last_chips)
        if chips < self.last_chips:
            self.losses.append(self.last_chips - chips)
        self.last_chips = chips

    def av_win(self):
        return average(self.winnings)

    def av_loss(self):
        return average(self.losses)

    def av_folded(self):
        return average(self.losses_when_folded)

    def av_delta(self):
        if self.rounds < 1:
            return 0
        return round((sum(self.winnings) - sum(self.losses))/self.rounds)

    def percent_won(self):
        won = len(self.winnings)
        if won == 0:
            return 0
        return round((won/self.rounds) * 100)

    def best_win(self):
        return max(self.winnings)

    def worst_loss(self):
        return min(self.losses)
