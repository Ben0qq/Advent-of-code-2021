from typing import final

file1 = open('input.txt', 'r')
lines = file1.readlines()
fishes = lines[0].split(',')
counts = []
for x in range(0,9):
    counts.append(0)
for x in range(0,len(fishes)):
    print(len(counts), int(fishes[x]))
    counts[int(fishes[x])]+=1
for a in range(0,256):
    temp=counts[0]
    for x in range(0,len(counts)):
        if x<8:    
            counts[x]=counts[x+1]  
        if x==6:
            counts[x]+=temp
        if x==8:
            counts[x]=temp          
sum = 0
for x in range(0,len(counts)):
    sum += counts[x] 
print(sum)            
        