INPUT_FILE = './inputs/input.txt'

def safesearch(_y, _x):
    try:
        if _x < 0 or _y < 0:
            raise (IndexError)
        return wordsearch[_y][_x]
    except IndexError:
        return '.'

with open(INPUT_FILE, 'r') as f:
    wordsearch = [line.strip() for line in f.readlines()]

xmas_count = 0
x, y = len(wordsearch[0]), len(wordsearch)
for y0 in range(y):
    for x0 in range(x):
        if safesearch(y0, x0) == 'A':
            if (
                safesearch(y0-1, x0-1)+safesearch(y0+1, x0+1) in ['MS', 'SM'] and
                safesearch(y0-1, x0+1)+safesearch(y0+1, x0-1) in ['MS', 'SM']
            ):
                xmas_count += 1
                
print(xmas_count)
