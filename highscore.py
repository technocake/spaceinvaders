import turtle
highscorelist = {}


def playername():
    global highscorelist
    #får navn fra spiller og legger det til i highscore listen
    #returnerer spillernavn

    player =  turtle.textinput("player", "input your name")
    highscorelist[player] = 0
    return player

def starttid():
    #starter en timer
    pass

def stoptid():
    #stopper timeren
    pass

def lastinnhighscorefil(filnavn):
    #henter en fil med highscore
    pass

def lagretilhighscore(filnavn):
    #Lagrer highscoren i en fil
    pass



