import itertools
import numpy as np

INPUT_FILE = './inputs/input.txt'

with open(INPUT_FILE, 'r') as f:
    grid = list()
    for line in f.readlines():
        grid.append(list(line.strip()))
    grid = np.array(grid)

same_freq = dict()
for a in zip(*np.where(grid != '.')): 
    same_freq.setdefault(grid[a], []).append(a)

antinodes = set()
for antennas in same_freq.values():
    for (x1, y1), (x2, y2) in itertools.combinations(antennas, 2):
        x_d, y_d = x1 - x2, y1 - y2
        ant1_x, ant1_y = x1 + x_d, y1 + y_d
        ant2_x, ant2_y = x2 - x_d, y2 - y_d
        
        if 0 <= ant1_x < grid.shape[1] and 0 <= ant1_y < grid.shape[0]:
            antinodes.add((ant1_x, ant1_y))
        if 0 <= ant2_x < grid.shape[1] and 0 <= ant2_y < grid.shape[0]:
            antinodes.add((ant2_x, ant2_y))

print(f'Total number of unique antinodes: {len(antinodes)}')