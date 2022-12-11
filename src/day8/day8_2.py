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

file_path = os.path.join(os.getcwd(), "day8_2.txt")
with open(file_path,mode='r',encoding='UTF-8') as fp:
    lines = fp.readlines()

coordinates = coordinates(lines)
highest_scenic_score = 0

for y, row in enumerate(coordinates):
    for x, tree in enumerate(coordinates[y]):
        scenic_value_in_all_directions = [0, 0, 0, 0]

        for u in range(y - 1, -1, -1):
            scenic_value_in_all_directions[0] += 1
            if coordinates[u][x] >= coordinates[y][x]:
                break

        for l in range(x - 1, - 1, -1):
            scenic_value_in_all_directions[1] += 1
            if coordinates[y][l] >= coordinates[y][x]:
                break

        for r in range(x + 1, len(coordinates[y])):
            scenic_value_in_all_directions[2] += 1
            if coordinates[y][r] >= coordinates[y][x]:
                break

        for d in range(y + 1, len(coordinates)):
            scenic_value_in_all_directions[3] += 1
            if coordinates[d][x] >= coordinates[y][x]:
                break

        current_scenic_value = scenic_value_in_all_directions[0] * scenic_value_in_all_directions[1] * \
scenic_value_in_all_directions[2] * scenic_value_in_all_directions[3]

        if current_scenic_value > highest_scenic_score:
            highest_scenic_score = current_scenic_value

print(f"Highest scenic score {highest_scenic_score}")