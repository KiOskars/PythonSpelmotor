from src.core import *

from src.game import *
from src.graphics import GraphicsEngine
from src.tools.Logging import Log


class Spelmotor(InitializerIf):
    def __init__(self):
        super(Spelmotor, self).__init__("Frogger Game Engine", "En spelmotor för att skapa spelet Frogger")

        self.__setattr__('GraphicsEngine', GraphicsEngine())

        turtleInit = Turtle()
        turtleInit.hideturtle()
        self.window = turtleInit.screen
        self.window.bgcolor("light green")

        self.window.listen()

    def play(self):
        player = Entity("Player", "turtle", 90, 10, 0, 0, "blue")
        player.defineKeys(self.window)

        enemy = Entity("Enemy", "arrow", 0, 10, -500, 0, "red")

        done()

        Log.out("Stänger ner applikationen och avslutar processen", "Ha en bra dag!")