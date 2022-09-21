from Bots import base_player as bp
import Bots.bot_helpers as b


class YOUR_BOT_NAME(bp.Player):
    def act(self, bet, my_bet, table=None, actions=None, pot=None):  # actions = dictionary: {name: amount}
        def call():
            return bet - my_bet

        def raise_x_(x):
            return (bet * x) - my_bet

        def all_in():
            return self.chips

        num_cards = self.get_num_cards()
        hand_value = self.get_hand_value()
        if num_cards == 2:
            if hand_value >= b.value_of(['Ah', 'Ad']):
                if pot and pot > self.chips / 10:
                    return all_in()
                elif pot == 0:

            elif hand_value >= b.value_of(['10h', '10d']):
                return call()
            elif hand_value >= b.value_of(['Ah']) and bet - my_bet < (self.chips / 10):
                return call()
        if num_cards > 2:
            if hand_value >= b.value_of(['5h', '6d', '7c', '8h', '9c']):
                return (bet * 3) - my_bet
            elif hand_value >= b.value_of(['Kh', 'Kd']):
                if bet == 0:
                    return 15
                elif bet - my_bet < (self.chips / 20):
                    return (bet * 2) - my_bet
        if bet == 0:
            return 5
        elif bet - my_bet < (self.chips / 50):
            return (bet * 2) - my_bet
        return None

    def bot_type(self):
        return "Your_bot_name"
