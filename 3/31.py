from typing import final


file1 = open('input.txt', 'r')
lines = file1.readlines()
listOfCounts = []
for x in lines[0]:
    if x!= '\n':
        listOfCounts.append(0)
for line in lines:
    for x in range(0, len(line)):
        if line[x] == '1':
            listOfCounts[x]+=1
finalString = ''            
for x in range(0, len(listOfCounts)):
        if listOfCounts[x] >len(lines)//2:
            finalString+='1'
        else:
            finalString+='0'               
print(finalString)
print(int('1111111111111',2)-int(finalString,2))
print(int(finalString,2)*(int('111111111111',2)-int(finalString,2)))
        