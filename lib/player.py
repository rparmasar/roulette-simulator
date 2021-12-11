from pytest import param
from . import bet as bt

class Player:
    """
    Represents a player in this game that can make bets and has an initial cash balance.
    """
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bets = []
    def placeBet(self, bet: dict, wager: float):
        """
        Adds a bet object to the player's bets property which is evaluated after each spin.

        Parameters
        ==========

        bet (dict): An input describing the bet. It is of the form {'betType': params}. Eg. a bet on 24 would be {'single_number': [24]}

        wager (float): The size of the wager.
        """
        # These will be tuples
        betTypeTuple, paramsTuple = zip(*bet.items())
        betType = betTypeTuple[0]
        params = paramsTuple[0]

        betObj = bt.Bet(betType, wager, params)

        self.bets.append(betObj)
        return f'Placed bet for {self.name}'
    def updateBalance(self, balance):
        """Updates the balance of this Player."""
        self.balance += balance
        return f'New balance for {self.name} is ${self.balance}'
        