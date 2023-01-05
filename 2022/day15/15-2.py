import re
from collections import deque, defaultdict

def main():
    print('\nZeroing in on the beacon...\n')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    t_row = 2000000

    sensors = []
    beacons = set()

    for x in input:
        coords = re.findall(r'-?\d+', x)
        sensors.append(Sensor(coords))

    for i in range(0, 4000000):
        if i % 1000000 == 0:
            if i != 0:
                print(f'Scanned up to record {i}...')

        impossible_ranges = []

        for s in sensors:
            hr = s.md - abs(s.y - i)
            if hr >=0:
                impossible_ranges.append((s.x -hr, s.x + hr))

        cr = []
        for b, e in sorted(impossible_ranges):
            if cr and cr[-1][1] >= b - 1:
                cr[-1][1] = max(cr[-1][1], e)
            else:
                cr.append([b, e])

        if len(cr) <= 1:
            continue
        else:
            print(f'\nBeacon location identified! Beacon is at {cr[0][1] + 1}, {i}')
            print(f'\n(15-2) Tuning frequency: {i + (cr[0][1] + 1) * 4000000}')
            break

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
