import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    t_row = -785477

    sensors = []
    beacons = set()

    for x in input:
        coords = re.findall(r'-?\d+', x)
        sensors.append(Sensor(coords))
        beacons.add((int(coords[2]), int(coords[3])))

    impossible_ranges = []

    for s in sensors:
        hr = s.md - abs(s.y - t_row)
        if hr >= 0:
            print(f'Sensor as {s.pos} and md {s.md} has range {(s.x - hr), (s.x + hr)}')
            impossible_ranges.append((s.x -hr, s.x + hr))

    cr = []
    for b, e in sorted(impossible_ranges):
        if cr and cr[-1][1] >= b - 1:
            cr[-1][1] = max(cr[-1][1], e)
        else:
            cr.append([b, e])
    print(impossible_ranges)
    print(cr)

    total = 0 
    actual_beacons = 0
    for r in cr:
        for b in beacons:
            if b[1] != t_row:
                continue
            if b[0] in range(r[0], r[1] + 1):
                actual_beacons += 1
        total += (r[1] - r[0]) + 1

    print(f'Final answer: {total-actual_beacons}')

class Sensor:
    def __init__(self, c):
        c = [int(x) for x in c]
        self.x = c[0]
        self.y = c[1]
        self.pos = (self.x, self.y)
        self.md = get_md((c[0], c[1]), (c[2], c[3]))


def get_md(p1, p2):
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) 

if __name__ == "__main__":
    main()
