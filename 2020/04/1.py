valid = 0

def IsValid(doc):
    should_contain = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for elem in doc.split(' '):
        field = elem.split(':')[0]
        if should_contain.__contains__(field):
            should_contain.remove(field)
    return len(should_contain) == 0

with open('input.txt', 'r') as f:
    doc = ""
    for line in f:
        if line != "\n":
            doc += " " + line.strip('\n')
        else:
            if IsValid(doc):
                valid += 1
            doc = ""
print(valid)