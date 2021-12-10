from random import randint
from . import wheel_spoke
from constants import board_layouts

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
        number_sequence = board_layouts.EUROPEAN_BOARD_NUMBER_SEQ

        zero_spoke = wheel_spoke.Spoke(0, 'green')
        spokes = [wheel_spoke.Spoke(i, 'red') if (i % 2) == 0 else wheel_spoke.Spoke(i, 'black') for i in range(0, 36, 1)]

        full_spokes = [zero_spoke, *spokes]
        
        new_wheel = Wheel(full_spokes, wheelType)
        
        return new_wheel
