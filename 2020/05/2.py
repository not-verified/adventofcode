def bin_string_to_num(x, map):
    res = 0
    for idx, char in enumerate(reversed(x)):
        res += map[char] * 2 ** idx
    return res

vertical_map = {"F": 0, "B": 1}
horizontal_map = {"L": 0, "R": 1}

high = 0
seats = []
with open('input.txt', 'r') as f:
    for line in f:
        seat = 8 * bin_string_to_num(line[:-4], vertical_map) + bin_string_to_num(line[-4:-1], horizontal_map)
        seats.append(seat)

seats.sort()

for a, b in (zip(seats[:-1],seats[1:])):
    if b - a != 1:
        print(b, a)