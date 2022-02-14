from typing import final

file1 = open('input.txt', 'r')
lines = file1.readlines()
fishes = lines[0].split(',')
for x in range(0,len(fishes)):
    fishes[x] = int(fishes[x])
for a in range(0,80):
    for x in range(0,len(fishes)):
        if fishes[x]==0:
            fishes[x] =6
            fishes.append(8) 
        elif fishes[x]>0:
            fishes[x]-=1
print(len(fishes))            
        