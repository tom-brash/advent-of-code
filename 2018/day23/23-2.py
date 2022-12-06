'''
Day 23-2: Optimizing bot placements

Brutally difficult one that I needed an assist on. Here it's essentially an optimization problem,
which isn't trivial. The unlock here is to use an optimization solver: in this case z3.

We can set it up as an optimization problem that first optimizes for the number of bots that
are in range, and second minimizes the distance to the origin (which on this input doesn't end
up mattering).

Of all AoC problems this is the closest I came to just rewriting code, but very cool to learn about 
z3 in this context.
'''

import re
from z3 import *

def main():
    with open('day23/23-1-input.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    nanobots = list(map(parse_bot, input_data))
    nanobots = [((n[0], n[1], n[2]), n[3]) for n in nanobots]

    (x, y, z) = (Int('x'), Int('y'), Int('z'))
    in_ranges = [Int('in_range_' + str(i)) for i in range(len(nanobots))]
    range_count = Int('sum')
    o = Optimize()

    for i in range(len(nanobots)):
        (nx, ny, nz), nrng = nanobots[i]
        o.add(in_ranges[i] == If(zabs(x - nx) + zabs(y - ny) + zabs(z - nz) <= nrng, 1, 0))
    o.add(range_count == sum(in_ranges))
    origin_distance = Int('dist')
    o.add(origin_distance == zabs(x) + zabs(y) + zabs(z))

    h1 = o.maximize(range_count)
    h2 = o.minimize(origin_distance)

    print(o.check())
    print(o.lower(h2))


def parse_bot(s):
    return list(map(int, re.findall(r'\-?\d+', s)))
    

def zabs(x):  # absolute function compatible with z3
    return If(x >=0, x, -x)




if __name__ == '__main__':
    main()