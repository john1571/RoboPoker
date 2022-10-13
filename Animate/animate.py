import os
import matplotlib as mpl
import matplotlib.pyplot as plt

log_file = os.getcwd() + "\\Animated_Logs\\animation.txt"
plots = {}
def Log_for_animation(players):
    if not os.path.exists(log_file) or os.stat(log_file).st_size == 0:
        with open(log_file, "w") as log:
            for player in players:
                log.write(player.name + ' - ' + player.type + ',')
                plots[player.name] = []
        with open(log_file, "a") as log:
            for player in players:
                log.write(str(player.chips) + ',')

def IsInt(character):
    try:
        i = int(character)
        return True
    except:
        return False

def plot():
    print(os.getcwd())
    if not os.path.exists(log_file):
        return False
    print("there")
    if not plots:
        plots["player1"] = []
        plots["player2"] = []
    j = 0
    with open(log_file, "r") as log:
        name_line = log.readline()
        line = log.readline()
        while line:
            values = line.split(",")
            i = 0
            for names in plots.keys():
                plots[names].append(values[i])
                i += 1
            line = log.readline()
            j += 1

    y = []

    print("here")
    for i in range(0, j):
        y.append(i)

    print(y)
    print(plots)
    for name, set in plots.items():
        print(name)
        print(set)
        plt.plot(y, set)
    plt.show()


if __name__ == '__main__':
    print("hi")
    plot()