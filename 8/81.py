from typing import final

file1 = open('input.txt', 'r')
lines = file1.readlines()
decoded_lines =[]
for line in lines:
    decoded_lines.append(line.split('|'))
decoded_lines = [[x[0].split(), x[1].split()] for x in decoded_lines]
count = 0
for line in decoded_lines:
    for value in line[1]:
        if len(value) in (2,3,4,7):
            count+=1
print(count)            
        