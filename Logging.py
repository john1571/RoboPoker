import os
log_file = "C:\\Users\\johnpaul.jones\\PycharmProjects\\PokerInterface3\\LogFile.txt"

def Log_chips(players, table):
    if not os.path.exists(log_file) or os.stat(log_file).st_size == 0:
        with open(log_file, "w") as log:
            for player in players:
                log.write(player.name + ',')
            log.write('\n')
    with open(log_file, "a") as log:
        for player in players:
            log.write(str(player.chips) + ',')
        if table:
            log.write(',' + table.show() + ',')
        for player in players:
            if player.hand:
                log.write(player.hand.log())
        log.write('\n')
