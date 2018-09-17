from turtle import *

from src.core import InitializerIf

class Spelmotor(InitializerIf):
    def __init__(self):
        super(Spelmotor, self).__init__("Frogger Game Engine", "En spelmotor för att skapa spelet Frogger")

        turtleInit = Turtle()
        turtleInit.hideturtle()
        self.window = turtleInit.screen
        self.window.bgcolor("light green")

        self.window.listen()
