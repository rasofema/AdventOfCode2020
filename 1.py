#find the two entries that sum to 2020 and then multiply those two numbers together

def loadData():
    data = []
    with open("1input.txt") as f:
        data = f.readlines()
    return data

def sum2To2020(data):
    for i in range(len(data)-1):
        for n in range(i+1, len(data)):
            if int(data[i]) + int(data[n]) == 2020:
                print(int(data[i]), int(data[n]))
                return (int(data[i]), int(data[n]))

def sum3To2020(data):
    for i in range(len(data)-1):
        for n in range(i+1, len(data)):
            for m in range(n+1, len(data)):
                if int(data[i]) + int(data[n]) + int(data[m]) == 2020:
                    print(int(data[i]), int(data[n]), int(data[m]))
                    return (int(data[i]), int(data[n]), int(data[m]))

def multiply(entries):
    result =  entries[0] * entries[1]
    return result

def productOf2():
    data = loadData()
    entries = sum2To2020(data)
    result = multiply(entries)
    print(result, "\n\n")

def productOf3():
    data = loadData()
    entries = sum3To2020(data)
    firstMultiply = multiply(entries)
    lastEntry = (firstMultiply, entries[2])
    result = multiply(lastEntry)
    print(result)


productOf2()
productOf3()