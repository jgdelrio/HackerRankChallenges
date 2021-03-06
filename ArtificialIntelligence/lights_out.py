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
import random
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
SIZE_LIMIT = 10                                       # Up to 100 in the challenge
RAND_SIZE = random.choice(range(3, SIZE_LIMIT, 2))
TESTS = [[random.choices(range(0,2), k=RAND_SIZE) for _ in range(RAND_SIZE)]]

policy_dict = {1: 'policy1', 2: 'policy2'}


def sum_grid(grid):
    return sum(map(sum, grid))


def locate(grid, number):
    return [(row_idx, col_idx) for row_idx, row in enumerate(grid) for col_idx, elem in enumerate(row) if elem == number]


def nextMove(player, grid):
    n = len(grid)

    evaluation = []
    for idx, row in enumerate(grid):
        evaluation.append(grid[idx])
        # Add next row if exists
        if idx + 1 < n:
            evaluation[idx] = [e + i for e, i in zip(evaluation[idx], grid[idx+1])]
        # Add next column
        for k in range(n-1):
            evaluation[idx][k] += row[k+1]
        # Clean up
        evaluation[idx] = [e * i for e, i in zip(evaluation[idx], grid[idx])]

    locate_3 = locate(evaluation, 3)
    n3 = len(locate_3)
    locate_2 = locate(evaluation, 2)
    n2 = len(locate_2)
    locate_1 = locate(evaluation, 1)
    n1 = len(locate_1)
    total = sum_grid(grid)
    print(f"Player: {player} --> Total sum: {total} | Evaluation table...")
    print_grid(evaluation)

    # Set policies: We can set different policies for player 1 and 2 as per policy_dict
    if policy_dict[player] == 'policy1':
        if n1 > 0:
            move = locate_1[-1]
        elif n2 > 0:
            move = locate_2[-1]
        elif n3 > 0:
            move = locate_3[-1]

    elif policy_dict[player] == 'policy2':
        if n3 > 0:
            move = locate_3[0]
        elif n2 > 0:
            move = locate_2[0]
        else:
            move = locate_1[0]

    else:
        raise ValueError("Invalid policy reference")

    [print(f"{k} ", end='') for k in move]
    print('')
    return move


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
        print_grid(grid)
        return grid
    else:
        raise ValueError(f"The move '{move}' is not allowed")


def print_grid(grid):
    [print(f" {row}") for row in grid]


def test():
    data = TESTS
    player = 1
    for grid in data:
        t0 = time()
        total_sum = 1
        print(f"Initial grid:")
        print_grid(grid)
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
