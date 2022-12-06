'''
DAY 8-1: Processing gameboy instructions

Given previous AOC puzzles with intcode, the code for this is structured
to allow for future additions. Otherwise it is straightforward. Infinite loops
are guaranteed when a n instruction is visited twice, as we are not modifying 
the instructions. 

Assuming there will be more additions, i and accumulator are stored as global variables,
assuming they need to be passed back and forth many times. 

When an instruction is done for the second time, we return the value in the accumulator.
'''

i = 0
accumulator = 0

def main():
    with open('day8/8-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    instructions = input_data.split('\n')
    instructions = [instruct_to_dict(x) for x in instructions]

    executed_instructions = set()

    while i < len(instructions):
        evaluate(instructions[i])
        
        num_commands = len(executed_instructions)
        executed_instructions.add(i)
        if len(executed_instructions) == num_commands:
            break

    print(accumulator)

def instruct_to_dict(instruction):
    i_d = {}
    i_d['program'] = instruction.split()[0]
    i_d['value'] = int(instruction.split()[1])
    return i_d

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