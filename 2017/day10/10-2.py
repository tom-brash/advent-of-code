from collections import defaultdict
from functools import reduce

def main():
    with open('day10/10.txt', 'r') as open_file:
        input_data = open_file.read()
    
    instructions = [ord(c) for c in input_data]
    instructions.extend([17, 31, 73, 47, 23])  # provided in question
    instructions = instructions * 64  # run a total of 64 rounds, preserving current and skip positions

    s = {x:x for x in range(256)}
    
    # sparse hash
    current = 0
    skip = 0

    for i in instructions:
        marks = list(range(current, current + i))
        seq = [s[x % 256] for x in marks]
        for x, m in enumerate(marks):
            s[m % 256] = seq[-(x + 1)]
        
        current = (current + i + skip) % 256
        skip += 1
    
    # dense hash

    print_string = ''
    for i in range(16):
        vals = [s[x] for x in range(i * 16, (i + 1) * 16)]
        res = reduce(lambda x, y: x ^ y, vals)
        hex_string = hex(res)[2:]
        if len(hex_string) == 1:
            hex_string = '0' + hex_string
        
        print_string += hex_string

    print(print_string)
        

if __name__ == '__main__':
    main()