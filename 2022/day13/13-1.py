import re
from collections import deque, defaultdict
import ast

def main():
    print('====Day 13====')
    print('Picked up distress signal!')
    print('Reordering packets in distress signal...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n\n')

    total = 0

    for i, pair in enumerate(input):
        packets = [ast.literal_eval(p) for p in pair.split('\n')]
        left = packets[0]
        right = packets[1]
        outcome = compare_packets(left, right)
        if outcome:
            total += (i + 1)

    print(f'\n(13-1) Packets already in the correct order: {total}')

def compare_packets(left, right):
    
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        return None

    if isinstance(left, int):
        left = [left]

    if isinstance(right, int):
        right = [right]

    if len(left) < len(right):
        tiebreak = True
    elif len(right) < len(left):
        tiebreak = False
    else:
        tiebreak = None

    for i in range(min(len(left), len(right))):
        comp_val = compare_packets(left[i], right[i])
        if comp_val == True:
            return True
        elif comp_val == False:
            return False
    
    return tiebreak

if __name__ == "__main__":
    main()
