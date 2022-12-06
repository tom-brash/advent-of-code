'''
DAY 2-1: (Intcode) Restoring gravity assist

In this version, using a completed Intcode Computer, it is as trivial as loading the 
code, modifying the specified steps, adn creating an intcode computer object to
process it
''' 

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from intcode import Intcode_computer

def main():
    with open('day2/2-1-input.txt', 'r') as input_file:
        input_string = input_file.read()

    init_memory = input_string.split(',')
    init_memory = [int(i) for i in init_memory]

    # hard code required by question
    init_memory[1] = 12
    init_memory[2] = 2

    comp = Intcode_computer(init_memory)
    comp.run()

    print('Full sequence:')
    comp.pprint()
    print('\nInteger at position 0:', comp.memory[0])


if __name__ == '__main__':
    main()