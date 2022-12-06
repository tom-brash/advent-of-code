# intcode processor

def main():
    with open('5-1-input.txt','r') as input_file:
        input_contents = input_file.read()

    init_memory = [int(i) for i in input_contents.split(',')]

    print('Running diagnostic tests...')
    _ = process_intcode(init_memory)


def process_intcode(memory):
    param_dict = {'01': 3, '02': 3, '03': 1, '04': 1, '99': 0}  # hard code noting how many parameters current instruction requires
    instruction_pointer = 0
    while True:
        current_value = str(memory[instruction_pointer])

        # extract opcode from the value at the instruction pointer
        if len(current_value) == 1:
            current_opcode = '0' + current_value
        else:
            current_opcode = current_value[-2:]

        # test if the opcode is a valid one
        if current_opcode not in param_dict:
            print('Invalid opcode found:', current_opcode)
            return memory

        # exit program if current opcode is 99
        if current_opcode == '99':
            return memory

        # determine modes for each parameter of the current opcode
        param_modes = get_param_modes(current_value[:-2], param_dict[current_opcode])

        # based on parameter modes, determine parameters as a dictionary
        params = get_params(memory, instruction_pointer, param_modes)

        # RUN OPCODE INSTRUCTIONS
        if current_opcode == '01':
            # add numbers located at indices shown by params 1 and 2, and store them in param 3 index
            # note here that for 01 and 02 the third parameter works as if it were in immediate mode
            # as such cannot use the value indicated by the params dictionary and is accessed directly
            memory[memory[instruction_pointer + 3]] = params[0] + params[1]

        if current_opcode == '02':
            # multiply numbers located at indices shown by params 1 and 2, and store them in param 3 index
            # note here that for 01 and 02 the third parameter works as if it were in immediate mode
            # as such cannot use the value indicated by the params dictionary and is accessed directly
            memory[memory[instruction_pointer + 3]] = params[0] * params[1]

        if current_opcode == '03':
            memory[memory[instruction_pointer + 1]] = int(input('Input diagnostic test value: '))

        if current_opcode == '04':
            print('Output: ', params[0])

        instruction_pointer += param_dict[current_opcode] + 1  # move instruction pointer


def get_param_modes(param_value, num_params):
    param_modes = param_value
    if len(param_modes) < num_params:
        param_modes = '0' * (num_params - len(param_modes)) + param_modes
    return param_modes[::-1] # reverse string to align modes with parameters


def get_params(memory, instruction_pointer, param_modes):
    params = {}
    for i, j in enumerate(param_modes):
        if j == '0':  # if parameter is in position mode
            params[i] = memory[memory[instruction_pointer + i + 1]]
        else:  # if parameter is in immediate mode
            params[i] = memory[instruction_pointer + i + 1]
    return params


if __name__ == '__main__':
    main()