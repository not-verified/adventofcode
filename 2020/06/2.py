groups = []

with open('input.txt', 'r') as f:
    group = []
    for line in f:
        if line != "\n":
            group.append(line.strip())
        else:
            groups.append(group)
            group = []
    groups.append(group) # Final group

def intersection_count(x):
    base_set = set(x[0])
    for element in x[1:]:
        base_set = base_set.intersection(element)
    return len(base_set)

print(sum([intersection_count(group) for group in groups]))