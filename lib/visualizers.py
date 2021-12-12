import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def _convertMetaDataToDf(metadata: list) -> pd.DataFrame:
    """Takes metadata (list of dicts) and returns a dataframe for easier data viz"""
    df = pd.json_normalize(metadata)
    return df

def drawBalanceLinePlot(metadata: list, player_names: list):
    """Plots the balances of each player for each round."""
    df = _convertMetaDataToDf(metadata)

    index = df['id']

    for player_name in player_names:
        balance_col_name = f'player_metadata.{player_name}.balance'
        balances = df[balance_col_name]

        plt.plot(index, balances, label=player_name)
    
    plt.legend()
    plt.title('Player Balances over Time')
    plt.xlabel('Rounds')
    plt.ylabel('Balance ($)')
    plt.ylim(bottom=0)
    plt.show()
    

def drawRealTimeBalancePlot(metadata: list, player_names: list):
    """Plots in real-time, the balance of each player for all rounds."""
    df = _convertMetaDataToDf(metadata)
    index = df['id']
    
    fig, ax = plt.subplots()
    lines = []
    balances = []

    for player in player_names:
        current_col_name = f'player_metadata.{player}.balance'
        current_balance_col = df[current_col_name]
        current_line, = ax.plot(index, current_balance_col)
        
        balances.append(current_balance_col)
        lines.append(current_line)
        
    
    def update(num, lines, balances, x):
        for (line, balance_col) in zip(lines, balances):
            line.set_data(x[:num], balance_col[:num])
        
        return lines

    ani = animation.FuncAnimation(fig, update, len(index), fargs=[lines, balances, index], interval=150, repeat=False)

    ax.set_xlabel('Rounds')
    ax.set_ylabel('Balance ($)')
    ax.set_title('Player Balances over Time')
    ax.legend(player_names)

    plt.show()
    