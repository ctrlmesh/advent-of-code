import itertools
import numpy as np

INPUT_FILE = './inputs/input.txt'

def place_antinodes(ant_pos, offset):
    ant_x, ant_y = ant_pos
    if 0 <= ant_x < grid.shape[1] and 0 <= ant_y < grid.shape[0]:
        antinodes.add((ant_x, ant_y))
        place_antinodes((ant_x + offset[0], ant_y + offset[1]), offset)

with open(INPUT_FILE, 'r') as f:
    grid = list()
    for line in f.readlines():
        grid.append(list(line.strip()))
    grid = np.array(grid)

antennas = set(zip(*np.where(grid != '.')))
same_freq = dict()
for a in antennas:
    same_freq.setdefault(grid[a], []).append(a)

antinodes = antennas.copy()
for antennas in same_freq.values():
    for (x1, y1), (x2, y2) in itertools.combinations(antennas, 2):
        x_d, y_d = x1 - x2, y1 - y2
        place_antinodes((x1, y1), (x_d, y_d))
        place_antinodes((x2, y2), (-x_d, -y_d))

print(f'Total number of unique antinodes: {len(antinodes)}')
