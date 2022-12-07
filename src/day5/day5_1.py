import os
from collections import deque

d_example= {
    "stack_1": deque(['Z','N']),
    "stack_2": deque(['M','C','D']),
    "stack_3": deque(['P'])
}

d = {
    "stack_1": deque(['N','R','G','P']),
    "stack_2": deque(['J','T','B','L','F','G','D','C']),
    "stack_3": deque(['M','S','V']),
    "stack_4": deque(['L','S','R','C','Z','P']),
    "stack_5": deque(['P','S','L','V','C','W','D','Q']),
    "stack_6": deque(['C','T','N','W','D','M','S']),
    "stack_7": deque(['H','D','G','W','P']),
    "stack_8": deque(['Z','L','P','H','S','C','M','V']),
    "stack_9": deque(['R','P','F','L','W','G','Z']),
}

file_path = os.path.join(os.getcwd(), "day5_sample.txt")
with open(file_path,mode='r',encoding='UTF-8') as fp:
    lines = fp.readlines()

for line in lines:
    lst = line.split()
    blocks_to_be_changed=int(lst[1])
    key1, key2 = f"stack_{lst[3]}", f"stack_{lst[5]}"
    for _ in range(blocks_to_be_changed):
        s = d[key1].pop()
        d[key2].append(s)

res = "".join(v.pop() for v in d.values())

print(res)


