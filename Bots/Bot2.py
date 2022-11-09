from Bots import base_player as bp
import random


class Bot2(bp.Player):
    def act(self, bet, my_bet, table=None, actions=None, pot=None,  players_in_round=None):  # actions = dictionary: name:(action, amount)
        if self.hand.get_value() > 310:
            if bet > 20:
                return bet*2
            return 40
        elif self.hand.get_value() < 10:
            return None
        if bet > 0:
            if my_bet != 0 and bet > my_bet * 5:
                return self.fold()
            if random.randint(0, 10) == 8:
                my_bet = (bet * 2) - my_bet
                return my_bet
            return bet - my_bet
        else:
            if random.randint(0, 10) > 5:
                my_bet = 5
            else:
                my_bet = 0
            return my_bet

    def bot_type(self):
        return "bot2"
