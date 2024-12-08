import itertools
import multiprocessing

INPUT_FILE = './inputs/input.txt'

def compute_possible_product(calc):
    product, numbers = calc
    for calc in itertools.product('+*|', repeat=len(numbers)-1):
        prev = numbers[0]
        for n, operator in zip(numbers[1:], calc):
            if operator == '|':
                prev = int(f'{prev}{n}')
            else:
                prev = eval(f'{prev}{operator}{n}')
        if prev == product:
            return product
    return 0

with open(INPUT_FILE, 'r') as f:
    calcs = []
    for line in f.readlines():
        product = int(line.split(':')[0])
        numbers = list(map(lambda n: int(n), line.split(':')[1].split()))
        calcs.append((product, numbers))

with multiprocessing.Pool() as pool:
    result = list(pool.map(compute_possible_product, calcs))

print(sum(result))