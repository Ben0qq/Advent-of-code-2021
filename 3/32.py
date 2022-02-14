from typing import final


file1 = open('input.txt', 'r')
lines = file1.readlines()      
count1=0
count0=0
currentSign=''
for x in range(0,len(lines[0])-1):
    for line in lines:
        if line[x]=='1':
            count1+=1
        else:
            count0+=1  
    if(count1>count0) or (count1==count0):
        currentSign = '1'
    else:
        currentSign = '0'  
    count1=0
    count0=0    
    y=0   
    while y <len(lines):
        if lines[y][x] != currentSign:
            lines.pop(y)
            y-=1
        y+=1    
    if(len(lines)==1):
        break    
n1=lines[0]     
print(lines)
file1 = open('input.txt', 'r')
lines = file1.readlines()
for x in range(0,len(lines[0])-1):
    for line in lines:
        if line[x]=='1':
            count1+=1
        else:
            count0+=1          
    if(count0<count1) or (count1==count0):
        currentSign = '0'
    else:
        currentSign = '1'  
    count1=0
    count0=0 
    y=0   
    while y <len(lines):
        if lines[y][x] != currentSign:
            lines.pop(y)
            y-=1
        y+=1  
    if(len(lines)==1):
        break       
n2=lines[0]
print(int(n1,2))  
print(int(n1,2)*int(n2,2))          