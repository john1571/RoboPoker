from Bots import base_player as bp
import Bots.bot_helpers as b


class JoanBot1(bp.Player):
    def act(self, json_data=None):
        data = b.dictionary_from_json_data(json_data)
        bet = data['bet']
        my_bet = data['my_bet']
        def call():
            return bet - my_bet

        def raise_x_(x):
            return (bet * x) - my_bet

        def all_in():
            return self.chips

        num_cards = self.get_num_cards()
        hand_value = self.get_hand_value()
        if num_cards == 2:
            if hand_value >= b.value_of(['Jh', 'Jd']):  # all-in
                return all_in()
            elif hand_value >= b.value_of(['8h', '8d']):  # raise for good hand
                return raise_x_(4)
            elif hand_value >= b.value_of(['Ah']) and bet - my_bet < (self.chips / 10):  # call if low bet
                return call()
        if num_cards > 2:
            if hand_value >= b.value_of(['5h', '6d', '7c', '8h', '9c']):
                return raise_x_(4)
            elif hand_value >= b.value_of(['Jh', 'Jd']):
                if bet == 0:
                    return 15
                elif bet - my_bet < (self.chips / 15):
                    return raise_x_(3)
        if bet == 0:
            return 5
        elif bet - my_bet < (self.chips / 50):
            return raise_x_(3)
        return call()

    def bot_type(self):
        return "JoanBot1"
