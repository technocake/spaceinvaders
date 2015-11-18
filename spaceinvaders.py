import turtle
import game

import configparser
import sys
import threading
import time
from random import randrange

def loadkeystoturtle():
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
                    # try:
                    turtle.onkeypress(func, key)
                    # except:
                    #     print('binding', func, 'to', key, 'failed')
                    #     pass

step = 5

def forward():
    player.move(player.getxyfromfwd(step))

def turnleft():
    player.left(step)

def turnright():
    player.right(step)

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
    t.daemon = True


    space = turtle.screensize()
    npcradius = 20
    npcs = []
    turtle.register_shape("Alienship.gif", shape = None)
    turtle.register_shape("playership.gif", shape = None)
    for i in range(0, 5):
        npcs.append(game.NPC(space, npcradius, 20, 5))

    playercount = 1
    players = []
    for i in range(0, playercount):
        players.append(game.PC(3, space))
    player = players[0]
    player.goto(200,200)
    loadkeystoturtle()

    turtle.listen()

    t.start()
    ##############################################
    #  Spillet kjører
    ##############################################
    #La spiller skrive inn navn
    # Starte timer



    turtle.mainloop()


