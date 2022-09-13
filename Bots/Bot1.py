
import base_player as bp
import random

class Bot1(bp.Player):
    def bet(self, amount):
        self.chips -= amount
        return amount

    def act(self, bet, my_bet, actions=None):  # actions = dictionary: name:(action, amount)
        if bet > 0:
            if self.folded:
                return self.fold()
            if my_bet != 0 and bet > my_bet * 5:
                return self.fold()
            if random.randint(0, 10) == 8:
                my_bet = (bet * 2) - my_bet
                return self.bet(my_bet)
            return self.bet(bet - my_bet)
        else:
            if random.randint(0, 10) > 5:
                my_bet = 5
            else:
                my_bet = 0
            return self.bet(my_bet)
