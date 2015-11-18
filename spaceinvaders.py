import turtle
import game
import highscore

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
    print('thread started')
    while True:
        time.sleep(0.9)
        for npc in npcs:
            if npc.collisionwith(player.pos()):
                player.mistliv()
                print(player.hitpoints)
                if -1 < player.hitpoints < 1:
                    print('GAME OVER')
                    highscore.stoptid()

if __name__ == '__main__':
    ##############################################
    #   Forberedelsesfase
    ##############################################
    # Laste inn highscore hær.
    highscore.lastinnhighscorefil("highscoreliste.txt")
    #Gjøre det klart for at vi kan stoppe timer
    t = threading.Thread(target=mainthread)
    t.daemon = True

    space = turtle.screensize()
    npcradius = 100
    npcs = []
    turtle.register_shape("Alienship.gif", shape = None)
    turtle.register_shape("playership.gif", shape = None)

    loadkeystoturtle()
    ##############################################
    #  Spillet kjører
    ##############################################
    #La spiller skrive inn navn
    highscore.playername()
    # Starte timer
    highscore.starttid()

    for i in range(0, 5):
        npcs.append(game.NPC(space, npcradius, 20, 5))

    playercount = 1
    players = []
    for i in range(0, playercount):
        players.append(game.PC(3, space, "classic"))
    player = players[0]
    player.goto(200,200)

    t.start()

    turtle.listen()
    turtle.mainloop()


