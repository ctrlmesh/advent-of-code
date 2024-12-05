FILE_INPUT = './inputs/input.txt'

total_distance = 0
left, right = [], []
with open(FILE_INPUT, 'r') as f:
    for line in f.readlines():
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

for n1, n2 in zip(sorted(left), sorted(right)):
    total_distance += abs(n1 - n2)

print(total_distance)