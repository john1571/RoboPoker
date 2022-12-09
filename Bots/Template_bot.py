from Bots import base_player as bp
import Bots.bot_helpers as b

# Copy this template to create a new bot.
# Add your bot class in the Register array.
# Watch it compete

class YourBotName(bp.Player):
    # bet: current bet at the table.
    # my_bet: amount of money you have already put in the pot
    # actions: a dictionary of actions from other players
    def act(self, bet, my_bet, table=None, pot=None,  players_in_round=None, json_data=None):
        data = b.dictionary_from_json_data(json_data)
        bet = data['bet']
        my_bet = data['self']['chips_in_round']
        num_cards = self.get_num_cards()
        hand_value = self.get_hand_value()

        def call():
            return data['bet'] - data['self']['chips_in_round']

        def raise_x_(x):
            return (data['bet'] * x) - my_bet

        def all_in():
            return self.chips

        def fold():
            return None  # return None to fold

        # YOUR CODE GOES HERE
        return call()


    # Change this function to return your bot type
    def bot_type(self):
        return "Your_bot_type"
