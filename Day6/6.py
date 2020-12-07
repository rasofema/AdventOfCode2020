"""
Each group's answers are separated by a blank line,
and within each group, each person's answers are on
a single line.
For each group, count the number of questions to which
anyone answered "yes". What is the sum of those counts?
"""

QUESTIONS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',\
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',\
             'u', 'v', 'w', 'x', 'y', 'z']

def loadData():
    data = []
    elem = []
    with open("answers.txt") as f:
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

def checkGroupAnswers(data):
    totalAnswers = []
    for group in data:
        currentAnswer = 0
        for question in QUESTIONS:
            for answer in group:
                if question in answer:
                    currentAnswer += 1
                    break
        totalAnswers.append(currentAnswer)
    return totalAnswers

def checkSameGroupAnswers(data):
    totalAnswers = []
    for group in data:
        currentAnswer = 0
        for question in QUESTIONS:
            sameAnswer = 0
            for answer in group:
                if question in answer:
                    sameAnswer += 1
            if sameAnswer == len(group):
                currentAnswer += 1
        totalAnswers.append(currentAnswer)
    return totalAnswers

def part1():
    data = loadData()
    answersPerGroup = checkGroupAnswers(data)
    totalAnswers = 0
    for answer in answersPerGroup:
        totalAnswers += answer
    print(totalAnswers)

def part2():
    data = loadData()
    answersPerGroup = checkSameGroupAnswers(data)
    totalAnswers = 0
    for answer in answersPerGroup:
        totalAnswers += answer
    print(totalAnswers)

part1()
part2()