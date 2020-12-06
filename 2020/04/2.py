import re

valid = 0

def IsValidField(field, val):
    switcher = {
        "byr": lambda x: 2002 >= int(x) >= 1920,
        "iyr": lambda x: 2020 >= int(x) >= 2010,
        "eyr": lambda x: 2030 >= int(x) >= 2020,
        "hgt": lambda x: 193 >= int(x.split("c")[0]) >= 150 if "cm" == x[-2:] else 76 >= int(x.split("i")[0]) >= 59 if "in" == x[-2:] else False,
        "hcl": lambda x: True if re.search("^#[a-f0-9]{6}$",x) else False,
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: True if re.search("^[0-9]{9}$",x) else False,
    }
    print(field, val, switcher[field](val))
    return switcher[field](val)

def IsValid(doc):
    should_contain = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for elem in doc.split(' '):
        field, *val = elem.split(':')
        val = val or " "
        val = val[0]
        if should_contain.__contains__(field):
            if IsValidField(field, val):
                should_contain.remove(field)
    return len(should_contain) == 0

with open('input.txt', 'r') as f:
    doc = ""
    for line in f:
        if line != "\n":
            doc += " " + line.strip('\n')
        else:
            if IsValid(doc):
                print("VALID!")
                print(doc)
                valid += 1
            else:
                print("INVALID!")
                print(doc)
            doc = ""
print(valid)