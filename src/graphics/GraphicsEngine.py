from src.core import *


class GraphicsEngine(SubsystemIf):
    def __init__(self):
        super(GraphicsEngine, self).__init__("Grafikmotor", "Ett subsystem som tillhandahåller vad som visas på skärmen")

    def initialize(self):
        super(GraphicsEngine, self).initialize()

        turtleInit = Turtle()
        turtleInit.hideturtle()

        self.__setattr__('window', turtleInit.screen)
        window = self.__getattribute__('window')
        window.bgcolor("light green")
        window.listen()
