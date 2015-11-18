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

ctrl = 0
def setctrl1():
    global ctrl
    ctrl = 0
def setctrl2():
    global ctrl
    ctrl = 1
def setctrl3():
    global ctrl
    ctrl = 2
def setctrl4():
    global ctrl
    ctrl = 3
def setctrl5():
    global ctrl
    ctrl = 4

def gofwd():
    npcs[ctrl].forward(5)
def gorev():
    npcs[ctrl].backward(5)

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
    # for npc in npcs:
    #     npc.forward(200)

    turtle.onkeypress(setctrl1, '1')
    turtle.onkeypress(setctrl2, '2')
    turtle.onkeypress(setctrl3, '3')
    turtle.onkeypress(setctrl4, '4')
    turtle.onkeypress(setctrl5, '5')
    turtle.onkeypress(gofwd, 'Up')
    turtle.onkeypress(gorev, 'Down')

    turtle.listen()

    ##############################################
    #  Spillet kjører
    ##############################################
    #La spiller skrive inn navn
    # Starte timer



    turtle.mainloop()
