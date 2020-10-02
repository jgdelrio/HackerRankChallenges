"""
Dashboard > Artificial Intelligence > Games > Lights Out

Lights Out is a game of cellular automaton where a cell and all its defined neighbors changes states on firing it.
In this version of Lights Out, 2 players compete against each other by firing the cells on an 8x8 grid.
Each cell has 2 states:
  -  ON indicated by the number 1
  -  OFF indicated by the number 0

A cell at (r,c) on firing changes its state and 2 of its neighbors,
the one towards its right (r,c+1) and the one below (r+1,c).

You are allowed only to fire at cells that are ON.

Input format
------------
Top left cell of the grid is indexed as (0,0) and the bottom right of the grid is indexed at (7,7).
The 1st player is represented by the number 1 and the 2nd player is represented by the number 2.

The first line of input contains the number of the current player.
8 lines follow, each line containing 8 integers without any space between them.
Each integer can be either 0 or 1 representing the 2 states of the cell.

Output Format
-------------
You are required to output two single spaced integers that is the position of the cell you wish to fire.
"""
import re
import numpy as np
from time import time


princess_regexp = re.compile(r'p')
bot_regexp = re.compile(r'm')

# Fixed matrix for testing
TESTS_BAK = [
    [[0, 1, 1, 0],
     [0, 1, 0, 1],
     [1, 0, 0, 0],
     [0, 0, 1, 0]],
]

# Random matrix for testing and evaluation
RAND_SIZE = np.random.choice(range(3, 100, 2))
TESTS = [np.random.randint(0, 2, (RAND_SIZE, RAND_SIZE)).tolist()]


policy_dict = {1: 'policy1', 2: 'policy2'}


def nextMove(player, grid):
    n = len(grid)
    grid = np.array(grid)

    evaluation = (grid * (grid + \
                          np.concatenate([grid[1:, :], np.zeros((1, n))], axis=0) + \
                          np.concatenate([grid[:, 1:], np.zeros((n, 1))], axis=1)) ).astype('uint8')
    locate_3 = np.argwhere(evaluation == 3)
    n3 = len(locate_3)
    locate_2 = np.argwhere(evaluation == 2)
    n2 = len(locate_2)
    locate_1 = np.argwhere(evaluation == 1)
    n1 = len(locate_1)
    total = sum_grid(grid)
    print(f"Player: {player} Evaluation table... \n{evaluation}")

    # Set policies: We can set different policies for player 1 and 2 as per policy_dict
    if policy_dict[player] == 'policy1':
        if n1 > 0:
            return locate_1[-1]
        elif n2 > 0:
            return locate_2[-1]
        elif n3 > 0:
            return locate_3[-1]

    elif policy_dict[player] == 'policy2':
        if n3 > 0:
            return locate_3[0]
        elif n2 > 0:
            return locate_2[0]
        else:
            return locate_1[0]

    else:
        raise ValueError("Invalid policy reference")


def hackerrank_run():
    player = int(input())
    grid = []
    grid.append(list(map(int, input().strip())))
    n = len(grid[0]) - 1
    for i in range(0, n):
        grid.append(list(map(int, input().strip())))

    nextMove(player, grid)


def update_grid(grid, move):
    val = grid[move[0]][move[1]]
    n = len(grid)
    if val == 1:
        grid[move[0]][move[1]] = 0
        # Swap right value
        if move[1]+1 < n:
            grid[move[0]][move[1]+1] = 1 - grid[move[0]][move[1]+1]
        # Swap down value
        if move[0]+1 < n:
            grid[move[0]+1][move[1]] = 1 - grid[move[0]+1][move[1]]
        print(f"Updated grid:")
        print(np.array(grid))
        return grid
    else:
        raise ValueError(f"The move '{move}' is not allowed")


def sum_grid(grid):
    return np.sum(np.array(grid))


def test():
    data = TESTS
    player = 1
    for grid in data:
        t0 = time()
        total_sum = 1
        print(f"Initial grid: \n{np.array(grid)}")
        while total_sum > 0:
            move = nextMove(player, grid)
            grid = update_grid(grid, move)
            total_sum = sum_grid(grid)
            print("------------------------------------")
            player = 3 - player

        print(f"We have a winner!! Which is {3 - player}")
        t1 = time() - t0
        print(f'Total time: {t1}')


if __name__ == '__main__':
    test()
