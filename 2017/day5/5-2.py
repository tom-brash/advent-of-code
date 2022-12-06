def main():
    with open('day5/5.txt', 'r') as open_file:
        instructions = open_file.read().split('\n')

    instructions = [int(i) for i in instructions]

    i = 0
    steps = 0
    while i >= 0 and i < len(instructions):
        c = instructions[i]
        if instructions[i] < 3:
            instructions[i] += 1
        else:
            instructions[i] -= 1
        i += c
        steps += 1
    
    print(steps)


if __name__ == '__main__':
    main()