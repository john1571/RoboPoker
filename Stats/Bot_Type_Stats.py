import json
import os
import globals as g

"""
{
    games_played : 0,
    bots: [
        {
            bot_type: type,
            games_played: 0,
            games_won: 0,
      later:      average_rounds_lasted: 0,
     Later: opponents: [
                {
                    bot_type: 0,
                    games_played_against: 0,
                    outlasted: 0,
                    won: 0,
                }            
            ]
        }
    
    ]
}
"""

stat_file_name = os.getcwd() + "\\Stats\\Bot_Type_Stats.txt"
def log_stats(all_players):
    if not g.LONG_TERM_STATS:
        return
    stats_to_update = {}
    with open(stat_file_name, 'r') as stats_file:
        stats_to_update = json.load(stats_file)
    if stats_to_update.get('bots', None) is None:
        stats_to_update['bots'] = []
    stats_to_update['games_played'] = stats_to_update.get('games_played', 0) + 1
    for player in all_players:
        index = -1
        updated = False
        for bot_type in stats_to_update.get('bots', []):
            index += 1
            if player.bot_type() == bot_type.get('bot_type', None):
                stats_to_update['bots'][index] = update_bot_stat(player, bot_type)
                updated = True
        if not updated:
            stats_to_update['bots'].append(add_new_bot(player))
    with open(stat_file_name, 'w') as stats_file:
        json.dump(stats_to_update, stats_file)

def update_bot_stat(bot, bot_dict):
    bot_dict['games_played'] = bot_dict['games_played'] + 1
    if bot.chips > 0:
        bot_dict['games_won'] = bot_dict['games_won'] + 1
    return bot_dict

def add_new_bot(bot):
    return {
        'bot_type': bot.bot_type(),
        'games_played': 1,
        'games_won': 1 if bot.chips > 0 else 0,
    }