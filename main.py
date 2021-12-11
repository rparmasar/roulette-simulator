import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from lib import game, visualizers
from pprint import pprint

def main():
    roulette_game = game.Game('European')
    testBet = {'single_number': {
        'numbers': [24]
    }}
    testBet2 = {'two_numbers': {
        'numbers': [10, 0]
    }}

    roulette_game.addPlayer('Rajeev', 1000)
    roulette_game.addPlayerBet('Rajeev', testBet, 1)
    roulette_game.addPlayerBet('Rajeev', {'single_colour':{'colour': 'black'}}, 20)
    
    roulette_game.addPlayer('Gary', 1000)
    roulette_game.addPlayerBet('Gary', testBet2, 1)

    result = roulette_game.simulate(n=1000)

    rounds = [rnd['id'] for rnd in result]
    player_metadata = [rnd['player_metadata'] for rnd in result]
    player_balances1 = [x['Rajeev']['balance'] for x in player_metadata]
    player_balances2 = [x['Gary']['balance'] for x in player_metadata]

    testdict = {'Rajeev': player_balances1, 'Gary': player_balances2}
    testdf = pd.DataFrame(testdict)

    
    sns.lineplot(data=testdf)
    
    plt.show()
    
    
    




if __name__ == '__main__':
    main()