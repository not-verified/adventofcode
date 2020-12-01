import itertools

threshold = int(2020/2)
large_numbers = []
small_numbers = []

with open('input.txt', 'r') as f:
    for line in f:
        num = int(line)
        if num >= threshold:
            large_numbers.append(num)
        if num <= threshold:
            small_numbers.append(num)
            
for combo in itertools.product(small_numbers, small_numbers, large_numbers):
    if (combo[0] + combo[1] + combo[2] == 2020):
        print(combo[0] * combo[1] * combo[2])