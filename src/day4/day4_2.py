import os

def main():
    file_path = os.path.join(os.getcwd(), "day4_sample.txt")
    with open(file_path,mode='r',encoding='UTF-8') as fp:
        lines = fp.readlines()
    counter = 0
    for line in lines:
        lst_temp=line.split(',')
        s1,s2 = (lst_temp[0]).split('-'), (lst_temp[1]).split('-')
        l1 = list(range(int(s1[0]), int(s1[1])+1))
        l2 = list(range(int(s2[0]), int(s2[1])+1))
        if len(l1)>len(l2):
            l1,l2 = l2,l1
        for item in l1:
            if item in l2:
                counter+=1
                break
    return counter

print(main())