import base_player
import Bots.Bot1
import Bots.Bot2


def register():
    return [
        base_player.Player,
        Bots.Bot1.Bot1,
        Bots.Bot2.Bot2,
    ]
