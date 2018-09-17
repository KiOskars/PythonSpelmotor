from abc import abstractmethod

from src.tools.Logging import Log
from .InitializerIf import InitializerIf


class SubsystemIf(InitializerIf):
    def __init__(self, name, description):
        super(SubsystemIf, self).__init__(name, description)

    @abstractmethod
    def initialize(self):
        Log.out("Initialiserade " + self.__getattribute__('name'))

