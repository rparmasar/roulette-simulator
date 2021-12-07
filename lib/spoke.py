class Spoke:
    """
    Represents one spoke on a roulette wheel with a particular number and colour
    """
    def __init__(self, number, colour):
        self.number = number
        self.colour = colour
    def __repr__(self) -> str:
        return f"Spoke: {self.number} ({self.colour})"