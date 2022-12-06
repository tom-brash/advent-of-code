'''
DAY 14-2: Apply modified memory bitmask to get multiple memory locations

The function of 'X' in the bitmask is now either a 0-1, and we need to find all
possible values of the masked number based on those possibilities.

We use itertools to create all possible sequences of 0 and 1 of length n, where
n is the number of Xs in the current bitmask. Much like in 14-1, we use similar
methods of converting between base 10 and 2 to convert back and forth, and add
the value to all of the memory locations that are implied by the different 
sequences
'''

import re
import itertools

def main():
    with open('day14/14-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    instructions = input_data.split('\n')
    mask = '0' * 32
    memory = {}
    for instruction in instructions:
        if instruction[0:4] == 'mask':
            mask = instruction.split(' = ')[-1]
        else:
            mem_location = int(re.search(r'\[([A-Za-z0-9_]+)\]', instruction).group(1))
            number = int(instruction.split(' = ')[-1])
            memory_masked = apply_mem_mask(mem_location, mask)
            memory_list = mem_permutations(memory_masked)
            for mem_loc in memory_list:
                memory[mem_loc] = number
    
    total = 0
    for value in memory.values():
        total += value

    print(total)


def apply_mem_mask(mem_location, mask):
    bin_number = str(bin(mem_location))[2:]
    bin_number = up_to_36(bin_number)
    masked_number = [0] * 36
    for i in range(len(bin_number)):
        if mask[i] != '0':
            masked_number[i] = mask[i]
        else:
            masked_number[i] = bin_number[i]
    masked_number = ''.join(masked_number)
    return masked_number


def mem_permutations(masked_number):
    number_floats = masked_number.count('X')
    perm_list = list(itertools.product([0, 1], repeat = number_floats))
    memory_list = []
    for perm in perm_list:
        perm_l = list(perm)
        new_memory = masked_number
        for _ in range(number_floats):
            new_memory = new_memory.replace('X', str(perm_l.pop(0)), 1)
        memory_list.append(int(new_memory, 2))
    return(memory_list)


def up_to_36(bin_number):
    extra_zeroes = 36 - len(bin_number)
    return('0' * extra_zeroes + bin_number)


if __name__ == "__main__":
    main()