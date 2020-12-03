import math
with open('input.txt', 'r') as f:
    lines = []
    for line in f:
        lines.append(line)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

grand_total = 1
for right, down in slopes:
    trees = 0
    right_per_line = right/down
    for idx, line in enumerate(lines):
        if idx % down == 0:
            trees += 1 if line[(int(idx * right_per_line)) % (len(line)-1)] == "#" else 0
    grand_total *= trees

print(grand_total)
