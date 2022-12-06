'''
Day 1-2: Processing arithmetic

Trivial starting problem processing arithmetic operators. Set makes this vastly
faster than list, but otherwise nothing major here
'''

def main():
    with open('day1/1-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    reached_vals = set()
    reached_vals.add(0)
    instructions = input_data.split('\n')
    total = 0
    i = 0
    while True:
        instruction = instructions[i % len(instructions)]
        if instruction[0] == '+':
            sign = 1
        else:
            sign = -1
        total += sign * int(instruction[1:])
        if total in reached_vals:
            print('First val reached twice:', total)
            break
        reached_vals.add(total)
        i += 1
    
    
if __name__ == '__main__':
    main()