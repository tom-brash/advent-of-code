import re
from collections import deque, defaultdict

def main():
    print('====Day 6====')
    print('Leaving camp!')
    print('Received malfunctioning *device*')
    print('Debugging the communication routine...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip()

    input = [c for c in input]
    for i, c in enumerate(input):
        ss = set(input[i: i + 4])
        if len(ss) == 4:
            print(f'\n(6-1) Detected subroutine buffer at position: {i + 4}')
            break

if __name__ == "__main__":
    main()
