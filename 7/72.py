from typing import final
import math

file1 = open('input.txt', 'r')
lines = file1.readlines()
crabs=[int(x) for x in lines[0].split(',')]
maks = max(crabs)
sum=0
best_sum=1000000000
for x in range (0, maks+1):
    sum=0
    for crab in crabs:
        distance = int(math.fabs(crab-x))
        sum+=((2+(distance-1))/2)*distance
    if sum<best_sum:
        best_sum=sum
print(best_sum)        