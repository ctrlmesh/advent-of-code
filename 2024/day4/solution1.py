INPUT_FILE = 'input2.txt'


def safesearch(_y, _x):
    try:
        if _x < 0 or _y < 0:
            raise (IndexError)
        return wordsearch[_y][_x]
    except IndexError:
        return '.'


with open(INPUT_FILE, 'r') as f:
    wordsearch = [line.strip() for line in f.readlines()]

to_check = []
x, y = len(wordsearch[0]), len(wordsearch)
for y0 in range(y):
    for x0 in range(x):
        if safesearch(y0, x0) in ['X', 'S']:
            to_check.append(''.join([safesearch(y0, x0+i) for i in range(4)]))
            to_check.append(''.join([safesearch(y0-i, x0) for i in range(4)]))
            to_check.append(
                ''.join([safesearch(y0-i, x0+i) for i in range(4)]))
            to_check.append(
                ''.join([safesearch(y0-i, x0-i) for i in range(4)]))

xmas_count = to_check.count('XMAS') + to_check.count('SAMX')
print(xmas_count)
