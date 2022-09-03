# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pack
import hand_helpers as Hands
import Logging

class Table:
    def __init__(self, deck):
        self.deck = deck
        self.burned = []
        self.flop1 = None
        self.flop2 = None
        self.flop3 = None
        self.turn = None
        self.river = None

    def _turn(self):
        print("\nTURN:", end="\t")
        self.burned = self.deck.pop(0)
        self.turn = self.deck.pop(0)
        self.flop1.print_with_color()
        self.flop2.print_with_color()
        self.flop3.print_with_color()
        self.turn.print_with_color()
        print("******")

    def flop(self):
        print("\nFLOP:", end="\t")
        self.burned = self.deck.pop(0)
        self.flop1 = self.deck.pop(0)
        self.flop2 = self.deck.pop(0)
        self.flop3 = self.deck.pop(0)
        self.flop1.print_with_color()
        self.flop2.print_with_color()
        self.flop3.print_with_color()
        print("******")

    def _river(self):
        print("\nRIVER:", end="\t")
        self.burned = self.deck.pop(0)
        self.river = self.deck.pop(0)
        self.flop1.print_with_color()
        self.flop2.print_with_color()
        self.flop3.print_with_color()
        self.turn.print_with_color()
        self.river.print_with_color()
        print("******")




names = ['Adam', 'Ben', 'Caleb', 'Dan', 'Eli', 'Frank', 'Gad', 'Huz', 'Isiah', 'John']

def deal(players, table):
    deck = pack.getDeck()
    print(deck.pop(0))
    hands = []
    for i in range(0, 2):
        for player in players:
            player.add_card(deck.pop(0))

    for hand in hands:
        hand.show(table)

def flop(table, hands):
    table.flop()
    for hand in hands:
        hand.show(table)

def turn(table, hands):
    table._turn()
    for hand in hands:
        hand.show(table)

def river(table, hands):
    table._river()
    for hand in hands:
        hand.show(table)

def end(players):
    Table(pack.getDeck())
    for player in players:
        player.reset()

#def betting():
    # later

class Actions:
    fold = 0
    call = 1
    bet = 2
    check = 3
    allin = 4

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = Hands.Hand(self.name)
        self.folded = False

    def fold(self):
        self.folded = True
        return 0

    def bet(self, amount):
        self.chips -= amount
        return amount

    def add_card(self, card, table=None):
        self.hand.add_card(card, table)

    def status(self, table):
        self.hand.show(table)
        print(self.chips)

    def act(self, bet):  # actions = dictionary: name:(action, amount)
        if self.folded or bet > 5:
            return Actions.fold, self.fold()
        return Actions.bet, self.bet(5)

    def reset(self):
        self.hand = Hands.Hand(self.name)


def betting(players):
    pot = 0
    bet = 0
    for player in players:
        if player.folded == True:
            continue
        action, bet = player.act(bet)
        pot += bet
    return pot


def play(num_starting_players):
    players = []
    for player in range(0, num_starting_players):
        players.append(Player(names[player], 1000))


    for round in range(0, 100):
        table = Table(pack.getDeck())
        deal(players, table)
        hands = []
        pot = 0
        for player in players:
            hands.append(player.hand)
        pot += betting(players)
        flop(table, hands)
        pot += betting(players)
        turn(table, hands)
        pot += betting(players)
        river(table, hands)
        pot += betting(players)
        best_hand_value = 0
        winners = []
        for hand in hands:
            if hand.get_value(table) > best_hand_value:
                winners = []
                winners.append(hand.name)
                best_hand_value = hand.get_value(table)
            elif hand.get_value(table) == best_hand_value:
                winners.append(hand.name)

        num_split = len(winners)
        for player in players:
            if player.name in winners:
                player.chips += (pot/num_split)
            player.status(table)
        end(players)
        Logging.Log_chips(players)

def print_hi(name):
    play(5)
    # Use a breakpoint in the code line below to debug your script.
    print("LETS GO")  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
