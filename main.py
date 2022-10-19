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

def blinds(live_players, dealer, big_blind):
    little_blind = round(big_blind/2)
    button = live_players.get_at(dealer)
    if button + 1 > len(live_players):
        little_blind_player = live_players[0]
        big_blind_player = live_players[1]
    elif button + 2 > len(live_players):
        little_blind_player = live_players[button + 1]
        big_blind_player = live_players[0]
    else:
        little_blind_player = live_players[button + 1]
        big_blind_player = live_players[button + 2]
    little_blind_player.blind(little_blind)
    big_blind_player.blind(big_blind)


def done_betting(players):
    current_bet = 0
    for player in players:
        if player.folded or player.all_in or player.busted:
            continue
        if current_bet > player.chips_in_round:
            return False
        else:
            current_bet = player.chips_in_round
    return True


def bet(live_players, on_index):
    while not done_betting(live_players):
        under_gun = live_players[on_index]
        for player in live_players:
            if player is under_gun:
                on_index += 1
                if on_index > len(live_players) - 1:
                    on_index = 0
                under_gun = live_players[on_index]
                if not player.can_bet(live_players):
                    continue
                if player.outer_act(live_players) is None:
                    player.fold()


round_order = [globals.FLOP, globals.TURN, globals.RIVER]


def deal_round(round_num, dealer_num, all_players):
    _Table = t.Table(pack.get_deck())
    side_pots = {}
    players = []
    for person in all_players:
        if not person.busted:
            person.new_hand()
            players.append(person)
    _Table.deal(players)
    if round_num > 0 and round_num % 25 == 0:
        little_blind *= 2
        big_blind *= 2
    for action in round_order:
        bet(players, dealer_num)
        _Table.next_card(action, players)
    payout = gp.get_current_pot(players)
    pot = gp.payout(payout, side_pots, players, _Table)
    Logging.log_chips(all_players, _Table, pot)

    for player in players:
        player.new_hand()
    for person in all_players:
        person.update_stats()
    return pot, little_blind, big_blind


def play(num_starting_players):
    all_players = init_players(num_starting_players)
    dealer_num = -1
    little_blind = 5
    big_blind = 10
    pot = 0
    if globals.ANIMATE:
        ani.start_log(all_players)
    for round_num in range(0, 1000):
        dealer_num += 1
        if round_num == 0:
            Logging.log_chips(all_players, None, 0)
        deal_round(round_num, dealer_num, all_players)
        ended = False
        num_busted = 0
        for player in all_players:
            if player.busted:
                num_busted += 1
                if num_busted == len(all_players) - 1:
                    ended = True
        if ended:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play(5)
    print("LETS GO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
