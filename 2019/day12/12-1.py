'''
DAY 12-1: Plotting planetary movements

Here we need to track the movement of planets in a number of steps, assessing how 
gravity will impact them and adjusting their position accordingly.

Numpy helps do the array addition reasonably efficiently, and we do 1,000 steps 
to get the answer
''' 

import re
import copy
import numpy as np
import pprint

def main():
    with open('day12/12-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    # extract planet data from inputs using regex to get the numbers
    planet_data = input_data.split('\n')
    planet_pattern = re.compile(r'\-?[0-9]+')
    planets = {}
    for i, planet in enumerate(planet_data):
        loc = planet_pattern.findall(planet)
        pos = np.array([int(x) for x in loc])
        vel = np.array([0, 0, 0])
        planets[i] = {'pos': pos, 'vel': vel}
    
    # run 1,000 steps
    for i in range(1000):
        planets = step(planets)

    print('Total energy after 1000 steps: ', calculate_energy(planets))

# process a single step
def step(planets):
    # create a copy so that all changes can be made 'simultaneously'
    planet_copy = copy.deepcopy(planets)
    for i in planets:
        for j in planets:
            if i != j:
                # update velocity
                planet_copy[i]['vel'] += compare_planet_locations(planets[i]['pos'], planets[j]['pos'])    
        # update position
        planet_copy[i]['pos'] += planet_copy[i]['vel']
    return planet_copy


# along each axis, return -1 if greater than, 1 if less than
def compare_planet_locations(loc_1, loc_2):
    update = loc_1 - loc_2
    update = np.where(update < 0, 1,
        (np.where(update > 0, -1, 0)))
    return update


# calculate 'potential and kinetic' energy according to rules provided
def calculate_energy(planets):
    total_energy = 0
    for key in planets:
        potential = np.sum(np.absolute(planets[key]['pos']))
        kinetic = np.sum(np.absolute(planets[key]['vel']))
        total_energy += potential * kinetic
    return total_energy


if __name__ == "__main__":
    main()