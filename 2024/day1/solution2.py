#!/usr/bin/env python3

FILE_INPUT = 'input2.txt'

def main():
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

if __name__ == '__main__':
    main()