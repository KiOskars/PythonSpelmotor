from abc import abstractmethod

from src.tools.Logging import Log


class InitializerIf:
    def __init__(self, name: str, description):
        self.setName(name)
        self.__setattr__('description', description)
        self.__setattr__('type', type(self).__name__)

    @abstractmethod
    def initialize(self):
        Log.out("Initialiserade",
                self.__str__(),
                "== * Attribut * ==",
                **self.__dict__)

    def __str__(self):
        return self.__getattribute__('name') + "\n" + self.__getattribute__('description')

    def setName(self, name):
        self.__setattr__('name', name + " - " + type(self).__name__)

    def getName(self):
        return self.__getattribute__('name')

    def printAttributes(self):
        Log.out(**self.__dict__)
