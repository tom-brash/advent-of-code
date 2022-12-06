'''
DAY 17-2: (Intcode) Reading in scaffolding pattern from camera input 

The second part involves finding the sequence that appropriately traverses the 
scaffolding and then breaks it into 3 repeatable parts. The actual sequencing
here was done manually, with the resultant functions being passed directly as 
input.
''' 

import sys
import os
import pprint
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day17/17-1-input.txt','r') as input_file:
        input_contents = input_file.read()
    
    initial_memory = [int(x) for x in input_contents.split(',')]
    initial_memory[0] = 2
    
    camera = Intcode_computer(initial_memory, input_queue=[])
    
    fA = [ord(x) for x in 'R,6,L,10,R,10,R,10\n']
    fB = [ord(x) for x in 'L,10,L,12,R,10\n']
    fC = [ord(x) for x in 'R,6,L,12,L,10\n']
    main_queue = [ord(x) for x in 'A,B,A,B,A,C,A,C,B,C\n']

    camera.add_to_input_queue(main_queue, add_list=True)
    camera.add_to_input_queue(fA, add_list=True)
    camera.add_to_input_queue(fB, add_list=True)
    camera.add_to_input_queue(fC, add_list=True)
    
    camera.add_to_input_queue([110, 10], add_list=True)
    
    camera.run()

    print(camera.get_last_output(exclude_last=True)) 


def print_camera_output(output):
    print_string = ''
    for i in output:
        if i != 'halt':
            print_string += chr(i)
    print(print_string)
    return print_string


if __name__ == "__main__":
    main()