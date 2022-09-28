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

def pad_num_to_string(number, string_length, num_tabs, prefix = ''):
    padded_string = ""
    spaces_needed = string_length
    temp = number/10
    if number < 0:
        spaces_needed -= 1
        while temp < -1:
            spaces_needed -= 1
            temp = temp/10
    else:
        while temp > 1:
            spaces_needed -= 1
            temp = temp/10
    while spaces_needed > 0:
        padded_string += " "
        spaces_needed -= 1
    tabs = ""
    for i in range(0, num_tabs):
        tabs += '\t'
    return padded_string + prefix + str(number) + tabs



def print_status(players, bets, current_actor, pot, table, user, prompt, sleep=0):
    if globals.g_watch:
        line_1 = "Table: " + table.show()
        name_line = "Names:  "
        player_chips = "Chips:  "
        player_hands = "Hands:  "
        bets_string =  "Bets:   "
        average_win =  "Av. W.:"
        average_loss = "Av. L.:"
        percent_won = "Win %: "
        local_sleep = sleep
        for player in players:
            if player.busted:
                continue
            if player == current_actor:
                player_chips += ">"
                if player.busted or player.folded:
                    local_sleep = 0
            name_line += player.name[:4] + ": \t\t"
            chips_string = ""
            if player.busted:
                chips_string = " OUT"
            else:
                chips_string = pad_num_to_string(player.chips, 5, 2)
            player_chips += chips_string
            if player.hand:
                player_hands += player.hand.show_for_print() + "\t\t"
            else:
                player_hands += "\t\t\t"
            if player.folded:
                bets_string += "fold" + "\t\t"
            elif player.busted:
                bets_string += " out" + "\t\t"
            else:
                bet_string = pad_num_to_string(bets[player.name], 5, 2)
                bets_string += bet_string
            win_average = pad_num_to_string(player.stats.av_win(), 5, 2)
            average_win += win_average
            loss_average = pad_num_to_string(player.stats.av_loss(), 5, 2)
            average_loss += loss_average
            win_percent = pad_num_to_string(player.stats.percent_won(), 4, 2, '%')
            percent_won += win_percent
        print("\n\n\n\n\n")
        print("Pot: " + str(pot) + "\tTable: ", end="")
        print(table.show_with_color())
        print(name_line)
        print(player_chips)
        print(player_hands)
        print(bets_string)
        print(prompt)
        print("Stats:")
        print(name_line)
        print(average_win)
        print(average_loss)
        print(percent_won)
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
