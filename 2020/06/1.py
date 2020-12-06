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

print(sum([len(set(''.join(group))) for group in groups]))