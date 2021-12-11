class Round:
    """
    Represents an instance where the wheel is spun and bets are evaluated.
    """
    def __init__(self, id: str) -> None:
        self.id = id
    def run(self, wheel: object, players: list) -> dict:
        """
        Spins the wheel, evaluates the bets for each player and returns the metadata for this round.
        
        Parameters
        ==========

        wheel (Wheel): An instance of the Wheel class.

        players (list of Player): A list of Player instances with bets.

        Returns
        =======

        metadata (dictionary): A dictionary containing information like:
        - spin result
        - player wins
        - player balances
        """
        # Get our spin result
        spinResult = wheel.spin()

        metadata = {}

        # For loop here for readability and easier updating of metadata.
        for player in players:
            player_metadata = {}

            # Get the resultant balance update after resolving each bet.
            balance_update = sum([bet.resolve(spinResult) for bet in player.bets])

            player.updateBalance(balance_update)

            player_metadata['balance'] = player.balance
            player_metadata['win'] = 1 if balance_update > 0 else 0
        
        # Now update the metadata
        metadata['spin_result_number'] = spinResult.number
        metadata['spin_result_colour'] = spinResult.colour
        metadata['player_metadata'] = player_metadata
        metadata['id'] = self.id

        return metadata
            

                



        