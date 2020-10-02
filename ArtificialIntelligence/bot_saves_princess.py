"""
Dashboard > Artificial Intelligence > Bot Building  Bot saves princess

Princess Peach is trapped in one of the four corners of a square grid.
You are in the center of the grid and can move one step at a time
in any of the four directions. Can you rescue the princess?

Input format
------------
The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid.
This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45).
The bot position is denoted by 'm' and the princess position is denoted by 'p'.

Grid is indexed using Matrix Convention
"""
import re
from math import ceil
from time import time


princess_regexp = re.compile(r'p')
bot_regexp = re.compile(r'm')

TESTS = [
    ([3, ('---', '-m-', 'p--')], ['DOWN', 'LEFT']),
    ([5, ('----p', '-----', '--m--', '-----', '-----')], ['UP', 'RIGHT', 'UP', 'RIGHT']),
    ([5, ('-----', '-----', '--m--', '-----', 'p----')], ['DOWN', 'LEFT', 'DOWN', 'LEFT']),
    ([5, ('-----', '-----', '--m--', '-----', '----p')], ['DOWN', 'RIGHT', 'DOWN', 'RIGHT']),
]


def lateral_move(pos, centre):
    if pos[1] > centre:
        return 'RIGHT'
    else:
        return 'LEFT'


princes_moves_dict = {
    'LEFT': 1,
    'RIGHT': -1,
}


def displayPathtoPrincess(n, grid):
    princess = None
    bot = None
    centre = ceil(n/2)
    moves = []
    princ_move = None
    for idx, row in enumerate(grid):
        p_pos = princess_regexp.search(row)
        b_pos = bot_regexp.search(row)
        if p_pos:
            princess = [idx, p_pos.start()]
        if b_pos:
            bot = [idx, b_pos.start()]

        if princess and (bot is None):
            if princ_move is None:
                princ_move = lateral_move(princess, centre)
            moves.extend(['UP', princ_move])
            princess = [idx+1, princess[1] + princes_moves_dict[moves[-1]]]
        elif princess and bot:
            diff = princess[1] - bot[1]
            if diff > 0:
                moves.extend([i for k in range(abs(diff)) for i in ['DOWN', 'RIGHT']])
                bot = [bot[0]+diff, bot[1]+diff]
            else:
                moves.extend([i for k in range(abs(diff)) for i in ['DOWN', 'LEFT']])
                bot = [bot[0]-diff, bot[1]+diff]

        if bot is not None and bot == princess:
            moves_str = '\n'.join(moves)
            print(moves_str)
            return moves


def hackerrank_run():
    # print all the moves here
    m = int(input())
    grid = []
    for i in range(0, m):
        grid.append(input().strip())

    displayPathtoPrincess(m, grid)


def test():
    data = TESTS
    for d in data:
        input = d[0]
        output = d[1]

        t0 = time()
        rst = displayPathtoPrincess(*input)
        t1 = time() - t0
        if not rst == output:
            print(f"{input} Expected: {output} Result: {rst}")
        print(f'Total time: {t1}')


if __name__ == '__main__':
    test()
