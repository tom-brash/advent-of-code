'''
DAY 19-1: (Intcode) Determining tractor beam effective zone 

The first part uses an intcode computer to assess whether a tractor beam is active
at a given coordinate. By scanning a 100 x 100 area, we can build a map of exactly
where the pattern is active, which also gives us information as to how to tackle
the second part through observation.

Unlike past intcode machines, this one does not keep looping and providing output values:
it gives a single output and then halts, meaning it needs to be reset before providing 
another output. Nonetheless, this problem is trivial with a working intcode processor.

While the optimizations from part 2 could be applied here to dramatically cut down on the 
speed, it isn't really necessary 
''' 

import sys
import os
import pprint
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day19/19-1-input.txt','r') as input_file:
        input_contents = input_file.read()
    
    initial_memory = [int(x) for x in input_contents.split(',')]
    total = 0
    for y in range(50):
        print_string = ''
        for x in range(50):
            output = determine_beam(initial_memory, [x, y])
            print_string += output
            if output == '#':
                total += 1
        print(print_string)
    print('Total:', total)
    

def determine_beam(memory, location):
    tractor_robot = Intcode_computer(memory, input_queue=location)
    tractor_robot.run()
    output = tractor_robot.get_last_output(exclude_last=True)
    if output == 1:
        return '#'
    else:
        return '.'

if __name__ == "__main__":
    main()