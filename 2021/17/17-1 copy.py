from collections import defaultdict
from collections import deque
import copy
import re


def main():
    with open('17/17.txt', 'r') as open_file:
        input_data = open_file.read()
    
    x1, x2, y1, y2 = [int(x) for x in re.findall(r'\-?\d+', input_data)]
    best_found = 0
    for x in range(x2 + 1):
        for y in range(y1, 1000):
            h = plot_path(x, y, x1, x2, y1, y2)
            if h:
                best_found += 1
    print(best_found)


def plot_path(x, y, x1, x2, y1, y2):
    x_vel = x
    y_vel = y
    xp = yp = 0
    high_point = 0
    while xp < x2 and yp > y1:
        xp += x_vel
        yp += y_vel
        #print(xp, yp)
        if yp > high_point:
            high_point = yp
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
        if xp >= x1 and xp <= x2 and yp >= y1 and yp <= y2:
            return True
    return False


class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()