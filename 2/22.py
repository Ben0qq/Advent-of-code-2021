file1 = open('input.txt', 'r')
lines = file1.readlines()
forward = 0
depth = 0
aim = 0
for line in lines:
    direction, number = line.split()
    if(direction == 'forward'):
        forward += int(number)
        depth += aim*int(number)
    else:
        if(direction=='down'):
            aim += int(number)
        else:
            aim -= int(number)
print(forward, depth)   
print(forward*depth)                 
        