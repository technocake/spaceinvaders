import turtle
import time
highscorelist = {}
tidstart = 0
spiller = None

def playername():
    global highscorelist
    #får navn fra spiller og legger det til i highscore listen
    #returnerer spillernavn

    player =  turtle.textinput("player", "input your name")
    highscorelist[player] = 0
    #putter spiller in i player for å bruke den etterpå
    spiller = player
    return player

def starttid():
    global tidstart
    #starter en timer
    tidstart = time.time()

def stoptid():
    #stopper timeren
    global tidstart
    global highscorelist
    global spiller
    tidstop = time.time()
    score = tidstop - tidstart
    highscorelist[spiller] = score

def lastinnhighscorefil(filnavn):
    #henter en fil med highscore
    pass

def lagretilhighscore(filnavn):
    #Lagrer highscoren i en fil
    pass

def displayhighscore():
    #viser highscore på skjermen
    pass



