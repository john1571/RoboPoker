from Bots import base_player as bp
import Bots.bot_helpers as b

# Copy this template to create a new bot.
# Add your bot class in the Register array.
# Watch it compete


callers = []

class JPBot5(bp.Player):
    def act(self, bet, my_bet, table=None, pot=None,  players_in_round=None, json_data=None):
        data = b.dictionary_from_json_data(json_data)
        opponents = data['opponents']
        opponent_names = []
        for opponent in opponents:
            opponent_names.append(opponent['name'])
        to_remove = []
        for name in callers:
            if name not in opponent_names:
                to_remove.append(name)
        for name in to_remove:
            callers.remove(name)
        for bot in opponents:
            if data['round_num'] == 0 and bot['name'] not in callers:
                callers.append(bot['name'])
            if bot['name'] in callers:
                if bot['busted'] or bot['folded']:
                    callers.remove(bot['name'])
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
        if len(callers) > 0:
            if b.value_of(['Th', 'Ts', 'Tc']) <= self.get_hand_value():
                return all_in()
        if bet - my_bet > data['big_blind'] * 3:
            return None
        else:
            return bet - my_bet


    # Change this function to return your bot type
    def bot_type(self):
        return "Call-Killer"
