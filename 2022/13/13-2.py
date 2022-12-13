import re
from collections import deque, defaultdict
from functools import cmp_to_key

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n\n')

    packets = []

    for i, pair in enumerate(input):
        packets.extend([eval(x) for x in pair.split('\n')])

    packets.extend([[[2]], [[6]]])
    packets = sorted(packets, key = cmp_to_key(compare_packets))
    
    print(f'Final answer: {(packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)}')

def compare_packets(left, right):
    
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        return 0

    if isinstance(left, int):
        left = [left]

    if isinstance(right, int):
        right = [right]

    if len(left) < len(right):
        tiebreak = -1
    elif len(right) < len(left):
        tiebreak = 1
    else:
        tiebreak = 0

    for i in range(min(len(left), len(right))):
        comp_val = compare_packets(left[i], right[i])
        if comp_val == -1:
            return -1
        elif comp_val == 1:
            return 1
    
    return tiebreak

if __name__ == "__main__":
    main()
