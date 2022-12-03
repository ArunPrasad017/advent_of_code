import os
from heapq import nlargest

def func():
    d,ctr = {}, 0
    file_path = os.path.join(os.getcwd(), "day1_sample.txt")
    with open(file_path, 'r', encoding='UTF-8') as fp:
        lines = fp.readlines()

    for line in lines:
        if line.strip() == "":
            ctr+=1
            d[str(ctr)] = 0
        elif str(ctr) in d:
            d[str(ctr)]+=int(line)
        else:
            d[str(ctr)]=int(line)
    max_lst = nlargest(3,d,key=d.get)
    return sum(d[item] for item in max_lst)
        
def main():
    print(func())

main()