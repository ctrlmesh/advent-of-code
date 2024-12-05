INPUT_FILE = './inputs/input.txt'

safe_count = 0
with open(INPUT_FILE, 'r') as f:
    for report in f.readlines():
        for prev, curr in zip(report.split(), report.split()[1:]):
            prev, curr = int(prev), int(curr)
            if abs(prev - curr) in range(1, 4):
                if prev < curr and int(report.split()[0]) < int(report.split()[1]):
                    continue
                elif prev > curr and int(report.split()[0]) > int(report.split()[1]):
                    continue
                break
            else: break
        else:
            safe_count += 1
print(safe_count)