import itertools

INPUT_FILE = './inputs/input.txt'

# TODO: Make this faster

with open(INPUT_FILE, 'r') as f:
    disk_map = f.read().strip()
    filesystem = []
    for id, (file_block, free_block) in enumerate(itertools.zip_longest(disk_map[::2], disk_map[1::2], fillvalue=0)):
        filesystem.extend([id]*int(file_block) + [-1] * int(free_block))

checksum = 0
for b_index, block in reversed(list(enumerate(filesystem))):
    if -1 not in filesystem:
        break
    if block != -1 and b_index > (f_index := filesystem.index(-1)):
        filesystem[f_index] = block
    filesystem.pop(b_index)

checksum = sum((index * id for index, id in enumerate(filesystem)))

print(checksum)
