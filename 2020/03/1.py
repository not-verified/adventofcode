with open('input.txt', 'r') as f:
    lines = []
    for line in f:
        lines.append(line)

trees = 0
for idx, line in enumerate(lines):
    trees += 1 if line[(idx * 3) % (len(line)-1)] == "#" else 0

print(trees)
