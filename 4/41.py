from typing import final


file1 = open('input.txt', 'r')
lines = file1.readlines()
bingo_values = lines[0].split(',')
bingo_tables = []
current_table = []
for x in range(2, len(lines)):
    if(lines[x] == '\n'):
        bingo_tables.append(current_table)
        current_table = []
    else:
        current_table.append([(y, False) for y in lines[x].split()])
bingo_row = True
bingo_column = []
winning_table=[]
winning_number = 0
for a in bingo_tables[0]:
            bingo_column.append(True)
for number in bingo_values:
    for x in range(0,len(bingo_tables)):
        for a in range(0,len(bingo_tables[0])):
            bingo_column[a] = True
        for y in range(0,len(bingo_tables[0])):
            bingo_row=True
            for z in range(0,len(bingo_tables[0][0])):
                if bingo_tables[x][y][z][0] == number:
                    bingo_tables[x][y][z] = (bingo_tables[x][y][z][0], True)
                if bingo_tables[x][y][z][1]==False:
                    bingo_row=False
                    bingo_column[z]=False  
            if bingo_row==True:
                break          
        if bingo_row==True or (any(a==True for a in bingo_column)):
            winning_number=number
            winning_table = bingo_tables[x]
            break  
    if bingo_row==True or (any(a==True for a in bingo_column)):
                    break                                                 
print(winning_table) 
false_sum=0
for x in winning_table:
    for y in x:
        if y[1]==False:
            false_sum+=int(y[0])
print(false_sum, winning_number)
print(false_sum*int(winning_number))                      
