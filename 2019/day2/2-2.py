'''
DAY 2-2: (Intcode) Finding nouns and verbs

In this version, using a completed Intcode Computer, we can loop through all possible
combinations of nouns and verbs between 0-99 and check whether they equal the magic 
number, in this case 19690720
''' 

from itertools import combinations_with_replacement
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from intcode import Intcode_computer

def main():
    with open('day2/2-1-input.txt', 'r') as input_file:
        input_string = input_file.read()

    init_memory = input_string.split(',')
    init_memory = [int(i) for i in init_memory]

    possible_combinations = list(combinations_with_replacement(range(100),2))
    for c in possible_combinations:
        memory = init_memory.copy()
        memory[1] = c[0]
        memory[2] = c[1]
        comp = Intcode_computer(memory)
        comp.run()
        if comp.memory[0] == 19690720:
            noun = c[0]
            verb = c[1]
            break
    
    print('noun: ', noun)
    print('verb: ', verb)
    print('answer: ', 100 * noun + verb)



if __name__ == '__main__':
    main()