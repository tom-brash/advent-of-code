import re
from collections import deque, defaultdict

def main():
    print('\nAmending to look for start of message markers...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip()

    input = [c for c in input]
    for i, c in enumerate(input):
        ss = set(input[i: i + 14])
        if len(ss) == 14:
            print(f'\n(6-2) Detected subroutine buffer at position: {i + 14}')
            break

if __name__ == "__main__":
    main()
