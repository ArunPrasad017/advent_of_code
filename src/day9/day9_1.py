# Ref - https://replit.com/@skybadger/AOC2022-Day09#main.py
import os

def follower(head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    old_x, old_y = tail
    if (abs(x_diff) == 2) and (abs(y_diff) == 2):
        tail[0] += x_diff//2
        tail[1] += y_diff//2
    elif abs(x_diff) == 2:
        tail[0] += x_diff//2
        tail[1] = head[1]
    elif abs(y_diff) == 2:
        tail[1] += y_diff//2
        tail[0] = head[0]
    new_x, new_y = tail
    return ((new_x != old_x) or (new_y != old_y))


def main():
    file_path = os.path.join(os.getcwd(), "day9.txt")
    with open(file_path,mode='r',encoding='UTF-8') as fp:
        lines = fp.readlines()
    d = {line.strip().split()[0]: int(line.strip().split()[1]) for line in lines}
    max_len = max(d.values())
    # m1 = [['.' for _ in range(max_len)] for _ in range(max_len)]
    # m2 = [['.' for _ in range(max_len)] for _ in range(max_len)]

    rope = [[0,0], [0,0]]
    head, tail = rope[0], rope[-1]
    visits = {str(tail)}
    for line in lines:
        k,v = line.strip().split()[0], int(line.strip().split()[1])
        for _ in range(v):
            if k == 'D':
                head[1]-=1
                moved = True
            elif k == 'L':
                head[0]-=1
                moved = True
            elif k == 'R':
                head[0]+=1
                moved = True
            elif k == 'U':
                head[1]+=1
                moved = True
            for n in range(1, len(rope)):
                if moved:
                    moved = follower(rope[n-1],rope[n])
            if moved:
                visits.add(str(rope[-1]))

    return(len(visits))

print(main())