from Bots import base_player
import Bots.Bot1
import Bots.Bot2
import Bots.Bot3
import Bots.JoanBot1


def register():
    return [
        base_player.Player,
        Bots.Bot1.Bot1,
        Bots.Bot2.Bot2,
        Bots.Bot3.Bot3,
        Bots.JoanBot1.JoanBot1,

    ]
