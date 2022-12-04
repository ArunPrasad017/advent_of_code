import os
# from enum import Enum

# class RPS(Enum):
#     rock = 1
#     paper = 2
#     scissors = 3

# print(RPS.rock.value)

opponent = {'A': 1, 'B': 2, 'C': 3}
user = {'X': 1, 'Y': 2, 'Z': 3}
pts = {'Win':6, 'Draw':3, 'Loss':0}
res = 0

file_path = os.path.join(os.getcwd(), "day2_sample.txt")
with open(file_path,mode='r',encoding='UTF-8') as fp:
    lines = fp.readlines()

for line in lines:
    lst = line.split()
    if (lst[0] == 'A' and lst[1] == 'X') or (lst[0]=='B' and lst[1]=='Y') or (lst[0]=='C' and lst[1]=='Z'):
        res+=(pts['Draw'] + user[lst[1]])
    elif lst[0] == 'A' and lst[1] == 'Y':
        res+=(pts['Win']+ user[lst[1]])
    elif lst[0] == 'A' and lst[1] == 'Z':
        res+=(pts['Loss']+ user[lst[1]])

    elif lst[0] == 'B' and lst[1] == 'Z':
        res+=(pts['Win']+ user[lst[1]])
    elif lst[0] == 'B' and lst[1] == 'X':
        res+=(pts['Loss']+ user[lst[1]])

    elif lst[0] == 'C' and lst[1] == 'X':
        res+=(pts['Win']+ user[lst[1]])
    elif lst[0] == 'C' and lst[1] == 'Y':
        res+=(pts['Loss']+ user[lst[1]])

print(res)
