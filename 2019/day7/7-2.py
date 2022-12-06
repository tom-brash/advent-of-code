'''
DAY 7-2: (Intcode) Running looped boosters

Now each booster needs to be stored as a separate object. This is enabled
by creating Intcode_computer classes. Each computer is run until it hits an 
output, at which point it will pause. Before it is run again, the previous
computer's output will be added to the computer's input queue.
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
    permutation_list = list(itertools.permutations([5, 6, 7, 8, 9]))

    best_power = 0
    best_permutation = ()

    test_computer = Intcode_computer(init_memory, input_queue=[5, 1])
    test_computer.run()

    for permutation in permutation_list:

        booster_phases = list(permutation)
        boosters = {}
        for i in range(5):
            boosters[i] = Intcode_computer(init_memory, input_queue = [booster_phases[i]])
        
        next_input = 0
        run_count = 0
        current_booster = boosters[0]

        e_outputs = []
        while current_booster.get_last_output() != 'halt':
            current_booster = boosters[run_count % 5]
            current_booster.add_to_input_queue(next_input)
            current_booster.run(pause_at_output=True)
            next_input = current_booster.get_last_output()
            if run_count % 5 == 4:
                e_outputs.append(next_input)
            run_count += 1
        
        if e_outputs[-1] == 'halt':
            e_outputs.remove('halt')
        
        final_power = int(e_outputs[-1])
        if final_power > best_power:
            best_power = final_power
            best_permutation = list(permutation)

    print('Maximum power obtained: ', best_power)
    print('Maximum permutation: ', best_permutation)


if __name__ == '__main__':
    main()