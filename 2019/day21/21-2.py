'''
DAY 21-2: (Intcode) Programming a springbot with extra registers

The only difference in part 2 is that we now have 8 registers, so can see more into the future.
This gives us somewhat more strategy, but not as much as might be supposed. 

We can, however, cover one edge case. In particular, we do not want to jump if we will jump
to a platform where another jump is immediately required, and that jump will take the bot into 
a hole. In other words, the bot should not jump in the below scenario:

@## #X##X

The bits marked X are key. If the bot jumps, it will be forced into another jump, which will put it
in a hole. Better to wait a couple of tiles, where a safer jump may be possible (of course, there 
are many possible configurations where there are no paths forward).

The actual programming of this command is a little convoluted with only two writable registers, but the 
logic is just adding this one extra rule.
''' 
import sys
import os
import pprint
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day21/21-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    starting_memory = [int(x) for x in input_data.split(',')]

    springbot = Intcode_computer(memory=starting_memory, input_queue=[])
    
    # instructions to the bot, separated by function
    instructions = ['OR D J',  # if D is solid, jump

                    'OR J T',  # if jumping, set T to True

                    'AND A T',  # if A, B, and C are True, keep T as True
                    'AND B T',
                    'AND C T',

                    'AND J T',  # keep T as True if jumping. Need to reverse T because of limited operations
                    'NOT T T',
                    'AND T J',
                                # NEW COMMANDS FOR PART 2
                    'NOT E T',  # Turn on T if E is a hole
                    'NOT T T',  # Flip T
                    'OR H T',   # As a result, T should be on if E is solid or if H is solid
                    'AND T J',  # If E or H is solid and the bot was jumping anyway, stay jumping
                    'RUN']
    
    # add the instructions as ACII integers
    for i in instructions:
        springbot.add_to_input_queue(to_instruction(i), add_list=True)
    
    springbot.run()
    if springbot.get_last_output(exclude_last=True) > 256:  # if reporting a final answer
        print('Damage to the hull:', springbot.get_last_output(exclude_last=True))
    else:  # if the bot fell, print the last frames of what happened to it
        print_camera_output(springbot.output_queue)


def print_camera_output(output):
    print_string = ''
    for i in output:
        if i != 'halt':
            print_string += chr(i)
    print(print_string)
    return print_string


def to_instruction(s):
    s = to_ascii(s)
    s.append(10)
    return s


def to_ascii(s):
    return [ord(c) for c in s]


if __name__ == "__main__":
    main()