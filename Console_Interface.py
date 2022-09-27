import os
import time
import globals

divideder = "\n**********\n"
showdown = False
user_bets_status = []  # User name, bet
current_actor = ""
pot = 0
table = ""
user_turn = False


def print_status(players, bets, current_actor, pot, table, user, prompt, sleep=2):
    if globals.g_watch:
        line_1 = "Table: " + table.show()
        name_line = ""
        line_2 = ""
        line_3 = ""
        line_4 = ""
        local_sleep = sleep
        for player in players:
            if player == current_actor:
                line_2 += ">"
                if player.busted or player.folded:
                    local_sleep = 0
            name_line += player.name[:4] + ": \t\t"
            chips_string = ""
            if player.busted:
                chips_string = " OUT"
            else:
                if player.chips < 10:
                    chips_string = "   " + str(player.chips)
                elif player.chips < 100:
                    chips_string = "  " + str(player.chips)
                elif player.chips < 1000:
                    chips_string = " " + str(player.chips)
                else:
                    chips_string = str(player.chips)
            line_2 += chips_string + "\t\t"
            if player.hand:
                line_3 += player.hand.show_for_print() + "\t\t"
            else:
                line_3 += "\t\t\t"
            if player.folded:
                line_4 += "fold" + "\t\t"
            elif player.busted:
                line_4 += " out" + "\t\t"
            else:
                bet_string = ""
                player_bet = bets[player.name]
                if player_bet < 10:
                    bet_string = "   " + str(player_bet)
                elif player_bet < 100:
                    bet_string = "  " + str(player_bet)
                elif player_bet < 1000:
                    bet_string = " " + str(player_bet)
                else:
                    bet_string = str(player_bet)
                line_4 += bet_string + "\t\t"
        print("\n\n\n\n\n")
        print("Pot: " + str(pot) + "\tTable: ", end="")
        print(table.show_with_color())
        print(name_line)
        print(line_2)
        print(line_3)
        print(line_4)
        time.sleep(local_sleep)


    if not globals.g_user_playing:
        return ""

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
