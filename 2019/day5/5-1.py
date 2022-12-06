'''
DAY 5-1: (Intcode) Running diagnostic tests

In this version, using a completed Intcode Computer, it is as trivial as running
the code and entering the diagnostic code '1'
''' 

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from intcode import Intcode_computer

def main():
    with open('day5/5-1-input.txt','r') as input_file:
        input_contents = input_file.read()

    init_memory = [int(i) for i in input_contents.split(',')]
    
    print('Running diagnostic tests...')
    comp = Intcode_computer(init_memory)
    comp.run()

    print(comp.get_last_output(exclude_last=True))


if __name__ == '__main__':
    main()