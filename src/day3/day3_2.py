import os
from string import ascii_lowercase, ascii_uppercase

def main():
    file_path = os.path.join(os.getcwd(), "day3_2.txt")
    with open(file_path,mode='r',encoding='UTF-8') as fp:
        lines = fp.readlines()
    
    res= 0
    alpha_dict = {v:k+1 for k,v in enumerate(ascii_lowercase)}
    for k, v in enumerate(ascii_uppercase):
        alpha_dict[v] = k+27
    for i in range(0, len(lines), 3):
        sub_list1,sub_list2,sub_list3 = lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()
        common_set = set(sub_list1).intersection(set(sub_list2),set(sub_list3))
        for item in common_set:
            res+=alpha_dict[item]
    return res

print(main())