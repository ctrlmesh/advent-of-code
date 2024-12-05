from math import floor

INPUT_FILE = 'input2.txt'

def sort_pages(pages):
    new_pages = []
    for page in pages:
        index = len(new_pages)
        while not all([index < new_pages.index(rule)+1 for rule in set(new_pages) & set(page_rules.get(page, []))]):
            index -= 1
        new_pages.insert(index, page)
    return new_pages

with open(INPUT_FILE, 'r') as f:
    rules, prints = (block.split() for block in f.read().split('\n\n'))

page_rules = {}
for rule in rules:
    rule = rule.split('|')
    page_rules.setdefault(rule[0], []).append(rule[1])

page_sum = 0
for pages in prints:
    pages = pages.split(',')
    if pages != (new_pages := sort_pages(pages)):
        page_sum += int(new_pages[floor(len(new_pages) / 2)])
print(page_sum)
            