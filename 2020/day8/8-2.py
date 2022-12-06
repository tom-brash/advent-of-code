'''
DAY 8-2: Processing gameboy instructions

Here we make many copies of the program to try and find out which set of jmp | nop needs to be 
switched to the other. We modify the code from 8-1 to just inform us if there is an infinite loop,
and then try all of the different versions of the gameboy instructions.

Note that as we are creating copies of a list of objects and don't want to modify the original instructions,
we use the deepcopy function from the copy package.
'''

import copy

i = 0
accumulator = 0

def main():
    global i
    global accumulator
    
    with open('day8/8-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    instructions = input_data.split('\n')
    instructions = [instruct_to_dict(x) for x in instructions]

    switch_dict = {'jmp':'nop', 'nop':'jmp'}
    for i in range(len(instructions)):
        if instructions[i]['program'] == 'acc':
            continue
        else:
            modified_instructions = copy.deepcopy(instructions)
            modified_instructions[i]['program'] = switch_dict[modified_instructions[i]['program']]
            evaluate_instructions(modified_instructions)


def instruct_to_dict(instruction):
    i_d = {}
    i_d['program'] = instruction.split()[0]
    i_d['value'] = int(instruction.split()[1])
    return i_d


def evaluate_instructions(instructions):
    global i
    global accumulator
    
    # set up the environment
    executed_instructions = set()
    i = 0
    accumulator = 0
    infinite_loop = False
    
    # run instructions
    while i < len(instructions):
        evaluate(instructions[i])       
        num_commands = len(executed_instructions)
        executed_instructions.add(i)
        if len(executed_instructions) == num_commands:
            infinite_loop = True
            break
    if infinite_loop == False:
        print(accumulator)


def evaluate(instruction):
    global i
    global accumulator
    program = instruction['program']
    value = instruction['value']
    if program == 'nop':
        i += 1
    elif program == 'acc':
        accumulator += value
        i += 1
    elif program =='jmp':
        i += value


if __name__ == "__main__":
    main()