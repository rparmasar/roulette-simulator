from lib import game, visualizers

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

    player_names = list(roulette_game.players.keys())
    # visualizers.drawBalanceLinePlot(result, player_names)
    visualizers.drawRealTimeBalancePlot(result, player_names)
    
    
    
    




if __name__ == '__main__':
    main()