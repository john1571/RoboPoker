from Bots import base_player
import Bots.Bot1
import Bots.Bot2
import Bots.Bot3
import Bots.JoanBot1
import Bots.JPBot4
import Bots.Calling_Station
import Bots.RatioBot
import Bots.JPBot4_2
import Bots.JPBot4_3
import Bots.JPBot5
import Bots.JPBot5_2
import Bots.JPBot5_3


def register():
    return [
        base_player.Player,
        Bots.Bot1.Bot1,
        Bots.Bot2.Bot2,
        Bots.Bot3.Bot3,
        Bots.JoanBot1.JoanBot1,
        Bots.JPBot4.Bot4,
        Bots.Calling_Station.CallingStation,
        Bots.RatioBot.Ratio,
        Bots.JPBot4_2.Bot4_2,
        Bots.JPBot4_3.Bot4_3,
        Bots.JPBot5.JPBot5,
        Bots.JPBot5_2.JPBot5_2,
        Bots.JPBot5_3.JPBot5_3,
    ]


def required():
    return [
        # these bots will automatically be added to game
    ]
