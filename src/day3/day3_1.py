import os
from string import ascii_lowercase, ascii_uppercase

def main():
    file_path = os.path.join(os.getcwd(), "day3_1.txt")
    with open(file_path,mode='r',encoding='UTF-8') as fp:
        lines = fp.readlines()
    
    res, common = 0, []
    alpha_dict = {v:k+1 for k,v in enumerate(ascii_lowercase)}
    for k, v in enumerate(ascii_uppercase):
        alpha_dict[v] = k+27
    for line in lines:
        line = line.strip()
        n = len(line)
        split1, split2 = list(line)[:n//2], list(line)[n//2:]
        common_set = set(split1).intersection(set(split2))
        for item in common_set:
            common.append(item)
            res+=(alpha_dict[item])
    return res

print(main())