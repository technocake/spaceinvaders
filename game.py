import turtle
import threading
from time import sleep
from random import randrange
from math import radians, cos, sin

class Character(turtle.Turtle): #note capiptal letter in beginning of class name
    def __init__(self, space):
        turtle.Turtle.__init__(self)
        self.penup()
        self.space = space # contains 2 x,y coord defining world space/game board, similar to turtle.Vec2D
        pass

    def __repr__(self):
        return ""

    def canmove(self, x, y=None):
        "function checks if character is allowed to move within space, returns false if trying to move without of bounds (self.space)"
        # write function for checking if can move within space
        if y is None:
            dest = x
        else:
            dest = [x,y]
        return -1 * self.space[0] < dest[0] < self.space[0] and -1 * self.space[1] < dest[1] < self.space[1]

    def move(self, x, y=None):
        if y is None:
            dest = x
        else:
            dest = [x,y]
        if self.canmove(dest):
            self.goto(dest)
            return True
        else:
            return False

    def getxyfromfwd(self, dist=5):
        # calculate coordinates from distance given setheading
        pos = self.pos()
        ang = self.heading()
        rad = radians(ang)
        dest = [pos[0] + cos(rad) * dist, pos[1] + sin(rad) * dist]
        return dest

class PC(Character):
    def __init__(self, helse, space, shape="playership.gif"):
        Character.__init__(self, space)
        self.hitpoints = helse
        self.shape(shape)
    def mistliv(self):
        self.hitpoints -= 1

class NPC(Character):


    def movement(self):
        delay_ms = self.fart / 1000
        while True:
            sleep(delay_ms)
            dest = self.getxyfromfwd(self.distprmove)
            if self.canmove(dest):
                self.goto(dest)
            else:
                self.setheading(randrange(360))

    def collisionwith(self, x, y=None):
        if y is None:
            collider = x
        else:
            collider = [x,y]
        sx = self.pos()[0] # self pos x
        sy = self.pos()[1] # self pos y
        cx = collider[0] # collider x
        cy = collider[1] # collider y

        return (cx - sx)**2 + (cy - sy)**2 < self.radius**2


    def __init__(self, space, radius, fart=20, dist=5):
        super(NPC, self).__init__(space) # another way of Character.__init__(self)
        turtle.tracer(50)
        self.shape("Alienship.gif")
        self.distprmove = dist
        self.space = space
        self.radius = radius
        self.fart = fart
        self.setheading(randrange(360))
        self.t = threading.Thread(target=self.movement)
        self.t.daemon = True
        self.t.start()
        turtle.tracer(1)

