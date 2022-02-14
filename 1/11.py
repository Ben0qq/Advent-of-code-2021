file1 = open('input.txt', 'r')
lines = file1.readlines()
count = 0
prevLine = 1000000;
for line in lines:
    if(int(line)>prevLine):
        count +=1
    prevLine = int(line)
print(count)    
        