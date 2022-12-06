'''
DAY 9-2: Finishing up the intcode processor

Day 9-2 works on exactly the same principles as 9-1, except uses 2 as the test code
''' 

# intcode processor
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