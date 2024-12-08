INPUT_FILE = './inputs/input.txt'

def travel_grid(grid, guard_pos, direction=(-1, 0)):
    g_y, g_x = guard_pos
    d_y, d_x = direction
    visited = set()

    while True:
        next_y, next_x = g_y + d_y, g_x + d_x
        if next_y not in range(0, len(grid)) or next_x not in range(0, len(grid[0])):
            break

        if (next_y, next_x, d_y, d_x) in visited:
            return -1
        visited.add((next_y, next_x, d_y, d_x))

        if grid[next_y][next_x] == '#':
            # Rotate direction vector by 90 degrees the easy way
            d_y, d_x = (0, -d_y) if d_y != 0 else (d_x, 0)
        else:
            g_y, g_x = next_y, next_x
    return visited

with open(INPUT_FILE, 'r') as f:
    grid = []
    g_y, g_x = 0, 0
    for col_index, row in enumerate(f.readlines()):
        grid.append(list(row.strip()))
        if '^' in row:
            g_y, g_x = col_index, row.index('^')

start_pos = (g_y, g_x)

loops = 0
placed = set()

initial_path = travel_grid(grid, (g_y, g_x))
if initial_path != -1:
    for pos_y, pos_x, d_y, d_x in initial_path:
        if (pos_y, pos_x) in placed or (pos_y, pos_x) == start_pos:
            continue

        prev = grid[pos_y][pos_x]
        grid[pos_y][pos_x] = '#'
        if travel_grid(grid, start_pos) == -1:
            placed.add((pos_y, pos_x))
            loops += 1
        grid[pos_y][pos_x] = prev

print(loops)
