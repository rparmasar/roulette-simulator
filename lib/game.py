from . import roulette_round, wheel, player

class Game:
    """
    Represents a collection of many rounds of a particular type of roulette
    """
    def __init__(self, wheelType: str) -> None:
        self.wheel = wheel.createWheel(wheelType)
        self.players = {}
    def addPlayer(self, player_name: str, balance: float) -> None:
        """Creates a Player object and adds it to this Game."""
        new_player = player.Player(player_name, balance)
        self.players[player_name] = new_player
    def addPlayerBet(self, player_name: str, bet: dict, wager: float) -> None:
        """Places a bet for the given Player."""
        current_player = self.players[player_name]

        current_player.placeBet(bet, wager)
    def simulate(self, n: int=1000) -> list:
        """Runs n rounds and returns a list of metadata for each round."""
        # TODO: Make sure n is valid (not < 0)
        metadata_list = []

        for i in range(0,n):
            current_round = roulette_round.Round(i)
            
            # Params for a given round
            WHEEL = self.wheel
            PLAYERS = list(self.players.values())

            round_metadata = current_round.run(wheel=WHEEL, players=PLAYERS)
            # Put in our result list
            metadata_list.append(round_metadata)
        
        return metadata_list
            

    
    
