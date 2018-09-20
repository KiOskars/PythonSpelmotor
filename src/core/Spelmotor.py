from src.core import *

from src.game import *
from src.graphics import GraphicsEngine
from src.tools.Logging import Log

class Spelmotor(SubsystemIf):
    def __init__(self):
        super(Spelmotor, self).__init__("Frogger Game Engine", "En spelmotor för att skapa spelet Frogger")

        self.initializeSubsystem('grafikmotor', GraphicsEngine())

    def play(self):
        player = Entity("Player", "turtle", 90, 10, 0, 0, "blue")
        player.defineKeys(self.getSubsystem('grafikmotor').__getattribute__('window'))

        enemy = Entity("Enemy", "arrow", 0, 10, -500, 0, "red")

        done()

        Log.out("Stänger ner applikationen och avslutar processen", "Ha en bra dag!")

    def initializeSubsystem(self, key, subsystem: SubsystemIf):
        if not self.__dict__.__contains__(subsystem):
            Log.out("Subsystemet fanns inte i {}, sätter attributet {} som {}".format(self.getName(),
                                                                                      key,
                                                                                      subsystem.getName()))
            self.__setattr__(key, subsystem)

        Log.out("Inititaliserar {} som attribut {}".format(subsystem.getName(), key))
        return subsystem.initialize()

    def deinitializeSubsystem(self, key):
        subsystem = self.getSubsystem(key)

        if subsystem is None:
            Log.out("{} har inget subsystem {}", self.getName(), key)
            return 1

        Log.out("Avinititaliserar {} som attribut {}".format(subsystem.getName(), key))

        return subsystem.deinitialize()

    def getSubsystem(self, key) -> SubsystemIf:
        return self.__getattribute__(key)

