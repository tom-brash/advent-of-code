'''
DAY 7-1: (Intcode) Running sequential boosters

In this version of the code, each booster is only used once. As a result, there
is no need to store individual instances of the boosters
''' 

import sys
import os
import itertools

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from intcode import Intcode_computer

def main():
    with open('day7/7-1-input.txt','r') as input_file:
        input_contents = input_file.read()

    init_memory = [int(i) for i in input_contents.split(',')]

    permutation_list = list(itertools.permutations([0, 1, 2, 3, 4]))

    max_power = 0
    max_permutation = ()
    for permutation in permutation_list:
        next_input = 0
        for i in range(5):
            booster = Intcode_computer(init_memory, input_queue = [permutation[i], next_input])
            booster.run(pause_at_output=True)
            next_input = booster.output_queue[-1]
        
        final_power = next_input
        if final_power > max_power:
            max_power = final_power
            max_permutation = permutation


    print('Maximum power obtained: ', max_power)
    print('Maximum permutation:' , max_permutation)


if __name__ == '__main__':
    main()