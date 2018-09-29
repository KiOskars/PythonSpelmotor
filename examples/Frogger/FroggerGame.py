from src.core import Spelmotor

engine = Spelmotor()

if engine.initialize() == 0:
    engine.run()

engine.deinitialize()
