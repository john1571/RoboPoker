from Bots import base_player
import Bots.Bot1
import Bots.Bot2
import Bots.Bot3
import Bots.JoanBot1
import Bots.JPBot4
import Bots.Calling_Station
import Bots.RatioBot
import Bots.JPBot4_2

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
    ]
