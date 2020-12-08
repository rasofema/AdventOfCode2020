"""
How many bag colors can eventually contain at least one shiny gold bag?

How many individual bags are required inside your single shiny gold bag?
"""

def loadData():
    data = []
    with open("rules.txt") as f:
        info = f.readlines()
        for line in info:
            lineList = line.split(" contain ")
            data.append(lineList)
    return data

def loadDictionary():
    data = {}
    with open("rules.txt") as f:
        info = f.readlines()
        for line in info:
            lineList = line.split(" contain ")
            data.update({lineList[0][:-5]: lineList[1][:-2]})
    return data

def checkBag(data, bagColours):
    approvedBags = set()
    listOfBags = []
    for bag in data:
        for bagColour in bagColours:
            if bagColour in bag[1]:
                approvedBags.add(bag[0][:-5])
                listOfBags.append(bag[0][:-5])
    if len(listOfBags) > 0:
        for item in checkBag(data, listOfBags):
            approvedBags.add(item)
    return approvedBags

def insideBag(data, bagColour):
    counter = 0
    bagsInside = data[bagColour]
    if bagsInside == 'no other bags':
        counter += 0
    else:
        otherBags = bagsInside.split(", ")
        for bag in otherBags:
            if bag[-2:] == 'gs':
                counter += int(bag[0]) + int(bag[0]) * insideBag(data, bag[2:-5])
            else:
                counter += int(bag[0]) + insideBag(data, bag[2:-4])
    return counter


def part1():
    data = loadData()
    goldInData = checkBag(data, ["shiny gold"])
    print(len(goldInData))

def part2():
    data = loadDictionary()
    bagsInGold = insideBag(data, "shiny gold")
    print(bagsInGold)

part1()
part2()