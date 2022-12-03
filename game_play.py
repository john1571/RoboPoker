import globals


def get_current_bet(players):
    current_bet = 0
    for player in players:
        if player.folded or player.all_in or player.busted:
            continue
        if player.chips_in_round > current_bet:
            current_bet = player.chips_in_round
    return current_bet


def get_current_pot(players):
    pot = 0
    for player in players:
        pot += player.chips_in_pot
    return pot


def get_betting_round_pot(players):
    pot = 0
    for player in players:
        pot += player.chips_in_round
    return pot


def get_winners(players, rewarded_players):
    best_hand_value = [0]
    winners = []
    for player in players:
        if player in rewarded_players:
            continue
        if player.folded:
            continue
        if player.hand.get_value() > best_hand_value:
            winners = [player]
            best_hand_value = player.hand.get_value()
        elif player.hand.get_value() == best_hand_value:
            winners.append(player)
    return winners


def check_side_pot(players, winner_chips_in_pot):
    side_pot = 0
    for player in players:
        if player.chips_in_pot > winner_chips_in_pot:
            side_pot += winner_chips_in_pot
        else:
            side_pot += player.chips_in_pot
    return side_pot


def get_lowest_winner(players, winners):
    side_pots = {}
    for winner in winners:
        side_pots[check_side_pot(players, winner.chips_in_pot)] = winner
    if len(side_pots) == 1:
        return None
    if min(side_pots.keys()) == max(side_pots.keys()) and min(side_pots.keys()) == get_current_pot(players):
        return None
    return side_pots[min(side_pots.keys())]


def distribute_pot(pot, winners):
    won = round(pot / len(winners))
    for winner in winners:
        winner.chips += won
        pot -= won

    while pot > 1:
        for winner in winners:
            winner.chips += 1
            pot -= 1
            if pot == 0:
                break
    return


def reduce_chips_in_pot(players, amount):
    for player in players:
        if player.chips_in_pot > amount:
            player.chips_in_pot -= amount
        else:
            player.chips_in_pot = 0


def payout_new(players):
    rewarded_players = []
    while get_current_pot(players) > 0:
        winners = get_winners(players, rewarded_players)
        lowest_winner = get_lowest_winner(players, winners)
        while lowest_winner:
            side_pot = check_side_pot(players, lowest_winner.chips_in_pot)
            distribute_pot(side_pot, winners)
            reduce_chips_in_pot(players, lowest_winner.chips_in_pot)
            winners.remove(lowest_winner)
            rewarded_players.append(lowest_winner)
            lowest_winner = get_lowest_winner(players, winners)
        else:
            if len(winners) > 0:
                side_pot = check_side_pot(players, winners[0].chips_in_pot)
                distribute_pot(side_pot, winners)
                reduce_chips_in_pot(players, winners[0].chips_in_pot)
        for winner in winners:
            rewarded_players.append(winner)

        # validation
        num_players = 1
        for player in players:
            if player.folded or player.busted:
                continue
            num_players += 1
        if len(rewarded_players) > num_players:
            print("rewarded players: ")
            print(rewarded_players)
            print("num_players")
            print(num_players)
            assert False
