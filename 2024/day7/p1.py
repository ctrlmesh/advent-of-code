import itertools

INPUT_FILE = './inputs/input.txt'

with open(INPUT_FILE, 'r') as f:
    calcs = []
    for line in f.readlines():
        product = int(line.split(':')[0])
        numbers = list(map(lambda n: int(n), line.split(':')[1].split()))
        calcs.append((product, numbers))

result = 0
for product, numbers in calcs:
    for calc in map(''.join, itertools.product('+*', repeat=len(numbers)-1)):
        prev = numbers[0]
        for n2, operator in zip(numbers[1:], calc):
            prev = eval(f'{prev}{operator}{n2}')
        if prev == product:
            result += product
            break

print(result)
