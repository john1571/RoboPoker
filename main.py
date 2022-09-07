# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

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

    def show(self):
        show_string = ""
        if (self.flop1):
            show_string += self.flop1.log_string() + ','
        if (self.flop2):
            show_string += self.flop2.log_string() + ','
        if (self.flop3):
            show_string += self.flop3.log_string() + ','
        if (self.turn):
            show_string += self.turn.log_string() + ','
        if (self.river):
            show_string += self.river.log_string() + ','
        return show_string


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

    def act(self, bet, my_bet):  # actions = dictionary: name:(action, amount)
        if bet > 0:
            if self.folded:
                return Actions.fold, self.fold()
            if my_bet != 0 and bet > my_bet * 5:
                return Actions.fold, self.fold()
            if random.randint(0, 10) == 8:
                my_bet = (bet * 2) - my_bet
                return Actions.bet, self.bet(my_bet)
            return Actions.bet, self.bet(bet - my_bet)
        else:
            if random.randint(0, 10) > 5:
                my_bet = 5
            else:
                my_bet = 0
            return Actions.bet, self.bet(my_bet)

    def reset(self):
        self.hand = Hands.Hand(self.name)


def betting(players):
    pot = 0
    current_bet = 0
    bet = 0
    bets = {} # player, bet
    for player in players:
        bets[player.name] = 0
    Betting_done = False
    while not Betting_done:
        for player in players:
            if player.folded:
                continue
            if current_bet > 0 and bets[player.name] == current_bet:
                continue
            action, bet = player.act(current_bet, bets[player.name])
            pot += bet
            bets[player.name] += bet
            if bets[player.name] < current_bet:
                player.folded = True
                bets.__delitem__(player.name)
                continue
            elif bets[player.name] >= current_bet * 2:
                current_bet = bets[player.name]
        Betting_done = True
        for bet in bets.values():
            if bet < current_bet:
                Betting_done = False
                break
    print("pot: " + str(pot))
    return pot


def play(num_starting_players):
    players = []
    for player in range(0, num_starting_players):
        players.append(Player(names[player], 1000))

    for round in range(0, 1000):
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
        Logging.Log_chips(players, table)
        end(players)
        ended = False
        for player in players:
            if player.chips < 0:
                ended = True
        if ended:
            break

def print_hi(name):
    play(5)
    # Use a breakpoint in the code line below to debug your script.
    print("LETS GO")  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
