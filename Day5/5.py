"""
The first 7 characters will either be F or B;
these specify exactly one of the 128 rows on
the plane (numbered 0 through 127). Each letter
tells you which half of a region the given seat
is in. Start with the whole list of rows;
the first letter indicates whether the seat is
in the front (0 through 63) or the back (64 through 127).
The next letter indicates which half of that region the
seat is in, and so on until you're left with exactly one row.

The last three characters will be either L or R; these specify
exactly one of the 8 columns of seats on the plane (numbered 0
through 7). The same process as above proceeds again, this time
with only three steps. L means to keep the lower half, while R
means to keep the upper half.
"""

def loadData():
    data = []
    with open("input.txt") as f:
        data = f.readlines()
    return data

def getSeat(bpass):
    rowMin = 0
    rowMax = 127
    columnMin = 0
    columnMax = 7
    
    # calculate row
    for i in range(6):
        if bpass[i] == 'F':
            rowMax = (rowMax + rowMin) // 2
        elif bpass[i] == 'B':
            rowMin = round((rowMax + rowMin) / 2)
    if bpass[6] == 'F':
        row = rowMin
    elif bpass[6] == 'B':
        row = rowMax

    #calculate column
    for i in range(7, 9):
        if bpass[i] == 'L':
            columnMax = (columnMax + columnMin) // 2
        elif bpass[i] == 'R':
            columnMin = round((columnMax + columnMin) / 2)
    if bpass[9] == 'L':
        column = columnMin
    elif bpass[9] == 'R':
        column = columnMax
    
    return (row, column)


def part1():
    data = loadData()
    maxSeatId = 0
    for bpass in data:
        seat = getSeat(bpass)
        seatId = seat[0] * 8 + seat[1]
        if seatId > maxSeatId:
            maxSeatId = seatId
    print(maxSeatId)

def part2():
    data = loadData()
    seats = []
    for bpass in data:
        seats.append(getSeat(bpass))
    for row in range(2, 102):
        for column in range(0, 8):
            if (row, column) not in seats:
                missingSeatId = row * 8 + column
    print(missingSeatId)

part2()