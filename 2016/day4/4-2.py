import re
from collections import Counter

def main():
    with open('day4/4.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    total = 0
    room_count = 0

    for room in input_data:
        room_data = re.search(r'(.+?)(\d+)\[(\w+)\]', room)
        o_name = room_data.group(1)
        name = room_data.group(1).replace('-', '')
        number = int(room_data.group(2))
        checksum = room_data.group(3)

        most_common = Counter(name).most_common()
        most_common.sort(key=lambda x: (-x[1], x[0]))
        
        code = ''
        for i in range(5):
            code += most_common[i][0]
        
        if code != checksum:
            continue
        
        d_name = ''
        for c in o_name:
            d_name += c_shift(c, number)

        if 'north' in d_name:
            print(d_name, number)


def c_shift(c, n):
    if c == '-':
        return c
    return (chr((ord(c) + n - 97) % 26 + 97))


if __name__ == '__main__':
    main()