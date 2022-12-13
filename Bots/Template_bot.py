from Bots import base_player as bp
import Bots.bot_helpers as b

# Copy this template to create a new bot.
# Add your bot class in the Register array.
# Watch it compete
'''
Updated 12/10/2022
data = {
    'round_num': round_num,
    'table_cards': cards_on_table_json,
    'pot': pot,
    'bet': current_bet,
    'call': current_bet - self.chips_in_round,
    'my_bet': self.chips_in_round,
    'self': self.bot_data,
    'opponents': [opponents.bot_data],
}

bot_data  = {
    "name": self.name,
    "type": self.bot_type(),
    "hand_cards": [] if hide_cards else self.hand.to_json(),
    "chips": self.chips,
    "chips_in_pot": self.chips_in_pot,
    "chips_in_round": self.chips_in_round,
    "first_bet": not self.has_bet,
    "folded": self.folded,
    "busted": self.busted
}
'''


class YourBotName(bp.Player):
    # bet: current bet at the table.
    # my_bet: amount of money you have already put in the pot
    def act(self, json_data=None):
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

    def observe_showdown(self, json_data):
        # If you like you can even use this data to improve your bot.
        """
        updated 12/10/22
        showdown_data = {
        'round_num': round_num,
        'table_cards': _Table.to_string(),
        'big_blind': big_blind,
        'pot': log_pot,
        'players': [player_data.to_json_string],
        'chip_differential': {player_name: player_chip_differential},
        }"""

