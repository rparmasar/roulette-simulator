def _createSuccessDomain(betType):
    """Returns a condition such that if a spin result falls in this domain, the payout is set to true."""

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

def _setPayout(betType):
    """Sets the payout for a given betType"""
    pass

class Bet:
    """
    Represents a bet placed by a player that is evaluated at the end of a spin.

    TYPES
    =====
    TODO: Confirm these payouts
    'zero': Pays 52 to 1

    'single_colour': Pays 2 to 1

    'number_parity': Odd or Even: Pays 2 to 1

    'single_number': Pays 20 to 1

    'lower_third': Covers 1-12; Pays 4 to 1
    
    'middle_third': Covers 13-24; Pays 4 to 1

    'upper_third': Covers 25-36; Pays 4 to 1
    """
    def __init__(self, betType: str, wager: float) -> None:
        self.betType = betType
        self.wager = wager
        self.successDomainValidator = _createSuccessDomain(betType)
    def evaluate(self, spinResult: object) -> float:
        """Returns the update required to a Player's balance."""


    