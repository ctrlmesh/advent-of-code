INPUT_FILE = './inputs/example.txt'

def travel_grid(grid, guard_pos, direction = (-1, 0)):
    visited = {}
    g_y, g_x = guard_pos
    d_y, d_x = direction
    while True:
        if not (d_y, d_x) in visited.setdefault(f'{g_y} {g_x}', []):
            visited.setdefault(f'{g_y} {g_x}', []).append((d_y, d_x))
        else:
            print('LOOP DETECTED')
            return -1
        # grid[g_y][g_x] = 'X'
        
        next_y, next_x = g_y + d_y, g_x + d_x
        if next_y not in range(0, len(grid)) or next_x not in range(0, len(grid[0])):
            break
        
        if grid[next_y][next_x] == '#':
            # Rotate direction vector 90 degrees the easy way
            d_y, d_x = (0, -d_y) if d_y != 0 else (d_x, 0)
        else:
            g_y, g_x = g_y + d_y, g_x + d_x
        
    print('FINISHED')
    print(visited)
    return visited

with open(INPUT_FILE, 'r') as f:
    grid = []
    g_y, g_x = 0, 0
    for col_index, row in enumerate(f.readlines()):
        grid.append(list(row.strip()))
        g_y, g_x  = (col_index, row.index('^')) if '^' in row else (g_y, g_x)

# for coords, directions in travel_grid(grid, (g_y, g_x)).items():
#     g_y, g_x = [int(i) for i in coords.split()]
#     for direction in directions:
        
    
# grid_map = '\n'.join([''.join(row) for row in grid])

# print(grid_map)
# print(grid_map.count('X'))
        
        