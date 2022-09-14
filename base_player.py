import hand_helpers as hands

class Actions:
    fold = 0
    call = 1
    bet = 2
    check = 3
    allin = 4


class Player:
    def __init__(self, name, chips, id=None):
        self.name = name
        if id:
            self.id = id
        else:
            self.id = name
        self.chips = chips
        self.busted = False
        self.folded = False
        self.hand = hands.Hand(self.id)

    def new_hand(self):
        self.folded = False
        self.hand = hands.Hand(self.id)
        if self.chips < 0:
            self.bust()

    def bust(self):
        self.busted = True
        self.hand = None

    def fold(self):
        self.folded = True
        return None

    def bet(self, amount):
        self.chips -= amount
        return amount

    def act(self, bet, my_bet, table=None, actions=None):
        if bet - my_bet > 50:
            return None
        else:
            return self.bet(bet - my_bet)

    def outer_act(self, bet, my_bet, table=None, actions=None):
        new_bet = self.act(bet, my_bet, table, actions)
        if new_bet:
            self.chips -= new_bet
        return new_bet

    def add_card(self, card, table=None):
        self.hand.add_card(card, table)

    def status(self, table):
        self.hand.show(table)
        print(self.bot_type())
        print(self.chips)

    def bot_type(self):
        return "base_player"

