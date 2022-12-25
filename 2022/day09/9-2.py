import re
from collections import deque, defaultdict

def main():
    print('\nThe rope snapped! Quickly simulating rope end locations to avoid!')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    num_knots = 9
    knots = {-1: (0, 0)}
    tracking = {}
    for k in range(num_knots):
        knots[k] = (0, 0)
        tracking[k] = set()

    for x in input:
        d, n = x.split(' ')
        n = int(n)
        for i in range(n):
            knots[-1] = move_head(knots[-1], d)
            for k in range(num_knots):
                knots[k] = move_tail(knots[k], knots[k-1])
                tracking[k].add(knots[k])

    print("\n(9-2) Spots visited by the final tail knot: ", len(tracking[num_knots - 1]))

def move_head(h, d):
    x, y = h
    if d == "R":
        x += 1
    elif d == 'L':
        x -= 1
    elif d == 'U':
        y += 1
    elif d == 'D':
        y -= 1
    return (x, y)

def move_tail(t, h):
    tx, ty = t
    hx, hy = h
    if abs(tx - hx) <= 1 and abs(ty - hy) <= 1:
        return t
    elif tx == hx:
        ty = hy - (hy - ty) // 2
    elif ty == hy:
        tx = hx - (hx - tx) // 2
    elif abs(tx- hx) == 2 and abs(ty - hy) == 2:
        tx = hx - (hx - tx) // 2
        ty = hy - (hy - ty) // 2
    elif abs(tx - hx) == 2:
        tx = hx - (hx - tx) // 2
        ty = hy
    elif abs(ty - hy) == 2:
        ty = hy - (hy - ty) // 2
        tx = hx
    return (tx, ty)
        
    
if __name__ == "__main__":
    main()
