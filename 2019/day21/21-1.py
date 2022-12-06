'''
DAY 21-1: (Intcode) Programming a springbot 

The springbot robot operates off springscript, a language with minimal commands and 
only boolean registers. There are 4 read only registers, representing the four spaces in front
of the bot, and whether they have solid ground or not, and two write registers, T and J. If 
J is true after running the program at the current space, the robot will jump.

Only seeing 4 spaces ahead, there is a limit to how intelligent the strategy can be. The strategy
used here is simple:

    - if there is solid ground 4 spaces away, JUMP...
    - unless there is also solid ground 1, 2, and 3 spaces away

There is no need for an instruction to jump if register A is empty, as either we will jump anyway
(if D is solid), or it doesn't matter whether we jump or not (if D is empty)

If there is the decision to land 4 or 5 spots away, it will always be better to land 4 spots away,
since the bot can always move to the next. However, jumping when there is only solid ground ahead
removes the ability to land on the tile 6 tiles away, which calls for the extra instruction. This
does not guarantee safety, but is the best we can do with four registers.
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
                    'WALK']
    
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