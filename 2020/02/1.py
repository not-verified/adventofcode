import re

valid = 0
r = re.compile('(?P<min>\d+)-(?P<max>\d+)\s(?P<c>.):\s(?P<s>.*)')

def IsValid(s):
    m = r.match(s)
    return int(m.group('min')) <= m.group('s').count(m.group('c')) <= int(m.group('max'))

with open('input.txt', 'r') as f:
    for line in f:
        if IsValid(line):
            valid += 1

print(valid)
