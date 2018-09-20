from src.core import *


class GraphicsEngine(SubsystemIf):
    def __init__(self):
        super(GraphicsEngine, self).__init__("Grafikmotor", "Ett subsystem som tillhandahåller vad som visas på skärmen")
