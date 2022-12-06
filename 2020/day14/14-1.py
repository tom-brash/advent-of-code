'''
DAY 14-1: Apply bitmask to numbers

This basically revolves around creating the function to apply a bitmask,
and converting back and forth between base 10 and base 2. The masked 
number is dropped in a dictionary set up for memory
'''

import re

def main():
    with open('day14/14-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    instructions = input_data.split('\n')
    mask = '0' * 32
    memory = {}
    for instruction in instructions:
        if instruction[0:4] == 'mask':
            mask = instruction.split(' = ')[-1]
            print('mask is now ' + mask)
        else:
            mem_location = re.search(r'\[([A-Za-z0-9_]+)\]', instruction).group(1)
            number = int(instruction.split(' = ')[-1])
            memory[mem_location] = apply_mask(number, mask)
    
    print(memory)
    total = 0
    for value in memory.values():
        total += value

    print(total)


def apply_mask(number, mask):
    bin_number = str(bin(number))[2:]
    bin_number = up_to_36(bin_number)
    masked_number = [0] * 36
    for i in range(len(bin_number)):
        if mask[i] != 'X':
            masked_number[i] = mask[i]
        else:
            masked_number[i] = bin_number[i]
    masked_number = ''.join(masked_number)
    return int(masked_number, 2)


def up_to_36(bin_number):
    extra_zeroes = 36 - len(bin_number)
    return('0' * extra_zeroes + bin_number)

if __name__ == "__main__":
    main()