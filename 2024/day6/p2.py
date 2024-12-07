INPUT_FILE = './inputs/input.txt'

def travel_grid(grid, guard_pos, direction = (-1, 0)):
    visited = set()
    g_y, g_x = guard_pos
    d_y, d_x = direction
    while True:
        next_y, next_x = g_y + d_y, g_x + d_x
        if next_y not in range(0, len(grid)) or next_x not in range(0, len(grid[0])):
            break
        
        if (g_y, g_x, d_y, d_x) in visited:
            print('LOOP DETECTED')
            return -1
        visited.add((g_y, g_x, d_y, d_x))
        # grid[g_y][g_x] = 'X'
     
        if grid[next_y][next_x] == '#':
            # Rotate direction vector 90 degrees the easy way
            d_y, d_x = (0, -d_y) if d_y != 0 else (d_x, 0)
        else:
            g_y, g_x = next_y, next_x
        
    print('FINISHED')
    print(visited)
    return visited

with open(INPUT_FILE, 'r') as f:
    grid = []
    g_y, g_x = 0, 0
    for col_index, row in enumerate(f.readlines()):
        grid.append(list(row.strip()))
        if '^' in row:
            g_y, g_x = col_index, row.index('^')

loops = 0
for state in travel_grid(grid, (g_y, g_x)):
    g_y, g_x, d_y, d_x = state
    prev = grid[g_y + d_y][g_x + d_x]
    grid[g_y + d_y][g_x + d_x] = '#'
    if travel_grid(grid, (g_y, g_x), (d_y, d_x)) == -1:
        loops += 1
    grid[g_y + d_y][g_x + d_x] = prev

print(loops)
        

# travel_grid(grid, (g_y, g_x))
# grid_map = '\n'.join([''.join(row) for row in grid])

# print(grid_map)
# print(grid_map.count('X'))
        
        