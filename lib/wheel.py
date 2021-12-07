from random import randint

class Wheel:
    """
    Represents a collection of spokes.
    """
    def __init__(self, spokes, wheelType):
        self.spokes = spokes
        self.wheelType = wheelType # European or American
    def __repr__(self) -> str:
        return f"Wheel: {self.wheelType} with spokes: {self.spokes}"
    def spin(self):
        "Simulates a spin of the wheel and randomly chooses a spoke"
        maxIndex = len(self.spokes)
        index = randint(0, maxIndex)
        return index
