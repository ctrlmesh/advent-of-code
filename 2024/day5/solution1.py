from math import floor

INPUT_FILE = 'input2.txt'

with open(INPUT_FILE, 'r') as f:
    rules, prints = (block.split() for block in f.read().split('\n\n'))

page_sum = 0
for pages in prints:
    pages = pages.split(',')
    for rule in rules:
        rule = rule.split('|')
        if rule[0] in pages and rule[1] in pages:
            if not pages.index(rule[0]) < pages.index(rule[1]):
                break
    else:
        page_sum += int(pages[floor(len(pages) / 2)])
print(page_sum)
            