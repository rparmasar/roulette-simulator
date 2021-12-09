from random import randint
from . import wheel_spoke

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
        index = randint(0, maxIndex - 1)
        print(index)
        return self.spokes[index]

def createWheel(wheelType='European'):
    """
    Creates an initial instance of a Wheel according to the wheelType (can be American or European)
    """
    if wheelType == 'European':
        # Omits 0 as it is green
        number_sequence = [32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

        zero_spoke = wheel_spoke.Spoke(0, 'green')
        spokes = [wheel_spoke.Spoke(i, 'red') if (i % 2) == 0 else wheel_spoke.Spoke(i, 'black') for i in range(0, 36, 1)]

        full_spokes = [zero_spoke, *spokes]
        
        new_wheel = Wheel(full_spokes, wheelType)
        return new_wheel
