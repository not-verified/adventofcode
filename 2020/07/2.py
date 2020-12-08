import re
import itertools

must_contain = {}

with open('input.txt', 'r') as f:
    for line in f:
       container = re.search("^(.*?)(?=\s*bags)",line).groups('0')[0]
       contained = re.search("(?<=contain\s)(\d.*?bags?\,?\s?)+", line)
       if contained:
           for contained in [x.strip() for x in contained.group().split(',')]:
               contained_split = contained.split(' ')
               num_contained = contained_split[0]
               colour_contained = ' '.join(contained_split[1:-1])
               must_contain.setdefault(container, []).append((colour_contained, num_contained))

to_contain = list(itertools.chain(*[[x[0]] * int(x[1]) for x in must_contain.get("shiny gold")]))
contained = []

while to_contain != []:
    for idx, bag in enumerate(to_contain):
        contained += [bag]
        to_contain = to_contain[1:]
        to_add = list(itertools.chain(*[[y[0]] * int(y[1]) for y in must_contain.get(bag, [])]))
        to_contain.extend(to_add)
        
print(len(contained))