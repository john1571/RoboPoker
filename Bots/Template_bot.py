from Bots import base_player as bp
import Bots.bot_helpers as b

# Copy this template to create a new bot.
# Add your bot class in the Register array.
# Watch it compete

class YOUR_BOT_NAME(bp.Player):
    # bet: current bet at the table.
    # my_bet: amount of money you have already put in the pot
    # actions: a dictionary of actions from other players
    def act(self, bet, my_bet, table=None, actions=None, pot=None):  # actions = dictionary: {name: amount}
        num_cards = self.get_num_cards()
        hand_value = self.get_hand_value()
        self.hand.cards         # array of cards available (on the table and in your hand)
        self.hand.cards_in_hand # array of cards in your hand
        for card in self.hand.cards:
            card.rank #
            card.suit #
            card.value #

        def call():
            return bet - my_bet

        def raise_x_(x):
            return (bet * x) - my_bet

        def all_in():
            return self.chips

        def fold():
            return None  # return None to fold

        # YOUR CODE GOES HERE

        # Example (replace this code with your own):
        if num_cards == 2: # If I have only two cards
            hand_value >= b.value_of(['Kh', 'Kd']): # and they are pocket kings or aces
                return all_in() # go all in
            elif hand_value >= b.value_of(['10h', '10d']): # if they are good
                return raise_x_(2) # double the bet
            elif hand_value >= b.value_of(['Ah']): # if they are ok
                return call() # just call
            else:   # if I don't even have an Ace high,
                return fold() # fold quickly

        # If I have more than two cards:
        if hand_value >= b.value_of(['5h', '6d', '7c', '8h', '9c']): # If I have a straight
            return raise_x_(3) # triple the bet
        elif hand_value >= b.value_of(['Kh', 'Kd']): # if I have at least a pair of kings
            if bet == 0: # If nobody else is betting
                return 15 # bet a small bet
            elif call() < (self.chips / 20): # if they are betting, but it isn't a big bet to call
                return call() # then call
        else: # if I don't even have a pair of kings at this point
            return fold() # run away!


    # Change this function to return your bot type
    def bot_type(self):
        return "Your_bot_type"
