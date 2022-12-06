'''
DAY 13-1: Finding the next bus

The first problem is relatively trivial: we simply go through the different shuttles
and use modulo operations to see when the next shuttle is, returning the minimum time
'''

import numpy as np

def main():
    with open('day13/13-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    input_lines = input_data.split('\n')
    current_time = int(input_lines[0])
    available_buses = input_lines[1].split(',')

    available_buses = [int(x) for x in available_buses if x != 'x']

    min_time = np.inf
    min_next_bus = None 
    for bus in available_buses:
        next_bus = bus - (current_time % bus)
        if next_bus < min_time:
            min_time = next_bus
            min_next_bus = bus
    
    print(min_time * min_next_bus)


if __name__ == "__main__":
    main()