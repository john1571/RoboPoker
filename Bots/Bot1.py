from Bots import base_player as bp
from Bots import bot_helpers as b
import random


class Bot1(bp.Player):
    def act(self, json_data=None):
        data = b.dictionary_from_json_data(json_data)
        bet = data['bet']
        my_bet = data['my_bet']
        if bet > 0:
            if my_bet != 0 and bet > my_bet * 5:
                return None
            if random.randint(0, 10) == 8:
                return (bet * 2) - my_bet
            return bet - my_bet
        else:
            if random.randint(0, 10) > 5:
                return 5
            else:
                return 0

    def bot_type(self):
        return "bot1"
