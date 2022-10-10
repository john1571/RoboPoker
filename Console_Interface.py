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



def print_status(players, bets, current_actor, pot, table, user, sleep=0):
    if globals.g_watch:
        if (current_actor):
            print("Round:\t" + str(current_actor.stats.rounds))
        line_1 = "Table:\t" + table.show()
        name_line = "Names:\t\t"
        bot_type_line = "Bots:\t\t"
        player_chips = "Chips:\t\t"
        player_hands = "Hands:\t\t"
        hands_string = "Values:\t\t"
        bets_string =  "Bets:\t\t"
        last_round = "Last:\t\t"
        average_win =  "Av. W.:\t\t"
        average_loss = "Av. L.:\t\t"
        average_delta = "Av. D.:\t\t"
        percent_won = "Win %: \t\t"
        local_sleep = sleep
        for player in players:
            if player.busted:
                continue
            if player == current_actor:
                player_chips += ">"
                if player.busted or player.folded:
                    local_sleep = 0
            name_line += player.name[:4] + ": \t\t"
            bot_type_line += player.bot_type()[:4] + "\t\t"
            chips_string = ""
            if player.busted:
                chips_string = " OUT"
            else:
                chips_string = pad_num_to_string(player.chips, 4, 2)
            player_chips += chips_string
            if player.hand:
                player_hands += player.hand.show_for_print() + "\t\t"
                hands_string += player.hand.get_hand_string(table)[:4] + "\t\t"
            else:
                player_hands += "\t\t\t"
            if player.folded:
                bets_string += " fold" + "\t\t"
            elif player.busted:
                bets_string += "   out" + "\t\t"
            else:
                bet_string = pad_num_to_string(bets[player.name], 4, 2)
                bets_string += bet_string
            win_average = pad_num_to_string(player.stats.av_win(), 4, 2)
            average_win += win_average
            loss_average = pad_num_to_string(player.stats.av_loss(), 4, 2)
            average_loss += loss_average
            win_percent = pad_num_to_string(player.stats.percent_won(), 3, 2, '%')
            percent_won += win_percent
            last_delta = pad_num_to_string(player.stats.last_delta, 4, 2)
            last_round += last_delta
            av_delta = pad_num_to_string(player.stats.av_delta(), 4 ,2)
            average_delta += av_delta
        print("\n\n\n\n\n")
        if (current_actor):
            print("Round: " + str(current_actor.stats.rounds))
        else:
            print("")
        print("Pot: " + str(pot) + "\tTable: ", end="")
        print(table.show_with_color())
        print(name_line)
        print(bot_type_line)
        print(player_chips)
        print(player_hands)
        print(hands_string)
        print(bets_string)
        print("\nStats:")
        print(name_line)
        print(last_round)
        print(average_delta)
        print(average_win)
        print(average_loss)
        print(percent_won)

        time.sleep(local_sleep)
