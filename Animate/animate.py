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


def log_for_animation(players):
    with open(log_file, "a") as log:
        for player in players:
            log.write(str(player.chips) + ',')
        log.write("\n")


def is_int(character):
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
        skipped = 0
        while line:
            values = line.split(",")
            i = 0

            for names in plots.keys():
                try:
                    k = int(values[i])
                except ValueError:
                    skipped += 1
                    continue
                plots[names].append(int(values[i]))
                i += 1
            line = log.readline()
            j += 1

    y = []
    j = j - skipped
    for i in range(0, j):
        y.append(i)

    sets = []
    ax.clear()
    try:
        for name, chips_array in plots.items():
            sets.append(y)
            sets.append(chips_array)
            ax.plot(y, chips_array, label=name)
        ax.legend(bbox_to_anchor=(0, 1, 1, .1), ncol=2, mode="expand", loc="lower left")
        fig.savefig("figure.pdf")
    except ValueError:
        pass

def animate():
    anim = mpla.FuncAnimation(fig, _plot, interval=500)
    fig.show()
    plt.show()
    return anim


if __name__ == '__main__':
    anim = None
    while True:
        try:
            anim = animate()
        except Exception:
            time.sleep(5)
            pass
