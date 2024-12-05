import re, math

FILE_INPUT = './inputs/input.txt'

with open(FILE_INPUT, 'r') as f:
    find_disabled = re.compile(r"don't\(\).*?(?=do\(\)|$)", re.DOTALL)
    all = [re.findall(r'[0-9]+', exp) for exp in re.findall(r'mul\([0-9]+\,[0-9]+\)', re.sub(find_disabled, '', f.read()))]
    sum = sum([math.prod(map(lambda x: int(x), nums)) for nums in all])
    
print(sum)