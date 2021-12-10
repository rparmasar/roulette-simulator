from constants import board_layouts, payout_multipliers


# TODO: Refactor to allow for different layouts
def _createSuccessDomain(betType):
    """Returns a condition such that if a spin result falls in this domain, the payout is set to true."""
    BOARD_ARR = board_layouts.EUROPEAN_BOARD_NUMBER_SEQ

    # Here the strategy is to create the success checking fn and then return that depending on the bet type.
    if betType == 'zero':
        def isInDomain(spoke : object) -> bool:
            return spoke.number == 0
        
        return isInDomain
    
    if betType == 'single_colour':
        def isInDomain(spoke : object, colour : str) -> bool:
            return spoke.colour == colour
        
        return isInDomain
    
    if betType == 'number_parity':
        def isInDomain(spoke : object, parity : str) -> bool:
            if parity == 'even':
                return (spoke.number % 2) == 0
            elif parity == 'odd':
                return (spoke.number % 2) != 0
        
        return isInDomain
    
    if betType == 'lower_third':
        def isInDomain(spoke : object) -> bool:
            domain = range(1,13)
            return spoke.number in domain
        
        return isInDomain

    if betType == 'middle_third':
        def isInDomain(spoke : object) -> bool:
            domain = range(13,25)
            return spoke.number in domain
        
        return isInDomain

    if betType == 'upper_third':
        def isInDomain(spoke : object) -> bool:
            domain = range(25,37)
            return spoke.number in domain
        
        return isInDomain

    # If we get to here then its an invalid / not supported bet
    raise ValueError(f"Bet type: {betType} not supported!")

class Bet:
    """
    Represents a bet placed by a player that is evaluated at the end of a spin.

    TYPES
    =====

    Inside Bets
    ===========

    'single_number': Pays 35 to 1

    TODO: Add success condition
    'split: Covers 2 adjacent numbers, horizontally or vertically. Pays 17 to 1.

    TODO: Add success condition
    'three_in_a_row': Covers 3 consecutive numbers. Pays 11 to 1.

    TODO: Add success condition
    'squad': Covers 4 consecutive numbers. Pays 8 to 1.
    
    TODO: Add success condition
    'six_in_a_row: Covers 6 consecutive numbers. Pays 5 to 1.
    
    Outside Bets
    ============

    'single_colour': Pays 1 to 1

    'number_parity': Odd or Even: Pays 1 to 1

    TODO: Add success condition
    'bigger': Covers 1-18: Pays 1 to 1
    
    TODO: Add success condition
    'smaller': Covers 19-36: Pays 1 to 1

    TODO: Check here: https://www.roulette17.com/bets/columns/
    'first_column':
    
    'second_column': 
    
    'third_column':

    'lower_third': Covers 1-12; Pays 2 to 1
    
    'middle_third': Covers 13-24; Pays 2 to 1

    'upper_third': Covers 25-36; Pays 2 to 1
    """
    def __init__(self, betType: str, wager: float) -> None:
        self.betType = betType
        self.wager = wager
        self.successDomainValidator = _createSuccessDomain(betType)
    def resolve(self, spinResult: object) -> float:
        """Returns the update required to a Player's balance."""


    