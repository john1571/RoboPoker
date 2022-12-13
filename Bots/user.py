from Bots import base_player as bp


class User(bp.Player):
    def act(self, json_data=None):
        response = input('integer for a bet, "All" for all in, anything else will fold: ')
        if str(response) == "All":
            return self.chips
        try:
            return int(response)
        except ValueError:
            return None

    def bot_type(self):
        return "user"
