'''
Day 1-1: Processing arithmetic

Trivial starting problem processing arithmetic operators
'''

def main():
    with open('day1/1-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    instructions = input_data.split('\n')
    total = 0
    i = 0
    for instruction in instructions:
        if instruction[0] == '+':
            sign = 1
        else:
            sign = -1
        total += sign * int(instruction[1:])
    
    print('Total at end:', total)

if __name__ == '__main__':
    main()