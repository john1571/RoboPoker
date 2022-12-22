from Bots import base_player as bp
import Bots.bot_helpers as b

# Copy this template to create a new bot.
# Add your bot class in the Register array.
# Watch it compete


callers = []
average_hand_value = {}
class JPBot5_3(bp.Player):
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
        if len(callers) > 0:
            raise_by = 0
            for player in data['opponents']:
                if player['folded']:
                    continue
                if player['name'] in callers:
                    raise_by = player['chips'] + player['chips_in_pot'] - self.chips_in_pot
            if raise_by > 0 and b.value_of(['2h', '2s', '2c']) <= self.get_hand_value():
                return max([raise_by, data['bet'] - data['my_bet']])
        if len(data['table_cards']) > 2 and data['round_num'] > 10:
            should_raise = True
            raise_by_array = []
            for player in data['opponents']:
                if player['name'] == self.name or player['folded'] or player['busted']:
                    continue
                if average_hand_value.get(player['name'], None) is None:
                    continue
                if average_hand_value[player['name']] > self.get_hand_value()[0]:
                    should_raise = False
                else:
                    raise_by_array.append(player['chips'] + player['chips_in_pot'] - self.chips_in_pot)
            if should_raise and len(raise_by_array) > 0:
                raise_by_array.append(data['bet'] - data['my_bet'])
                return max(raise_by_array)
        if bet - my_bet > data['big_blind'] * 3:
            return None
        else:
            return max([bet - my_bet, 5])


    # Change this function to return your bot type
    def bot_type(self):
        return "Student"

    def observe_showdown(self, json_data):
        # If you like you can even use this data to improve your bot.
        '''
        updated 12/10/22
        showdown_data = {
        'round_num': round_num,
        'table_cards': _Table.to_string(),
        'big_blind': big_blind,
        'pot': log_pot,
        'players': [player_data.to_json_string],
        'chip_differential': {player_name: player_chip_differential},
        }'''

        data = b.dictionary_from_json_data(json_data)
        players = data['players']
        if data['round_num'] == 0:
            callers.clear()
            average_hand_value.clear()
            for bot in players:
                if bot['name'] == self.name:
                    continue
                average_hand_value[bot['name']] = 0
                callers.append(bot['name'])

        for player in players:
            if player['name'] == self.name or player['name'] not in callers:
                continue
            if player['folded'] or player['busted']:
                callers.remove(player['name'])

        for player in players:
            if player['name'] == self.name or player['folded'] or player['busted']:
                continue
            if player['hand_cards'] == []:
                continue
            player_hand = b.value_of(data['table_cards']+player['hand_cards'])
            weight = data['round_num']
            if weight < 0:
                return
            old_average = average_hand_value[player['name']]
            new_average = ((old_average*weight) + player_hand[0])/(weight + 1)
            average_hand_value[player['name']] = new_average