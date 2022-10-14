import os
import matplotlib.animation as mpla
import matplotlib.pyplot as plt
import time
if "Animate" in os.getcwd():
    log_file = os.getcwd() + "\\Animated_Logs\\animation.txt"
else:
    log_file = os.getcwd() + "\\Animate\\Animated_Logs\\animation.txt"
plots = {}


def start_log(players):
    with open(log_file, "w") as log:
        for player in players:
            log.write(player.name + ' - ' + player.type + ',')
        log.write("\n")

def Log_for_animation(players):
    with open(log_file, "a") as log:
        for player in players:
            log.write(str(player.chips) + ',')
        log.write("\n")

def IsInt(character):
    try:
        i = int(character)
        return True
    except:
        return False
fig, ax = plt.subplots()
def _plot(i):
    print(os.getcwd())
    if not os.path.exists(log_file):
        return False
    j = 0
    with open(log_file, "r") as log:
        name_line = log.readline()
        names = name_line.split(",")
        names.pop()
        for name in names:
            plots[name] = []
        line = log.readline()
        while line:
            values = line.split(",")
            i = 0
            for names in plots.keys():
                plots[names].append(int(values[i]))
                i += 1
            line = log.readline()
            j += 1

    y = []
    for i in range(0, j):
        y.append(i)

    sets = []
    ax.clear()
    for name, set in plots.items():
        sets.append(y)
        sets.append(set)
        ax.plot(y, set, label=name)
    ax.legend(bbox_to_anchor=(0, 1, 1, .1), ncol=2, mode="expand", loc="lower left")
    fig.savefig("figure.pdf")




def animate():
    anim =  mpla.FuncAnimation(fig, _plot, interval=500)
    fig.show()
    plt.show()

if __name__ == '__main__':
    animate()
