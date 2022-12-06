def main():
    with open('2-1-input.txt', 'r') as input_file:
        input_string = input_file.read()

    seq = input_string.split(',')
    seq = [int(i) for i in seq]

    # hard code required by question
    seq[1] = 12
    seq[2] = 2

    # set up variables to run loop
    terminal = False
    current_pos = 0

    while not terminal:
        opcode = seq[current_pos]

        if opcode == 99:  # check if opcode is terminal
            break

        num_1 = seq[seq[current_pos + 1]]
        num_2 = seq[seq[current_pos + 2]]
        repl_ind = seq[current_pos + 3]

        if opcode == 1:
            repl_num = num_1 + num_2
            seq[repl_ind] = repl_num

        elif opcode == 2:
            repl_num = num_1 * num_2
            seq[repl_ind] = repl_num

        else:
            print('Error: invalid opcode')
            terminal = True

        current_pos += 4

    print('Full sequence:', seq)
    print('Integer at position 0:', seq[0])


if __name__ == '__main__':
    main()