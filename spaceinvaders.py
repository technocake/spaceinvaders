import turtle
import game

import configparser
import sys
import threading
import time
from random import randrange

def loadkeystoturtle(targetturtle):
    config = configparser.ConfigParser()
    config.optionxform=str  # preserve case
    config.read('config.ini')
    for section in config.sections():
        if section.lower() == 'keys':
            for key in config[section]:
                name = config['Keys'][key]
                obta = sys.modules[__name__]
                if hasattr(obta, name):
                    func = getattr(obta, name) # a function with no arguments or None
                    targetturtle.onkeypress(func, key)

def mainthread():
    while True:
        time.sleep(250)

if __name__ == '__main__':
    ##############################################
    #   Forberedelsesfase
    ##############################################
    # Laste inn highscore hær.
    #Gjøre det klart for at vi kan stoppe timer
    t = threading.Thread(target=mainthread)
    # t.daemon = True
    t.start()

    space = turtle.screensize()
    npcradius = 20
    npcs = []
    turtle.register_shape("Alienship.gif", shape = None)
    turtle.register_shape("playership.gif", shape = None)
    for i in range(0, 5):
        npcs.append(game.NPC(space, npcradius))

    ##############################################
    #  Spillet kjører
    ##############################################
    #La spiller skrive inn navn
    # Starte timer



    turtle.mainloop()
