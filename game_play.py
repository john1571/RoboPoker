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
        pot += player.chips_in_round
    return pot


def get_winners(players, rewarded_players, table):
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


def payout_internal(pot, side_pots, players, winners, rewarded):
    num_split = len(winners)
    for player in players:
        if player in winners:
            if player.name in side_pots.keys():
                if globals.USER_PLAYING:
                    print(player.name + " wins " + str(side_pots[player.name] / num_split))
                player.chips = round(side_pots[player.name] / num_split)
                num_split -= 1
                pot -= side_pots[player.name]
                rewarded.append(player)
    for player in winners:
        if player not in rewarded:
            reward = round(pot / num_split)
            if globals.USER_PLAYING:
                print(player.name + " wins " + str(reward))
            player.chips += reward
            pot -= reward
    return pot, rewarded


def payout(pot, side_pots, players, table):
    starting_total = 0
    for player in players:
        starting_total += player.chips
    starting_total += pot
    if globals.USER_PLAYING:
        print("final pot: " + str(pot))
    loc_players = players
    rewarded_players = []
    count = 0
    while pot > 1:
        count += 1
        winners = get_winners(loc_players, rewarded_players, table)
        pot, rewarded_players = payout_internal(pot, side_pots, loc_players, winners, rewarded_players)
        if count > 20:
            break
    end_total = 0
    for player in players:
        end_total += player.chips
    if end_total != starting_total:
        if starting_total + 3 <= end_total <= starting_total - 3:  # allow for rounding error
            print(end_total - starting_total)
    return pot
