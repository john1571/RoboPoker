import globals as g


class Table:
    def __init__(self, deck):
        self.deck = deck
        self.cards_on_table = []

    def flip(self, num, players):
        self.deck.pop(0)
        for i in range(0, num):
            new_card = self.deck.pop(0)
            self.cards_on_table.append(new_card)
            for player in players:
                player.add_card(new_card, self)

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

    def to_string(self):
        json_data = []
        for card in self.cards_on_table:
            json_data.append(card.to_json_string())
        return json_data

    def deal(self, players):
        for i in range(0, 2):
            for player in players:
                player.add_card(self.deck.pop(0))

    def next_card(self, action, players):
        if action == g.DEAL:
            self.deal(players)
        else:
            self.flip(action, players)

