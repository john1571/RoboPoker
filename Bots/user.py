from Bots import base_player as bp


class User(bp.Player):
    def act(self, bet, my_bet, table=None, actions=None, pot=None,  players_in_round=None):  # actions = dictionary: name:(action, amount)
        self.show_hand(table)
        print("Pot is %i\nMinimum bet to stay in: %i\nyour chips: %i" % (pot, bet - my_bet, self.chips))
        response = input('integer for a bet, "All" for all in, anything else will fold: ')
        if str(response) == "All":
            return self.chips
        try:
            return int(response)
        except:
            return None

    def bot_type(self):
        return "user"
