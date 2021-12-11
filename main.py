from lib import game

from pprint import pprint

def main():
    roulette_game = game.Game('European')
    testBet = {'single_number': {
        'numbers': [24]
    }}
    roulette_game.addPlayer('Rajeev', 1000)
    roulette_game.addPlayerBet('Rajeev', testBet, 10)

    result = roulette_game.simulate(n=10)
    pprint(result)




if __name__ == '__main__':
    main()