'''
DAY 19-2: (Intcode) Finding the first 100x100 square in the tractor beam 

The actal problem here is trivial, but given the way the intcode processor works,
it risks taking significant amounts of time. Eyeballing the pattern from 19-1, it is
possible a grid of 1,000 x 1,000 or bigger is required. As the intcode machine needs to 
be reset and run each time, processing each cell would take substantial time.

Fortunately, while the pattern from 19-1 is not obviously regular, it does have certain
characteristics. In particular, in a given row the beam is made up of contiguous tiles 
only. Further, the beam is never more than 1 tile smaller than the largest width observed
so far, and never 1 tile greater than the previous width. 

This means that while scanning, we can skip most of the start of the row, much of the beam
itself, and then everything after the beam ends. This means that we can scan even very large
grids and get a complete pattern (though we don't print it as the terminal is not large enough).

By observation, when the first square of a given size is found, it will be at the rightmost of the
top row that it exists in. While this may not be perfectly generalizable to all inputs, at worst it 
should give a very narrow search range to test
''' 

import sys
import os
import pprint
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day19/19-1-input.txt','r') as input_file:
        input_contents = input_file.read()
    
    # read in intcode memory
    initial_memory = [int(x) for x in input_contents.split(',')]
        
    current_left = 0  # current leftmost cell of the beam
    max_beam_width = 1  # current maximum beam width observed
    w = 1000
    s = 100  # square of size s x s to find
    y = 4  # start at row 4. By observation, there are empty rows above row 4 that are not helpful
    square_found = False
    while not square_found:
        print_string = '.' * current_left  # keeping track of the current row
        x = current_left
        beam_started = False
        beam_finished = False
        right_edge = None
        while not beam_finished:
            while not beam_started:
                # start at the current 'left' position of the beam and scan until beam is found
                output = determine_beam(initial_memory, [x, y])                
                
                # if beam is found
                if output == '#':
                    beam_started = True
                    print_string += output  # add the found '#'
                    print_string += '#' * max(0, max_beam_width - 2)  # skip over much of the beam itself, recognizing it could be 1 shorter than line above 
                    x += max(1, max_beam_width - 1)
                    break
                
                # otherwise
                x += 1
                current_left += 1
                print_string += output
            
            output = determine_beam(initial_memory, [x, y])
            if output == '#':  # if the beam is still going
                print_string += output
                max_beam_width = max(max_beam_width, print_string.count('#'))
                x += 1  
            else:  # if the beam is finished
                beam_finished = True            
                print_string += '.' * (w - x)  # add the remainder of the string in case we want to print
                right_edge = x - 1  # get the right edge of the beam
                if right_edge > s:  # don't bother checking for the square if the right_edge isn't far enough across (and avoid negative indices)
                    test = determine_beam(initial_memory, [x - s, y + (s - 1)])  # check the bottom left corner of where the square would be
                    if test == '#':  # if the lower right corner is also a #, then a square is found
                        print('Found square of size', s, ' at row', y)
                        square_found = True
                        top_left_cell = (x - s, y)
        print('Row: ', y, '   Max beam width:', max_beam_width, '  Right edge:', right_edge)
        y += 1
    
    print('Final answer: ', top_left_cell[0] * 10000 + top_left_cell[1])
                

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