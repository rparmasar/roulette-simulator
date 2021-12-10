from .constants import board_layouts, payout_multipliers

EUROPEAN_PAYOUTS = payout_multipliers.EUROPEAN_PAYOUT_MULTIPLIERS

# TODO: Refactor to allow for different layouts
def _createSuccessDomain(betType):
    """Returns a condition such that if a spin result falls in this domain, the payout is set to true."""

    # Here the strategy is to create the success checking fn and then return that depending on the bet type.
    if betType == 'single_number':
        def isInDomain(spoke : object,  number_arr: list) -> bool:
            return spoke.number in number_arr
        
        return isInDomain
    
    if betType == 'two_numbers':
        def isInDomain(spoke: object, two_number_arr: list) -> bool:
            return spoke.number in two_number_arr
        
        return isInDomain
    
    if betType == 'three_numbers':
        def isInDomain(spoke: object, three_number_arr: list) -> bool:
            return spoke.number in three_number_arr
        
        return isInDomain
    
    if betType == 'four_numbers':
        def isInDomain(spoke: object, four_number_arr: list) -> bool:
            return spoke.number in four_number_arr
        
        return isInDomain
    
    if betType == 'five_numbers':
        def isInDomain(spoke: object, five_number_arr: list) -> bool:
            return spoke.number in five_number_arr
        
        return isInDomain
    
    if betType == 'six_numbers':
        def isInDomain(spoke: object, six_number_arr: list) -> bool:
            return spoke.number in six_number_arr
        
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
    
    if betType == 'bigger':
        def isInDomain(spoke: object) -> bool:
            return spoke.number in range(1,18 + 1)
    
        return isInDomain

    if betType == 'smaller':
        def isInDomain(spoke: object) -> bool:
            return spoke.number in range(19,36 + 1)
    
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
    TODO: Update here.

    TYPES
    =====

    Inside Bets
    ===========

    'single_number': Pays 35 to 1

    'two_numbers': Covers 2 consecutive numbers. Pays 17 to 1.

    'three_numbers': Covers 3 consecutive numbers. Pays 11 to 1.

    'four_numbers': Covers 4 consecutive numbers. Pays 8 to 1.
    
    'five_numbers': Covers 5 consecutive numbers. Pays 6 to 1.
    
    'six_numbers: Covers 6 consecutive numbers. Pays 5 to 1.
    
    Outside Bets
    ============

    'single_colour': Pays 1 to 1

    'number_parity': Odd or Even: Pays 1 to 1

    'bigger': Covers 1-18: Pays 1 to 1
    
    'smaller': Covers 19-36: Pays 1 to 1

    TODO: Check here: https://www.roulette17.com/bets/columns/
    'first_column':
    
    'second_column': 
    
    'third_column':

    'lower_third': Covers 1-12; Pays 2 to 1
    
    'middle_third': Covers 13-24; Pays 2 to 1

    'upper_third': Covers 25-36; Pays 2 to 1
    """
    def __init__(self, betType: str, wager: float, params: dict={}) -> None:
        self.betType = betType
        self.wager = wager
        self.params = params
        # TODO: Need to refactor here for multiple game types.
        self.successDomainValidator = _createSuccessDomain(betType)
        self.payout = EUROPEAN_PAYOUTS[betType]
    def resolve(self, spinResult: object) -> float:
        """Returns the update required to a Player's balance."""
        if 'numbers' in self.params:
            # params of the form {'numbers': [1,2,3,...]}
            resolveStatus = self.successDomainValidator(spinResult, self.params['numbers'])
        elif 'parity' in self.params:
            # params of the form {'parity': 'odd' or 'even'}
            resolveStatus = self.successDomainValidator(spinResult, self.params['parity'])
        elif 'colour' in self.params:
            # params of the form {'colour': 'black' or 'red'}
            resolveStatus = self.successDomainValidator(spinResult, self.params['colour'])
        else:
            resolveStatus = self.successDomainValidator(spinResult)

        
        if resolveStatus:
            return self.wager * self.payout
        else:
            return self.wager * -1
        


    