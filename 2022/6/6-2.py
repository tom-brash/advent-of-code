import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip()

    input = [c for c in input]
    for i, c in enumerate(input):
        ss = set(input[i: i + 4])
        if len(ss) == 4:
            print(i+4)
            break

if __name__ == "__main__":
    main()
