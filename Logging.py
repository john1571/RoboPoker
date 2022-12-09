import os
from datetime import datetime
import globals
import Animate.animate as Animate
dt = datetime.now()
log_file = os.getcwd() + "\\Logs\\LogFile" + \
           dt.strftime('%Y-%m-%d_%H-%M-%S') + ".csv"

animation_log = ""


def log_chips(players, table, pot):
    if globals.ANIMATE:
        Animate.log_for_animation(players)
    if not os.path.exists(log_file) or os.stat(log_file).st_size == 0:
        with open(log_file, "w") as log:
            for player in players:
                log.write(player.name + ' - ' + player.type + ',')
            log.write(',pot,,flop 1,flop 2,flop 3,turn,river,,')
            for player in players:
                log.write(player.name + ' - ' + player.type + ',')
            log.write('\n')
    with open(log_file, "a") as log:
        for player in players:
            log.write(str(player.chips) + ',')
        log.write(',' + str(pot) + ',')
        if table:
            log.write(',' + table.show() + ',')
        for player in players:
            if player.busted:
                log.write("busted")
            elif player.folded:
                log.write("folded - ")
            if player.hand:
                log.write(player.hand.log())
            else:
                log.write(',')

        log.write('\n')
