from typing import final

file1 = open('input.txt', 'r')
lines = file1.readlines()
decoded_lines =[]
for line in lines:
    decoded_lines.append(line.split('|'))
decoded_lines = [[x[0].split(), x[1].split()] for x in decoded_lines]
count = 0
translation={
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g'
}
decode={
    'abcdef':'0',
    'bc':'1',
    'abdeg':'2',
    'abcdg':'3',
    'bcfg':'4',
    'acdfg':'5',
    'acdefg':'6',
    'abc':'7',
    'abcdefg':'8',
    'abcdfg':'9'
    
}
for line in range(0,len(decoded_lines)):
    coding=[]
    for i in range(0,7):
        coding.append(0)
    one = [i for i in decoded_lines[line][0] if len(i)==2][0]
    seven = [i for i in decoded_lines[line][0] if len(i)==3][0]
    four = [i for i in decoded_lines[line][0] if len(i)==4][0]
    for i in seven:
        if i not in one:
            coding[0]=i
    fg=''
    for i in four:
        if i not in one:
            fg+=i
    zero = [i for i in decoded_lines[line][0] if len(i)==6 and (fg[0] not in i or fg[1] not in i)][0]
    for i in fg:
        if i not in zero:
            coding[6]=i
        else:
            coding[5]=i  
    six = [i for i in decoded_lines[line][0] if len(i)==6 and (one[0] not in i or one[1] not in i)][0]
    for i in one:
        if i not in six:
            coding[1]=i
        else:
            coding[2]=i 
    eight = [i for i in decoded_lines[line][0] if len(i)==7][0]   
    de=''
    for i in eight:
        if i not in four+coding[0]:
            de+=i        
    nine = [i for i in decoded_lines[line][0] if len(i)==6 and (de[0] not in i or de[1] not in i)][0]
    for i in de:
        if i not in nine:
            coding[4]=i
        else:
            coding[3]=i       
    word=''     
    for digit in decoded_lines[line][1]:
        digit_list = list(digit)
        for x in range(0,len(digit_list)):
            digit_list[x] = translation[coding.index(digit_list[x])]
        digit_list.sort()
        digit="".join(digit_list)
        word+= decode[digit] 
    count+=int(word)                      
print(count)            
        