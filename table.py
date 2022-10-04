import random
import Bots.Register as Register
import globals as g


class Table:
    def __init__(self, deck):
        self.deck = deck
        self.cards_on_table = []

    def flip(self, num):
        burned = self.deck.pop(0)
        for i in range(0,num):
            self.cards_on_table.append(self.deck.pop(0))

    def show_with_color(self):
        show_string = ""
        for card in self.cards_on_table:
            show_string += card.get_with_color() + ' '
        return show_string

    def show(self):
        show_string = ""
        for card in self.cards_on_table:
            show_string += card.log_string() + ','
        return show_string

    def deal(self, players):
        for i in range(0, 2):
            for player in players:
                player.add_card(self.deck.pop(0))

    def next_card(self, action, players):
        if action == g.DEAL:
            self.deal(players)
        else:
            self.flip(action)



