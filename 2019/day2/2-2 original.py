def main():
    with open('2-1-input.txt','r') as input_file:
        input_contents = input_file.read()

    init_memory = [int(i) for i in input_contents.split(',')]

    #init_memory[1] = 12
    #init_memory[2] = 2
    #test = process_intcode(init_memory)


    noun, verb = search_for_noun_verb(19690720, init_memory)

    print('noun:', noun)
    print('verb:', verb)
    print('final solution:', 100 * noun + verb)


def search_for_noun_verb(target, init_memory):

    # test multiple combinations of 'nouns' and 'verbs' to find target
    for i in range(99):
        for j in range(99):

            memory = init_memory.copy()  # ensure init_memory remains unchanged
            memory[1] = i
            memory[2] = j

            memory = process_intcode(memory)
            output = memory[0]

            if output == target:
                noun = i
                verb = j
                return noun, verb

    print('Noun and verb not found to get to target: ', target)
    return 100, 100  # error values if noun and verb are not found


def process_intcode(memory):
    param_counter = {1:3, 2:3, 99:0}  # hard code noting how many parameters current instruction requires
    instruction_pointer = 0
    while True:
        current_instruction = memory[instruction_pointer]

        if current_instruction not in param_counter:
            print('Invalid opcode found:',current_instruction)
            return memory

        if current_instruction == 99:
            # termination code
            return memory

        if current_instruction == 1:
            # add numbers located at indices shown by params 1 and 2, and store them in param 3 index
            memory[memory[instruction_pointer + 3]] = memory[memory[instruction_pointer + 1]] + \
                                              memory[memory[instruction_pointer + 2]]

        if current_instruction == 2:
            # multiply numbers located at indices shown by params 1 and 2, and store them in param 3 index
            memory[memory[instruction_pointer + 3]] = memory[memory[instruction_pointer + 1]] * \
                                              memory[memory[instruction_pointer + 2]]

        instruction_pointer += param_counter[current_instruction] + 1  # move instruction pointer


if __name__ == '__main__':
    main()