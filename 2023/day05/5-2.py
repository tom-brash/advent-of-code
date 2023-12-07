import re
from pprint import pprint
import copy

def find_next(v, rules):
    mins = [r[1] for r in rules if r[1] > v]
    if len(mins) == 0:
        return False
    target = min(mins)
    for r in rules:
        if r[1] == target:
            return r

def map_range(m, r):
    unmapped = r[1]
    start_u = r[0]
    new_ranges = []
    while unmapped > 0:
        rule_found = False
        for rule in m:
            if start_u in range(rule[1], rule[1] + rule[2]):
                rule_found = True
                overlap = rule[1] + rule[2] - start_u
                new_ranges.append((rule[0] + start_u - rule[1], min(overlap, unmapped)))
                unmapped -= overlap
                start_u += overlap
                break
        if not rule_found:
            r = find_next(start_u, m)
            if not r:
                new_ranges.append((start_u, unmapped))
                unmapped = 0
            else:
                overlap = r[1] - start_u
                new_ranges.append((start_u, min(overlap, unmapped)))
                start_u += overlap
                unmapped -= overlap
    return new_ranges


def main():
    print('==== Day 5 ====')
    with open('input', 'r') as open_file:
	    blocks = open_file.read().strip().split('\n\n')

    BIG = 9999999999999999
    map_order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity']
    seed_ranges = [tuple([int(y) for y in x.group(0).split()]) for x in re.finditer(r'\d+\ \d+', blocks[0])]

    maps = {}

    for m in blocks[1:]:
        name = m.split('-')[0]
        maps[name] = []
        for line in m.split('\n')[1:]:
            maps[name].append(tuple([int(x) for x in line.split()]))

    for m in map_order:
        new_ranges = []
        for r in seed_ranges:
            new_ranges.extend(map_range(maps[m], r))
        seed_ranges = copy.deepcopy(new_ranges)

    lowest = BIG
    for r in seed_ranges:
        if r[0] < lowest:
            lowest = r[0]

    print(lowest)
    

if __name__ == "__main__":
	main()
