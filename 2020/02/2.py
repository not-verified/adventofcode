import re

valid = 0
r = re.compile('(?P<min>\d+)-(?P<max>\d+)\s(?P<c>.):\s(?P<s>.*)')

def IsValid(s):
    m = r.match(s)
    s = m.group('s')
    c = m.group('c')
    return (s[int(m.group('min')) - 1] == c) != (s[int(m.group('max')) - 1] == c)

with open('input.txt', 'r') as f:
    for line in f:
        if IsValid(line):
            valid += 1

print(valid)
