import re
from collections import deque, defaultdict

def main():
    print('====Day 9====')
    print('Encountered a rope bridge!')
    print('Modelling rope physics to distract from potential doom...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')
    
    h = (0, 0)
    t = (0, 0)
    visited = set()

    for x in input:
        d, n = x.split(' ')
        n = int(n)
        for i in range(n):
            h = move_head(h, d)
            t = move_tail(t, h)
            visited.add(t)

    print("\n(9-1) Hypothetical number of spots visited by the rope 'tail': ", len(visited))

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
    elif abs(tx - hx) == 2:
        tx = hx - (hx - tx) // 2
        ty = hy
    elif abs(ty - hy) == 2:
        ty = hy - (hy - ty) // 2
        tx = hx

    return (tx, ty)
        
    
if __name__ == "__main__":
    main()
