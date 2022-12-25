from Bots import base_player as bp
from Bots import bot_helpers as b

class CallingStation(bp.Player):
    def act(self, json_data=None):
        data = b.dictionary_from_json_data(json_data)

        def call():
            return data['call']
        return call()

    def bot_type(self):
        return "Calling Station"
