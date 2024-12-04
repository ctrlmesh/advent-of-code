#!/usr/bin/env python3
INPUT_FILE = 'input2.txt'

def is_proper(arr):
    arr = [int(n) for n in arr]
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        for prev, curr in zip(arr, arr[1:]):
            if abs(prev - curr) in range(1, 4):
                continue
            break
        else: return True
    return False

safe_count = 0
with open(INPUT_FILE, 'r') as f:
    for report in f.readlines():
        arr = report.split()
        for i, _ in enumerate(arr):
            arr_copy = arr.copy()
            arr_copy.pop(i)
            if is_proper(arr_copy):
                safe_count += 1
                break
            
# Very hacky bruteforce solution      
print(safe_count)