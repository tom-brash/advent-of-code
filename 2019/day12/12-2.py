'''
DAY 12-2: Finding loops in planetary movements

Here we need to see how many steps it will take to return to an identical position.

Because positions are determinative, then there should be a complete loop. This means that instead
of tracking a list of all known positions, we know that the first duplicated position will be the 
starting position, so we can just search for that.

It is known that the demo problem will take >4 trillion steps, and so using the code for 12-1 and checking
each step will take much too long.

However, we can see each axis operates entirely independently, and so will be on their own loops. We can get the 
answer by calculating the loop length of each axis, and then finding the lowest common multiple.

As we are just working with a single axis at a time, we can do this just using list comprehension for speed
instead of numpy across multiple axes.
''' 

import re
import copy
import math
import pprint

def main():
    with open('day12/12-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    # import data as a list of positions
    planet_data = input_data.split('\n')
    planet_pattern = re.compile(r'\-?[0-9]+')
    planets = {}
    for i, planet in enumerate(planet_data):
        planets[i] = [int(x) for x in planet_pattern.findall(planet)]
    
    # for each axis, find the cycle length
    cycle_length = []
    for axis, name in enumerate(['x', 'y', 'z']):
        axis_starting_pos = []
        for planet in planets.values():
            axis_starting_pos.append(planet[axis])
        axis_pos = copy.deepcopy(axis_starting_pos)
        axis_vels = [0, 0, 0, 0]
        iterations = 0
        while True:
            # update the velocity using list comprehension
            axis_vels = [x + sum(compare(axis_pos[i], y) for j, y in enumerate(axis_pos) if i!=j) for i, x in enumerate(axis_vels)]
            # update the positions using list comprehension
            axis_pos = [x + axis_vels[i] for i, x in enumerate(axis_pos)]
            iterations += 1
            if axis_vels == [0, 0, 0, 0]:    
                if axis_pos == axis_starting_pos:
                    break
        print('Cycle for axis', name, 'will take', iterations, 'iterations')
        cycle_length.append(iterations)

    # find LCM of all three numbers
    print('iterations for planets to return to starting configuration: ', lcm(lcm(cycle_length[0], cycle_length[1]), cycle_length[2]))


# find lowest common multiple
def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)


# compare according to provided rules, but along just one axis for speed
def compare(loc_1, loc_2):
    update = loc_1 - loc_2
    if update > 0:
        update = -1
    elif update < 0:
        update = 1
    return update



if __name__ == "__main__":
    main()