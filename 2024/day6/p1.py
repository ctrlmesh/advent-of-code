INPUT_FILE = './inputs/input.txt'

with open(INPUT_FILE, 'r') as f:
    grid = []
    g_y, g_x = 0, 0
    for col_index, row in enumerate(f.readlines()):
        grid.append(list(row.strip()))
        g_y, g_x  = (col_index, row.index('^')) if '^' in row else (g_y, g_x)
    
d_y, d_x = -1, 0
while True:
    next_y, next_x = g_y + d_y, g_x + d_x

    grid[g_y][g_x] = 'X'
    if next_y not in range(0, len(grid)) or next_x not in range(0, len(grid[0])):
        break
    elif grid[next_y][next_x] == '#':
        # Rotate direction vector 90 degrees the easy way
        d_y, d_x = (0, -d_y) if d_y != 0 else (d_x, 0)
        
    g_y, g_x = g_y + d_y, g_x + d_x

grid_map = '\n'.join([''.join(row) for row in grid])

print(grid_map)
print(grid_map.count('X'))
