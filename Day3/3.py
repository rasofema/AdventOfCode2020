"""
Open squares: (.)
Trees: (#)

Due to something you read about once involving
arboreal genetics and biome stability, the same
pattern repeats to the right many times.

From your starting position at the top-left,
check the position that is right 3 and down 1.
Then, check the position that is right 3 and
down 1 from there, and so on until you go past
the bottom of the map.

Starting at the top-left corner of your map and
following a slope of right 3 and down 1, how many
trees would you encounter?


Time to check the rest of the slopes.
Determine the number of trees you would
encounter if, for each of the following slopes,
you start at the top-left corner and traverse the
map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

What do you get if you multiply together the number of trees
encountered on each of the listed slopes?
"""

def loadData():
    data = []
    with open("map.txt") as f:
        data = f.readlines()
    return data

def checkPath(data, rowOffset, columnOffset):
    column = 0
    treeNum = 0
    for row in range(rowOffset, len(data), rowOffset):
        column += columnOffset
        char = data[row][column%31]
        if char == '#':
            treeNum += 1
    return treeNum

def part1():
    data = loadData()
    treeNum = checkPath(data, 1, 3)
    print(treeNum)

def part2():
    data = loadData()
    path1 = checkPath(data, 1, 1)
    path2 = checkPath(data, 1, 3)
    path3 = checkPath(data, 1, 5)
    path4 = checkPath(data, 1, 7)
    path5 = checkPath(data, 2, 1)
    print(path1*path2*path3*path4*path5)

part1()
part2()