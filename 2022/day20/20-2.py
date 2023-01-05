import re
from collections import deque, defaultdict

def main():
    print('\nResults nonsensical. Applying decryption key: 811589153...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    public_key = 811589153

    file = deque()
    order = []
    total_nums = len(input)

    for i, x in enumerate(input):
        n = int(x)  * public_key + i / 11000
        file.append(n)
        order.append(n)

    i = 0
    for j in range(total_nums * 10):
        total_rot = 0
        n = order[j % total_nums]
        ni = round(n)
        ix = file.index(n)
        file.rotate(-ix)
        temp = file.popleft()
        file.rotate(-ni)
        file.appendleft(temp)


    file_l = [round(x) for x in file]
    zix = file_l.index(0)
    
    total = sum([file_l[(zix + n) % total_nums] for n in [1000, 2000, 3000]])
    
    print(f'\nCoordinates of location: {[file_l[(zix + n) % total_nums] for n in [1000, 2000, 3000]]}')
        
    print(f'\n(20-2) Total of coordinates {total}')


if __name__ == "__main__":
    main()
