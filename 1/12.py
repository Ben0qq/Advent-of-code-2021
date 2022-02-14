file1 = open('input.txt', 'r')
lines = file1.readlines()
count = 0
prevSum = 1000000;
a=0
b=0
c=0
for line in lines:
    if a!=0 and b!=0 and c!=0 and a+b+c<b+c+int(line):
        count +=1
    a=b
    b=c    
    c = int(line)
print(count)    
        