import os
def main():
    file_path = os.path.join(os.getcwd(), "day10_1.txt")
    with open(file_path,mode='r',encoding='UTF-8') as fp:
        lines = [s.strip() for s in fp.readlines()]
    
    ctr, res = 0, 1
    lst_checkpoint = {}

    for line in lines:
        if line.split()[0] == 'addx':
            ctr+=1
            lst_checkpoint[ctr] = res*ctr
            ctr+=1
            lst_checkpoint[ctr] = res*ctr
            res+=int(line.split()[1])
        elif line.split()[0] == 'noop':
            ctr+=1
            lst_checkpoint[ctr] = res*ctr
    return sum(lst_checkpoint.get(i, 0) for i in range(20, 221, 40))

print(main())