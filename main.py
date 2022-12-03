# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import Bots.Register as Register
import Dealer.Parse_Config as Dealer_Config
import pack
import Logging
import game_play as gp
import globals
import Console_Interface as CI
import table as t
import Animate.animate as ani


names = ['Adam', 'Ben', 'Caleb', 'Dan', 'Eli', 'Frank', 'Gad', 'Huz', 'Isaiah', 'John']


def init_players(num=5, chips=1000):
    all_players = []
    for j in range(0, num):
        i = random.randint(0, len(Register.register()) - 1)
        new_player = Register.register()[i](names[j], chips)
        for player in all_players:
            if not player:
                break
            while player.bot_type() == new_player.bot_type():
                if i == len(Register.register()) - 1:
                    i = 0
                else:
                    i += 1
                new_player = Register.register()[i](names[j], chips)
        all_players.append(new_player)
    return all_players


def blinds(round_num, live_players, dealer_num, big_blind, _Table):
    little_blind = round(big_blind/2)
    on_index = dealer_num
    if dealer_num + 1 >= len(live_players):
        little_blind_player = live_players[0]
        big_blind_player = live_players[1]
        on_index = 2
    elif dealer_num + 2 >= len(live_players):
        big_blind_player = live_players[0]
        little_blind_player = live_players[dealer_num + 1]
        on_index = 1
    else:
        little_blind_player = live_players[dealer_num + 1]
        big_blind_player = live_players[dealer_num + 2]
        on_index = dealer_num + 3
    little_blind_player.outer_act(live_players, little_blind)
    CI.print_status(round_num, live_players, little_blind_player, _Table, "bet_pause")
    big_blind_player.outer_act(live_players, big_blind)
    CI.print_status(round_num, live_players, big_blind_player, _Table, "bet_pause")
    return on_index


def check_for_win(players):
    remaining = []
    for player in players:
        if player.folded or player.busted:
            continue
        else:
            remaining.append(player)
    if len(remaining) == 1:
        return remaining[0]
    else:
        return None


def done_betting(players):
    if check_for_win(players):
        return True
    bets = []
    for player in players:
        if player.folded or player.all_in or player.busted:
            continue
        bets.append(player.chips_in_round)
    if bets == []:
        debug = bets

    current_bet = max(bets)
    for player in players:
        if player.folded or player.all_in or player.busted:
            continue
        if not player.has_bet or current_bet > player.chips_in_round:
            return False
    return True


def bet(round_num, live_players, on_index, big_blind, _Table):
    num_players = len(live_players)
    if on_index >= num_players:
        on_index = num_players - on_index
    if big_blind is not None:
        if on_index == len(live_players) - 2:
            debug = True
        on_index = blinds(round_num, live_players, on_index, big_blind, _Table)
    while True:
        if done_betting(live_players):
            break
        debug_pot = gp.get_current_pot(live_players)
        debug_bet = gp.get_current_bet(live_players)
        if on_index >= num_players:
            on_index = num_players - on_index
        under_gun = live_players[on_index]
        on_index += 1
        if not under_gun.can_bet(live_players):
            debug_pot = gp.get_betting_round_pot(live_players)
            if done_betting(live_players):
                break
            continue
        if under_gun.outer_act(live_players) is None:
            under_gun.fold()
        CI.print_status(round_num, live_players, under_gun, _Table, "bet_pause")
        debug_pot = gp.get_current_pot(live_players)
        if done_betting(live_players):
            break

round_order = [globals.DEAL, globals.FLOP, globals.TURN, globals.RIVER]


def deal_round(round_num, dealer_num, all_players, big_blind):
    _Table = t.Table(pack.get_deck())
    players = []
    for person in all_players:
        if not person.busted:
            person.new_hand()
            players.append(person)
    if round_num > 0 and round_num % 25 == 0:
        big_blind *= 2

    for action in round_order:
        blind = big_blind if action == globals.DEAL else None
        _Table.next_card(action, players)
        for player in players:
            player.new_betting_round()
        bet(round_num, players, dealer_num, blind, _Table)
        CI.print_status(round_num, all_players, None, _Table, "round_pause")
    log_pot = gp.get_current_pot(players)
    pot = gp.payout_new(players)
    Logging.log_chips(all_players, _Table, log_pot)
    CI.print_status(round_num, all_players, None, _Table, "win_pause")

    for player in players:
        player.new_hand()
    for person in all_players:
        person.update_stats()
    return pot, big_blind


def play(num_starting_players):
    all_players = init_players(num_starting_players)
    dealer_num = -1
    big_blind = 10
    if globals.ANIMATE:
        ani.start_log(all_players)
    for round_num in range(0, 1000):
        dealer_num += 1
        if round_num == 0:
            Logging.log_chips(all_players, None, 0)
        elif round_num % 25 == 0:
            big_blind *= 2
        deal_round(round_num, dealer_num, all_players, big_blind)
        ended = False
        num_busted = 0
        for player in all_players:
            if player.busted:
                num_busted += 1
                if num_busted == len(all_players) - 1:
                    ended = True
        if ended:
            break
        if dealer_num > len(all_players) - num_busted:
            dealer_num = -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play(5)
    print("LETS GO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
