"""
The automatic passport scanners are slow
because they're having trouble detecting 
which passports have all required fields.
The expected fields are as follows:
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)


You can continue to ignore the cid field, but each other field has
strict rules about what values are valid for automatic validation:
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both
present and valid according to the above rules.
"""

FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
EYE_COLOURS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def loadData():
    data = []
    elem = []
    with open("data.txt") as f:
        info = f.readlines()
        for line in info:
            if line == '\n':
                data.append(elem)
                elem = []
            else:
                lineList = line.split()
                for field in lineList:
                    elem.append(field)
        data.append(elem)
    return data

def checkPassport(data):
    passportFields = []
    validPassports = 0
    fieldNum = 0
    for passport in data:
        for field in passport:
            passportFields.append(field[0:3])
        for fields in FIELDS:
            if fields in passportFields:
                fieldNum += 1
        if fieldNum == 7:
            validPassports += 1
        passportFields = []
        fieldNum = 0
    return(validPassports)

def checkPassportFields(data):
    passportFields = []
    validPassports = 0
    fieldNum = 0
    validFields = 0
    for passport in data:
        for field in passport:
            passportFields.append(field[0:3])
        for fields in FIELDS:
            if fields in passportFields:
                fieldNum += 1
        if fieldNum == 7:
            for field in passport:
                if field[0:3] == 'byr':
                    if len(field[4:]) == 4 and int(field[4:]) >= 1920 and  int(field[4:]) <= 2002:
                        validFields += 1

                elif field[0:3] == 'iyr':
                    if len(field[4:]) == 4 and int(field[4:]) >= 2010 and  int(field[4:]) <= 2020:
                        validFields += 1

                elif field[0:3] == 'eyr':
                    if len(field[4:]) == 4 and int(field[4:]) >= 2020 and  int(field[4:]) <= 2030:
                        validFields += 1

                elif field[0:3] == 'hgt':
                    if field[-2:] == 'cm' and int(field[4:-2]) >= 150 and  int(field[4:-2]) <= 193:
                        validFields += 1
                    elif field[-2:] == 'in' and int(field[4:-2]) >= 59 and  int(field[4:-2]) <= 76:
                        validFields += 1

                elif field[0:3] == 'hcl':
                    counter = 0
                    if field[4] == '#' and len(field[5:]) == 6:
                        for char in field[5:]:
                            if char in CHARS:
                                counter += 1
                        if counter == 6:
                            validFields += 1

                elif field[0:3] == 'ecl':
                    if field[4:] in EYE_COLOURS:
                        validFields += 1
            
                elif field[0:3] == 'pid':
                    counter = 0
                    if len(field[4:]) == 9:
                        for char in field[4:]:
                            if char in DIGITS:
                                counter += 1
                        if counter == 9:
                            validFields += 1

            if validFields == 7:
                validPassports += 1
        passportFields = []
        fieldNum = 0
        validFields = 0
    return(validPassports)

def part1():
    data = loadData()
    validPassports = checkPassport(data)
    print(validPassports)

def part2():
    data = loadData()
    validPassports = checkPassportFields(data)
    print(validPassports)

part1()
part2()