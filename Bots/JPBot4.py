from Bots import base_player as bp
import Bots.bot_helpers as b


class Bot4(bp.Player):
    # bet: current bet at the table.
    # my_bet: amount of money you have already put in the pot
    # actions: a dictionary of actions from other players
    def act(self, bet, my_bet, table=None, actions=None, pot=None,  players_in_round=None):  # actions = dictionary: {name: amount}
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

        # WAY TOO VERBOSE
        if pot > (bet - my_bet)*20:
            if bet - my_bet > self.chips:
                if num_cards == 2:
                    if hand_value > b.value_of(['8h', '8d']):
                        return all_in()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['3h', '3d', '3c']):
                        return all_in()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Jh', 'Jd', 'Jc']):
                        return all_in()
                    else:
                        return fold()
            elif bet - my_bet > (self.chips / 2):
                if num_cards == 2:
                    if hand_value > b.value_of(['Jh', 'Jd']):
                        return all_in()
                    elif hand_value > b.value_of(['5h', '5d']):
                        return call()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['8h', '8d', '8c']):
                        return all_in()
                    elif hand_value > b.value_of(['Qh', 'Qd']):
                        return call()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Qh', 'Qd', 'Qc']):
                        return all_in()
                    elif hand_value > b.value_of(['2h', '2d', '2c']):
                        return call()
                    else:
                        return fold()
            elif bet - my_bet > (self.chips / 4):
                if bet - my_bet > self.chips:
                    if num_cards == 2:
                        if hand_value > b.value_of(['8h', '8d']):
                            return raise_x_(2)
                        else:
                            return fold()
                    elif num_cards == 5:
                        if hand_value > b.value_of(['3h', '3d', '3c']):
                            return raise_x_(2)
                        else:
                            return fold()
                    else:
                        if hand_value > b.value_of(['Jh', 'Jd', 'Jc']):
                            return raise_x_(2)
                        else:
                            return fold()
                elif bet - my_bet > (self.chips / 2):
                    if num_cards == 2:
                        if hand_value > b.value_of(['Jh', 'Jd']):
                            return raise_x_(2)
                        elif hand_value > b.value_of(['5h', '5d']):
                            return call()
                        else:
                            return fold()
                    elif num_cards == 5:
                        if hand_value > b.value_of(['8h', '8d', '8c']):
                            return raise_x_(2)
                        elif hand_value > b.value_of(['Qh', 'Qd']):
                            return call()
                        else:
                            return fold()
                    else:
                        if hand_value > b.value_of(['Qh', 'Qd', 'Qc']):
                            return raise_x_(2)
                        elif hand_value > b.value_of(['2h', '2d', '2c']):
                            return call()
                        else:
                            return fold()
            elif bet - my_bet > (self.chips / 8):
                if num_cards == 2:
                    if hand_value > b.value_of(['Jh', 'Jd']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['5h', '5d']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Ad']):
                        return call()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['8h', '8d', '8c']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['Qh', 'Qd']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Th', 'Td']):
                        return call()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Qh', 'Jd', 'Th', '9h', '8d']):
                        return raise_x_(4)
                    elif hand_value > b.value_of(['2h', '2d', '2c']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Jh', 'Jd', 'Th', 'Td']):
                        return call()
                    else:
                        return fold()
            elif bet - my_bet > (self.chips / 16):
                if num_cards == 2:
                    if hand_value > b.value_of(['Jh', 'Jd']):
                        return raise_x_(4)
                    elif hand_value > b.value_of(['5h', '5d']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Ad']):
                        return call()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['8h', '8d', '8c']):
                        return raise_x_(4)
                    elif hand_value > b.value_of(['Qh', 'Qd']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Th', 'Td']):
                        return call()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Qh', 'Jd', 'Th', '9h', '8d']):
                        return raise_x_(4)
                    elif hand_value > b.value_of(['2h', '2d', '2c']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Jh', 'Jd', 'Th', 'Td']):
                        return call()
                    else:
                        return fold()
            else:
                if num_cards == 2:
                    if hand_value > b.value_of(['Jh', 'Jd']):
                        return raise_x_(5)
                    elif hand_value > b.value_of(['5h', '5d']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['Ad']):
                        return raise_x_(2)
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['8h', '8d', '8c']):
                        return raise_x_(5)
                    elif hand_value > b.value_of(['Qh', 'Qd']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['Th', 'Td']):
                        return raise_x_(2)
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Qh', 'Jd', 'Th', '9h', '8d']):
                        return raise_x_(5)
                    elif hand_value > b.value_of(['2h', '2d', '2c']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['Jh', 'Jd', 'Th', 'Td']):
                        return raise_x_(2)
                    else:
                        return fold()
        else:
            if bet - my_bet > self.chips:
                if num_cards == 2:
                    if hand_value > b.value_of(['6h', '6d']):
                        return all_in()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['3h', '3d', '4c', '4c']):
                        return all_in()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Jh', 'Jd', 'Jc']):
                        return all_in()
                    else:
                        return fold()
            elif bet - my_bet > (self.chips / 2):
                if num_cards == 2:
                    if hand_value > b.value_of(['Jh', 'Jd']):
                        return all_in()
                    elif hand_value > b.value_of(['5h', '5d']):
                        return call()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['8h', '8d', '8c']):
                        return all_in()
                    elif hand_value > b.value_of(['Qh', 'Qd']):
                        return call()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Th', 'Td', 'Tc']):
                        return all_in()
                    elif hand_value > b.value_of(['3h', '3d', '4c', '4c']):
                        return call()
                    else:
                        return fold()
            elif bet - my_bet > (self.chips / 4):
                if bet - my_bet > self.chips:
                    if num_cards == 2:
                        if hand_value > b.value_of(['6h', '6d']):
                            return raise_x_(2)
                        else:
                            return fold()
                    elif num_cards == 5:
                        if hand_value > b.value_of(['3h', '3d', '4c', '4c']):
                            return raise_x_(2)
                        else:
                            return fold()
                    else:
                        if hand_value > b.value_of(['Jh', 'Jd', 'Jc']):
                            return raise_x_(2)
                        else:
                            return fold()
                elif bet - my_bet > (self.chips / 2):
                    if num_cards == 2:
                        if hand_value > b.value_of(['Jh', 'Jd']):
                            return raise_x_(2)
                        elif hand_value > b.value_of(['5h', '5d']):
                            return call()
                        else:
                            return fold()
                    elif num_cards == 5:
                        if hand_value > b.value_of(['8h', '8d', '8c']):
                            return raise_x_(2)
                        elif hand_value > b.value_of(['Qh', 'Qd']):
                            return call()
                        else:
                            return fold()
                    else:
                        if hand_value > b.value_of(['Qh', 'Qd', 'Qc']):
                            return raise_x_(2)
                        elif hand_value > b.value_of(['3h', '3d', '4c', '4c']):
                            return call()
                        else:
                            return fold()
            elif bet - my_bet > (self.chips / 8):
                if num_cards == 2:
                    if hand_value > b.value_of(['Jh', 'Jd']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['5h', '5d']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Ad']):
                        return call()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['8h', '8d', '8c']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['Qh', 'Qd']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Th', 'Td']):
                        return call()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Qh', 'Jd', 'Th', '9h', '8d']):
                        return raise_x_(4)
                    elif hand_value > b.value_of(['Jh', 'Jd', 'Th', 'Td']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['3h', '3d', '4c', '4c']):
                        return call()
                    else:
                        return fold()
            elif bet - my_bet > (self.chips / 16):
                if num_cards == 2:
                    if hand_value > b.value_of(['Jh', 'Jd']):
                        return raise_x_(4)
                    elif hand_value > b.value_of(['5h', '5d']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Ad']):
                        return call()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['Jh', 'Jd', 'Th', 'Td']):
                        return raise_x_(4)
                    elif hand_value > b.value_of(['Qh', 'Qd']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Th', 'Td']):
                        return call()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Qh', 'Jd', 'Th', '9h', '8d']):
                        return raise_x_(4)
                    elif hand_value > b.value_of(['Jh', 'Jd', 'Th', 'Td']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['3h', '3d', '4h', '4d']):
                        return call()
                    else:
                        return fold()
            else:
                if num_cards == 2:
                    if hand_value > b.value_of(['Jh', 'Jd']):
                        return raise_x_(5)
                    elif hand_value > b.value_of(['5h', '5d']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['Ad']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Qh']):
                        return call()
                    else:
                        return fold()
                elif num_cards == 5:
                    if hand_value > b.value_of(['Jh', 'Jd', 'Th', 'Td']):
                        return raise_x_(5)
                    elif hand_value > b.value_of(['Qh', 'Qd']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['Th', 'Td']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['5h', '5d']):
                        return call()
                    else:
                        return fold()
                else:
                    if hand_value > b.value_of(['Qh', 'Jd', 'Th', '9h', '8d']):
                        return raise_x_(5)
                    elif hand_value > b.value_of(['Jh', 'Jd', 'Th', 'Td']):
                        return raise_x_(3)
                    elif hand_value > b.value_of(['3h', '3d', '4h', '4d']):
                        return raise_x_(2)
                    elif hand_value > b.value_of(['Jh', 'Jd']):
                        return call()
                    else:
                        return fold()

    def bot_type(self):
        return "Bot4"
