

layout = '''
All_Actions = {
1: {
    deal_bets : {
        1: { player: bet, player: bet, player: bet}  # each round of betting is its own dictionary
        2: { player: bet, player: bet, player: bet}
    flop_bets :
    turn_bets :
    river_bets :
    showdwon : [player, player]
    winner : player
},
2: {},
3: {},
4: {},
5: {},
}
'''

round_dictionary = {
    "deal_bets": {},
    "flop_bets": {},
    "turn_bets": {},
    "river_bets": {},
    "showdown": [],
    "winner": ""
}

