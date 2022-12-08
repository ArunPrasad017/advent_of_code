import os

def main():
    file_path = os.path.join(os.getcwd(), "day6.txt")
    with open(file_path,mode='r',encoding='UTF-8') as fp:
        lines = fp.read()

    lst = list(lines)
    for i in range(len(lst)-13):
        if len(lst[i:i+14]) == len(set(lst[i:i+14])):
            return (i+14)

print(main())