import re
from pprint import pprint

def map_val(rules, val):
    for rule in rules:
        if val in range(rule[1], rule[1] + rule[2]):
            return rule[0] + val - rule[1]
    return val

def main():
    print('==== Day 2 ====')
    with open('input', 'r') as open_file:
	    blocks = open_file.read().strip().split('\n\n')

    map_order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity']
    seeds = [int(x.group(0)) for x in re.finditer(r'\d+', blocks[0])]
    print(seeds)

    maps = {}

    for m in blocks[1:]:
        name = m.split('-')[0]
        maps[name] = []
        for line in m.split('\n')[1:]:
            maps[name].append(tuple([int(x) for x in line.split()]))

    lowest = 9999999999999
    for seed in seeds:
        val = seed
        for m in map_order:
            val = map_val(maps[m], val)
        if val < lowest:
            lowest = val

    print(lowest)

    

if __name__ == "__main__":
	main()
