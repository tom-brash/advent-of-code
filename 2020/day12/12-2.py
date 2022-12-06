'''
DAY 12-2: Process turtle instructions for ferry by a waypoint

Keeping track of the waypoint can be done similarly to the ferry in the previous problem.
We mostly need to make adjustments for turning (which now rotates around the origin, or
the ferry), and the fact that the only way the boat actually moves is by the 'forward' 
instruction.

By using numpy we can do multiplication of vectors more easily, as the forward instruction
will always move the boat by a multiple of the current waypoint vector
'''

import numpy as np

def main():
    with open('day12/12-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    instructions = input_data.split('\n')

    location = np.array([0, 0])
    waypoint_vector = np.array([10, 1])

    for i, instruction in enumerate(instructions):
        location, waypoint_vector = turtle_instruct(instruction, location, waypoint_vector)
        print(str(i) + ': ' + str(location) + ' with a waypoint vector of ' + str(waypoint_vector))
    
    print(location)
    print(waypoint_vector)
    print(abs(location[0]) + abs(location[1]))


def turtle_instruct(instruction, location, waypoint_vector):
    direction = instruction[0]
    value = int(instruction[1:])

    if direction == 'N':
        waypoint_vector[1] += value
    if direction == 'S':
        waypoint_vector[1] -= value
    if direction == 'E':
        waypoint_vector[0] += value
    if direction == 'W':
        waypoint_vector[0] -= value
    
    if direction == 'F':
        location = location + waypoint_vector * value
    
    if direction == 'R':
        direction = 'L'
        value = 360 - value

    if direction == 'L':
        if value == 90:
            new_vec = np.array([-waypoint_vector[1], waypoint_vector[0]])
            waypoint_vector = new_vec
        if value == 180:
            waypoint_vector = -1 * waypoint_vector
        if value == 270:
            new_vec = np.array([waypoint_vector[1], -waypoint_vector[0]])
            waypoint_vector = new_vec
    
    
    return location, waypoint_vector
    

def degree_to_direction(clockwise_degree_from_east):
    if clockwise_degree_from_east == 0:
        return 'E'
    if clockwise_degree_from_east == 90:
        return 'N'
    if clockwise_degree_from_east == 180:
        return 'W'
    if clockwise_degree_from_east == 270:
        return 'S'

if __name__ == "__main__":
    main()