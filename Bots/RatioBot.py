import random

from Bots import base_player as bp
import Bots.bot_helpers as b

# Copy this template to create a new bot.
# Add your bot class in the Register array.
# Watch it compete

class Ratio(bp.Player):
    # bet: current bet at the table.
    # my_bet: amount of money you have already put in the pot
    # actions: a dictionary of actions from other players
    def act(self, bet, my_bet, table=None, pot=None,  players_in_round=None, json_data=None):
        num_cards = self.get_num_cards()
        hand_value = self.get_hand_value()


        def call():
            return bet - my_bet

        def raise_x_(x):
            return (bet * x) - my_bet

        def all_in():
            return self.chips

        def fold():
            return None  # return None to fold

        # YOUR CODE GOES HERE
        expected = bet - my_bet

        if self.chips < expected:
            return all_in()

        if self.chips < expected * 2:
            return raise_x_(4)

        if self.chips < expected * 3:
            return raise_x_(3)

        if self.chips < expected * 4:
            return raise_x_(2)

        i = random.randint(0,3)
        if i == 0:
            return fold()
        if i == 1:
            return call()
        else:
            return raise_x_(i)

    # Change this function to return your bot type
    def bot_type(self):
        return "Ratio"
