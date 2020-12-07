import re

can_be_in = {}

with open('input.txt', 'r') as f:
    for line in f:
       container = re.search("^(.*?)(?=\s*bags)",line).groups('0')[0]
       contained = re.search("(?<=contain\s)(\d.*?bags?\,?\s?)+", line)
       if contained:
           for contained in [x.strip() for x in contained.group().split(',')]:
               contained_split = contained.split(' ')
               num_contained = contained_split[0]
               colour_contained = ' '.join(contained_split[1:-1])
               can_be_in.setdefault(colour_contained, []).append(container)

to_explore = can_be_in.get("shiny gold")
explored = []

while to_explore != []:
    for bag in to_explore:
        explored += [bag]
        to_explore = [x for x in list(set(to_explore + can_be_in.get(bag, []))) if x not in explored]

print(len(explored))