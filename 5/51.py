from typing import final

file1 = open('input.txt', 'r')
lines = file1.readlines()
board = [[0 for x in range(1000)] for y in range(1000)]
for x in range(0, 1000):
    for y in range(0, 1000):
        board[x][y] = 0
coordinates = []
for line in lines:
    coordinates.append({
        "xStart": int(line.split()[0].split(',')[0]),
        "yStart": int(line.split()[0].split(',')[1]),
        "xEnd": int(line.split()[2].split(',')[0]),
        "yEnd": int(line.split()[2].split(',')[1])
    })
for line in coordinates:
    if(line["xStart"] == line['xEnd'] and line["yStart"] != line['yEnd']):
        if line["yStart"]<line["yEnd"]:
            for x in range(line["yStart"], line['yEnd']+1):
                board[line["xStart"]][x] += 1
        else:
            for x in range(line["yEnd"], line['yStart']+1):
                board[line["xStart"]][x] += 1        
    elif(line["yStart"] == line['yEnd'] and line["xStart"] != line['xEnd']):
        if line["xStart"]<line["xEnd"]:
            for x in range(line["xStart"], line['xEnd']+1):
                board[x][line["yStart"]] += 1
        else:
            for x in range(line["xEnd"], line['xStart']+1):
                board[x][line["yStart"]] += 1       
winningPoints = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        if board[x][y] > 1:
            winningPoints += 1
print(winningPoints)            
