FILE_INPUT = './inputs/input.txt'

total_similarity = 0
left, right = [], []

with open(FILE_INPUT, 'r') as f:
    for line in f.readlines():
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

for number in left:
    total_similarity += number * right.count(number)

print(total_similarity)
