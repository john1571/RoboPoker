from Bots import base_player as bp
from Bots import bot_helpers as b
import random


class Bot2(bp.Player):
    def act(self, json_data=None):
        data = b.dictionary_from_json_data(json_data)
        bet = data['bet']
        my_bet = data['my_bet']
        sum_value = sum(self.hand.get_value())
        if sum_value >= 300:
            if bet > 20:
                return bet*2
            return 40
        elif sum_value < 10:
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
