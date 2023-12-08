import re
from math import lcm

def main():
    print('==== Day 8 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    instructions = [0 if x == 'L' else 1 for x in lines[0]]
    s_mapping = lines[2:]
    
    mapping = {}

    for m in s_mapping:
        letters = re.findall(r'[A-Z]+', m)
        mapping[letters[0]] = (letters[1], letters[2])

    locs = [l for l in mapping.keys() if l[2] == 'A' ]
    length = len(instructions)
    
    loc_cycles = {}

    for start_loc in locs:
        loc = start_loc
        cycle_found = False
        endpoints = []
        i = 0
        while not cycle_found:
            loc = mapping[loc][instructions[i % length]]
            i += 1
            if loc[-1] == 'Z':
                endpoints.append(i)
                if len(endpoints) < 3:
                    continue
                if endpoints[-1] - endpoints[-2] == endpoints[-2] - endpoints[-3]:
                    cycle_found = True
                    loc_cycles[start_loc] = endpoints[-1] - endpoints[-2]

    print(lcm(*list(loc_cycles.values())))


if __name__ == "__main__":
	main()
