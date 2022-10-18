from Bots import base_player as bp


class CallingStation(bp.Player):
    def act(self, bet, my_bet, table=None, actions=None, pot=None):  # actions = dictionary: name:(action, amount)
        def call():
            return bet - my_bet
        return call()

    def bot_type(self):
        return "Calling Station"
