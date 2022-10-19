import time
import globals
import Dealer.Parse_Config as Dealer_config
divideder = "\n**********\n"
showdown = False
user_bets_status = []  # User name, bet
current_actor = ""
pot = 0
table = ""
user_turn = False

column_width = 8
column_tabs = 2


def pad_num_to_string(number, string_length=column_width, num_tabs=column_tabs, prefix=''):
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
        if i == num_tabs - 2:
            tabs += "|"
    return padded_string + prefix + str(number) + tabs


def pad_string(string, string_length=column_width, num_tabs=column_tabs):
    tabs = ""
    for i in range(0, num_tabs):
        tabs += '\t'
        if i == num_tabs - 2:
            tabs += "|"

    if string_length < 0:
        return "" + tabs
    if len(string) > string_length:
        string = string[:string_length]
    else:
        while len(string) < string_length:
            string = string + " "
    return string + tabs


def print_status(round_num, players, bets, current_actor, pot, table, sleep=0):
    if int(Dealer_config.parse("skip_to_round", 0)) > round_num:
        sleep = 0
    stats_only = False
    if not bets or not table:
        stats_only = True
    if globals.WATCH:
        name_line = pad_string("Names:")
        bot_type_line = pad_string("Bots:")
        player_chips = pad_string("Chips:")
        average_win = pad_string("Av. W.:")
        average_loss = pad_string("Av. L.:")
        average_delta = pad_string("Av. D.:")
        percent_won = pad_string("Win %:")
        local_sleep = sleep
        player_hands = ""
        hands_string = ""
        bets_string = ""
        last_round = ""
        if not stats_only:
            line_1 = "Table:\t" + table.show()
            player_hands = pad_string("Hands:")
            hands_string = pad_string("Values:")
            bets_string =  pad_string("Bets:")
            last_round = pad_string("Last:")

        for player in players:
            if player == current_actor:
                name_line += ">"
                name_line += pad_string(player.name, column_width - 1)
                if player.busted or player.folded:
                    local_sleep = 0
            else:
                name_line += pad_string(player.name)
            bot_type_line += pad_string(player.bot_type())

            chips_string = ""
            if player.busted:
                chips_string = pad_string("--")
            else:
                chips_string = pad_num_to_string(player.chips)
            player_chips += chips_string
            if not stats_only:
                if player.busted:
                    player_hands += pad_string("")
                    hands_string += pad_string("")
                    bets_string += pad_string("")
                    last_round += pad_string("")
                else:
                    last_delta = pad_num_to_string(player.stats.last_delta)
                    last_round += last_delta
                    if player.hand:
                        if player.folded:
                            player_hands += pad_string("--")
                            hands_string += pad_string("--")
                        else:
                            player_hands += player.hand.show_for_print() + pad_string("", column_width - 5)
                            hands_string += pad_string(player.hand.get_hand_string(table))
                    else:
                        player_hands += pad_string("")
                    if player.folded:
                        bets_string += pad_string("fold")
                    elif player.busted:
                        bets_string += pad_string("--")
                    else:
                        bets_string += pad_num_to_string(bets[player.name])

            win_average = pad_num_to_string(player.stats.av_win())
            average_win += win_average
            loss_average = pad_num_to_string(player.stats.av_loss())
            average_loss += loss_average
            win_percent = pad_num_to_string(player.stats.percent_won(), column_width - 1, column_tabs, '%')
            percent_won += win_percent

            av_delta = pad_num_to_string(player.stats.av_delta())
            average_delta += av_delta
        print("\n\n\n\n\n")
        if (current_actor):
            print("Round: " + str(current_actor.stats.rounds))
        else:
            print("")
        if table:
            print("Pot: " + str(pot) + "\tTable: ", end="")
            print(table.show_with_color())
        print(name_line)
        print(bot_type_line)
        print(player_chips)
        if not stats_only:
            print(player_hands)
            print(hands_string)
            print(bets_string)
        print("\nStats:")
        print(name_line)
        if not stats_only:
            print(last_round)
        print(average_delta)
        print(average_win)
        print(average_loss)
        print(percent_won)

        time.sleep(local_sleep)
