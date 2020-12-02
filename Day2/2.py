"""
Each line gives the password policy and then the password.

The password policy indicates the lowest and highest number of
times a given letter must appear for the password to be valid.

For example, 1-3 a means that the password must contain a at
least 1 time and at most 3 times.

How many passwords are valid according to their policies?
"""

"""
Each policy actually describes two positions in the password,
where 1 means the first character, 2 means the second character, and so on.

(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)

Exactly one of these positions must contain the given letter.

How many passwords are valid according to the new interpretation of the policies?
"""

def loadData():
    data = []
    info = []
    with open("2input.txt") as f:
        data = f.readlines()
    for item in data:
        elem = item.split()

        elem[0] = elem[0].split('-')
        num = (int(elem[0][0]), int(elem[0][1]))

        elem[1] = elem[1][:-1]

        info.append([num, elem[1], elem[2]])
    return info

def isValidRange(pwd):
    frequence = 0
    for char in pwd[2]:
        if char == pwd[1]:
            frequence += 1
    
    if pwd[0][0] <= frequence and pwd[0][1] >= frequence:
        return 1
    else:
        return 0

def isValidPosition(pwd):
    frequence = 0
    
    if pwd[2][pwd[0][0] - 1] == pwd[1]:
        frequence += 1
    if pwd[2][pwd[0][1] - 1] == pwd[1]:
        frequence += 1

    if frequence == 1:
        return 1
    else:
        return 0

def policy1():
    data = loadData()
    totalValid = 0
    for pwd in data:
        totalValid += isValidRange(pwd)
    print(totalValid)

def policy2():
    data = loadData()
    totalValid = 0
    for pwd in data:
        totalValid += isValidPosition(pwd)
    print(totalValid)

policy1()
policy2()