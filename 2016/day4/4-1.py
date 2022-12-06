import re
from collections import Counter

def main():
    with open('day4/4.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    total = 0
    room_count = 0

    for room in input_data:
        room_data = re.search(r'(.+?)(\d+)\[(\w+)\]', room)
        name = room_data.group(1).replace('-', '')
        number = int(room_data.group(2))
        checksum = room_data.group(3)

        most_common = Counter(name).most_common()
        most_common.sort(key=lambda x: (-x[1], x[0]))
        
        code = ''
        for i in range(5):
            code += most_common[i][0]
        
        if code == checksum:
            total += number
            room_count += 1
    
    print(f'Total values on each of the rooms: {total}')
    print(f'Total number of valid rooms: {room_count}')


if __name__ == '__main__':
    main()