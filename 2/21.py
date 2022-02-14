file1 = open('input.txt', 'r')
lines = file1.readlines()
forward = 0
depth = 0
for line in lines:
    direction, number = line.split()
    if(direction == 'forward'):
        forward += int(number)
    else:
        if(direction=='down'):
            depth += int(number)
        else:
            depth -= int(number)
print(forward, depth)   
print(forward*depth)                 
        