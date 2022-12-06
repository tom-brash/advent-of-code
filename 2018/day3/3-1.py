'''
Day 3-1: Processing claims

Here we make a dictionary to establish which claims are infringing on which spaces
fof fabric. We use regex to process the claims, and then just add them to the dictinoary 
entry for the space
'''
from collections import defaultdict
import re

def main():
    with open('day3/3-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    claims = input_data.split('\n')
    spaces = defaultdict(int)
    for c in claims:
        x = int(re.search(r'\@\ ([0-9]+)', c)[1])
        y = int(re.search(r'\,([0-9]+)', c)[1])
        w = int(re.search(r'([0-9]+)x', c)[1])
        h = int(re.search(r'x([0-9]+)', c)[1])

        for i in range(w):
            for j in range(h):
                spaces[(x + i, y + j)] += 1
    
    total = 0
    for val in spaces.values():
        if val > 1:
            total += 1

    print(total)

if __name__ == '__main__':
    main()