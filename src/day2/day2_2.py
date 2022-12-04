import os

file_path = os.path.join(os.getcwd(), "day2_2_sample.txt")
with open(file_path,mode='r',encoding='UTF-8') as fp:
    lines = fp.readlines()

combinations = {
    "rock": ['paper', 'scissors'],
    "paper": ['scissors', 'rock'],
    "scissors": ['rock', 'paper']
}

d = {
    'A': "rock", 'B': "paper", 'C': "scissors"
}
val = {'rock': 1, 'paper': 2, 'scissors': 3}

res = 0

for line in lines:
    lst = line.split()
    if lst[1] == 'X':
        add_val = val[combinations[d[lst[0]]][1]]
        res+=add_val
    elif lst[1] == 'Z':
        add_val = val[combinations[d[lst[0]]][0]]
        res+=(6+add_val)
    elif lst[1] == 'Y':
        add_val = val[d[lst[0]]]
        res+=(3+add_val)
print(res)

