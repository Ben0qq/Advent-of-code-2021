from typing import final

file1 = open('input.txt', 'r')
lines = file1.readlines()
lines = [list(x) for x in lines]
for x in range(0, len(lines)):
    lines[x].pop()
    for y in range(0, len(lines[0])):
        lines[x][y] = int(lines[x][y])
lowPoints=[]
for x in range(0, len(lines)):
    for y in range(0, len(lines[0])):
        isLow = True
        if x > 0:
            if lines[x-1][y] <= lines[x][y]:
                isLow = False
        if y > 0:
            if lines[x][y-1] <= lines[x][y]:
                isLow = False
        if x < len(lines)-1:
            if lines[x+1][y] <= lines[x][y]:
                isLow = False
        if y < len(lines[0])-1:
            if lines[x][y+1] <= lines[x][y]:
                isLow = False
        if isLow == True:
            lowPoints.append([x,y])
print(sum)
