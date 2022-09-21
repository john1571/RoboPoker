from Bots import base_player as bp
import Bots.bot_helpers as b

class Bot3(bp.Player):
    def act(self, bet, my_bet, table=None, actions=None, pot=None):  # actions = dictionary: {name: amount}
        num_cards = self.get_num_cards()
        hand_value = self.get_hand_value()
        if num_cards == 2:
            if hand_value >= b.value_of(['Kh', 'Kd']):
                return self.chips
            elif hand_value >= b.value_of(['10h', '10d']):
                if self.name not in actions.keys():
                    return (bet * 3) - my_bet
                return bet - my_bet
            elif hand_value >= b.value_of(['Ah']) and bet - my_bet < (self.chips / 10):
                return bet - my_bet
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
        return "bot3"
