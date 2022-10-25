import hand_helpers as hands
import globals
import time
import Bots.bot_helpers as b
import game_play as gp

class Actions:
    fold = 0
    call = 1
    bet = 2
    check = 3
    allin = 4


class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.has_bet = False
        self.busted = False
        self.folded = False
        self.all_in = False
        self.big_blind = False
        self.hand = hands.Hand(self.name)
        self.type = self.bot_type()
        self.stats = b.Stats(self.chips)
        self.chips_in_pot = 0
        self.chips_in_round = 0

    def new_betting_round(self):
        self.has_bet = False
        self.chips_in_round = 0

    def new_hand(self):
        self.folded = False
        self.hand = hands.Hand(self.name)
        self.chips_in_pot = 0
        self.chips_in_round = 0
        if self.chips <= 0:
            self.bust()
        else:
            self.all_in = False

    def bust(self):
        self.busted = True
        self.hand = None

    def fold(self):
        self.folded = True
        return None

    def act(self, bet, my_bet, table=None, actions=None, pot=None):
        if bet - my_bet > 50:
            return None
        else:
            return bet - my_bet

    def can_bet(self, players):
        if self.folded or self.all_in or self.busted:
            return False
        if self.has_bet and self.chips_in_round >= gp.get_current_bet(players):
            return False
        return True

    def outer_act(self, players, forced=0):
        if not self.can_bet(players):
            return 0
        current_bet = gp.get_current_bet(players)
        pot = gp.get_current_pot(players)
        if forced == 0:
            new_bet = self.act(current_bet, self.chips_in_round, None, None, pot)
            self.has_bet = True
        else:
            new_bet = forced
        if new_bet:
            if new_bet >= self.chips:
                self.all_in = True
                new_bet = round(self.chips)
                self.chips = 0
                self.chips_in_pot += new_bet
                self.chips_in_round += new_bet
                return new_bet
            new_bet = round(new_bet)
            self.chips -= new_bet
            self.chips_in_pot += new_bet
            self.chips_in_round += new_bet
        return new_bet

    def add_card(self, card, table=None):
        self.hand.add_card(card, table)

    def status(self, table):
        self.show_hand(table)
        print(self.bot_type())
        print(self.chips)

    def show_hand(self, table, print_now=False):
        if print_now:
            print(self.hand.show(table))
        if self.hand:
            return self.hand.show(table)
        return ""

    def bot_type(self):
        return "base_player"

    def get_hand_value(self):
        if self.hand:
            return self.hand.get_value()
        return 0

    def get_num_cards(self):
        if self.hand:
            return len(self.hand.cards)
        return 0

    def update_stats(self):
        if self.stats.busted:
            return
        if self.folded:
            self.stats.folded(self.chips)
        else:
            self.stats.update(self.chips)
        if self.busted:
            self.stats.busted = True
