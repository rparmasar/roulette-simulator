class Player:
    """
    Represents a player in this game that can make bets and has an initial cash balance.
    """
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bets = []
    def placeBet(self, bet):
        """Adds a bet object to the player's bets property which is evaluated after each spin."""
        self.bets.append(bet)
        return f'Placed bet for {self.name}'
    def updateBalance(self, balance):
        """Updates the balance of this Player."""
        self.balance += balance
        return f'New balance for {self.name} is ${self.balance}'
        