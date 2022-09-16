import globals

def get_winners(players, rewarded_players, table):
    best_hand_value = 0
    winners = []
    for player in players:
        if player in rewarded_players:
            continue
        if player.folded:
            continue
        if player.hand.get_value(table) > best_hand_value:
            winners = []
            winners.append(player)
            best_hand_value = player.hand.get_value(table)
        elif player.hand.get_value(table) == best_hand_value:
            winners.append(player)
    return winners


def payout_internal(pot, side_pots, players, winners):
    num_split = len(winners)
    for player in players:
        if player in winners:
            if player.name in side_pots.keys():
                if globals.g_user_playing:
                    print(player.name + " wins " + str(side_pots[player.name] / num_split))
                player.chips = side_pots[player.name] / num_split
                num_split -= 1
                pot -= side_pots[player.name]
                winners.remove(player)
    for player in players:
        if player in winners:

            reward = pot / num_split
            if globals.g_user_playing:
                print(player.name + " wins " + str(reward))
            player.chips += reward
            pot -= reward
    return pot


def payout(pot, side_pots, players, table):
    if globals.g_user_playing:
        print("final pot: " + str(pot))
    loc_players = players
    rewarded_players = []
    while pot > 1 and len(loc_players) > 0:
        winners = get_winners(loc_players, rewarded_players, table)
        pot = payout_internal(pot, side_pots, loc_players, winners)
        for rewarded in winners:
            rewarded_players.append(rewarded)
        if len(rewarded_players) == len(players):
            return
            # TODO





