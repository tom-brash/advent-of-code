'''
DAY 13-1: (Intcode) Setting up an arcade machine 

The first part of this problem is straightforward. The intcode provided sets up
a game of what is essentially breakout. Outputs are provided in groups of three 
(x, y, block_type), and we just need to count how many blocks are printed to  
the display (we don't even need to print them)
''' 

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    # read in input as starting memory
    with open('day13/13-1-input.txt','r') as input_file:
        input_contents = input_file.read()
    
    starting_memory = [int(x) for x in input_contents.split(',')]
    
    arcade_cabinet = Intcode_computer(starting_memory, input_queue=[])
    arcade_cabinet.run()
    outputs = arcade_cabinet.output_queue
    blocks = 0
    for i, output in enumerate(outputs):
        if i % 3 == 2:
            if output == 2:
                blocks += 1
    print(blocks)

if __name__ == "__main__":
    main()