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
    best_hand_value = 0
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


def payout_internal(players, winners):
    num_split = len(winners)
    sorted_winners = sort_winners(winners)
    i = 0
    while i < len(sorted_winners):
        winner = sorted_winners[i]
        for player in players:
            if player is winner:
                continue
            if round(player.chips_in_pot/num_split) > winner.chips_in_pot:
                winner.chips += round(winner.chips_in_pot/num_split)
                player.chips_in_pot -= round(winner.chips_in_pot/num_split)
            else:
                winner.chips += round(player.chips_in_pot/num_split)
                player.chips_in_pot -= round(player.chips_in_pot/num_split)
        winner.chips += round(winner.chips_in_pot/num_split)
        winner.chips_in_pot -= round(winner.chips_in_pot/num_split)

        i += 1
        num_split -= 1
    rewarded = []
    for player in winners:
        rewarded.append(player.name)
    return rewarded


def payout(players):
    starting_total = 0
    for player in players:
        starting_total += player.chips
    starting_total += get_current_pot(players)
    loc_players = players
    rewarded_players = []
    count = 0
    while get_current_pot(players) > 1:
        count += 1
        winners = get_winners(loc_players, rewarded_players)
        payout_internal(players, winners)
        if count > 20:
            break
    end_total = 0
    for player in players:
        end_total += player.chips
    if end_total != starting_total:
        AssertionError("Chips discrepancy detected!")
        if starting_total + 3 <= end_total <= starting_total - 3:  # allow for rounding error
            print(end_total - starting_total)
    return get_current_pot(players)


def sort_winners(winners):
    huge = 100000
    dict = {}
    sorted_winners = []
    for player in winners:
        dict[player] = player.chips_in_pot
        if player.chips_in_pot > huge:
            huge = player.chips_in_pot * 2

    while len(sorted_winners) < len(winners):
        for player in winners:
            if player.chips_in_pot == min(dict.values()):
                sorted_winners.append(player)
                dict[player] = huge
    return sorted_winners





