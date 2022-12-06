'''
DAY 9-1: (Intcode) Finishing up the intcode processor

The intcode processor does most of the work here. For 9-1, the input value 
to be used is 1
''' 

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# intcode processor
from intcode import Intcode_computer

def main():
    with open('day9/9-1-input.txt','r') as input_file:
        input_contents = input_file.read()

    init_memory = [int(i) for i in input_contents.split(',')]
    comp = Intcode_computer(init_memory)
    comp.run()
    print(comp.get_last_output(exclude_last=True))

if __name__ == '__main__':
    main()