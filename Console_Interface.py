import os
divideder = "\n**********\n"
showdown = False
user_bets_status = []  # User name, bet
current_actor = ""
pot = 0
table = ""
user_turn = False

def print_status(players, bets, current_actor, pot, table, user, prompt):
    interface = ""
    interface += divideder
    interface += "Table:\t" + table.show() + "\n"
    interface += "Pot:\t$" + str(pot) + "\n"
    interface += divideder

    betting_string = "Bets:\n"
    for player in players:
        for name, bet in bets.items():
            if player.name == name:
                player_string = "\t" + name + "\t$" + str(bet) + "\t"
                if player.busted:
                    player_string += 'Busted'
                elif player.folded:
                    player_string += 'Folded'
                elif name == current_actor:
                    player_string += '<-ACTION'
                betting_string += player_string + '\n'

    interface += betting_string
    interface += divideder
    if user:
        interface += user.name + "'s cards:\t" + user.show_hand(table) + '\n'
        interface += user.name + "'s chips:\t$" + str(user.chips)
    interface += divideder
    os.system('cls')
    print(interface)
    if prompt:
        return input(prompt)
