import os

def coordinates(lines):
    coordinates = []
    for line in lines:
        line = line.strip()
        trees = []
        for l in line:
            trees.append(int(l))
        coordinates.append(trees)
    return coordinates

def search_horizontal(start,end,step,row,visible):
    highest = -1
    for i in range(start, end, step):
        if coordinates[row][i]>highest:
            key = f"{row}|{i}"
            if key not in visible:
                visible[key] = coordinates[row][i]
            highest = coordinates[row][i]

def search_vertical(start,end,step,col,visible):
    highest = -1
    for i in range(start, end, step):
        if coordinates[i][col]>highest:
            key = f"{i}|{col}"
            if key not in visible:
                visible[key] = coordinates[i][col]
            highest = coordinates[i][col]

file_path = os.path.join(os.getcwd(), "day8_1.txt")
with open(file_path,mode='r',encoding='UTF-8') as fp:
    lines = fp.readlines()

coordinates = coordinates(lines)
visible = {}

for y in range(len(coordinates)):
    search_horizontal(0, len(coordinates[0]), 1, y, visible)
    search_horizontal(len(coordinates[0])-1, -1, -1, y, visible)

for y in range(len(coordinates[0])):
    search_vertical(0, len(coordinates[0]), 1, y, visible)
    search_vertical(len(coordinates[0])-1, -1, -1, y, visible)

print(len(visible))