from abc import abstractmethod

from src.core import *
from src.tools.Logging import Log

class SubsystemIf(InitializerIf):
    def __init__(self, name, description):
        super(SubsystemIf, self).__init__(name, description)

    @abstractmethod
    def initialize(self):
        Log.out("Initialiserar subsystem: " + self.__getattribute__('name'))
