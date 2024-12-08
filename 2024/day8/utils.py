def print_grid(grid):
    print('  ', end='')
    for i in range(grid.shape[0]):
        print(f'  {i} ', end='')
    print('')
    for i, row in enumerate(grid):
        print(f'{i} ', end='')
        print(row)

def save_grid(grid):
    with open('./outputs/output.txt', 'w') as f:
        for row in grid:
            f.write(''.join(row)+'\n')
