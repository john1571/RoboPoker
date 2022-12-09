from Bots import base_player as bp


class CallingStation(bp.Player):
    def act(self, bet, my_bet, table=None, pot=None,  players_in_round=None, json_data=None):  
        def call():
            return bet - my_bet
        return call()

    def bot_type(self):
        return "Calling Station"
