'''
Day 3-2: Finding a unique claim

Another one done as train of thought for speed to code rather than speed to compute (though
it is again small enough to still be very efficient). The code from 3-1 can be easily 
extended, we just need to loop back through the boxes (having not cached the regexes...)
to see which one never overlaps
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
    
    for c in claims:
        overlap = False
        x = int(re.search(r'\@\ ([0-9]+)', c)[1])
        y = int(re.search(r'\,([0-9]+)', c)[1])
        w = int(re.search(r'([0-9]+)x', c)[1])
        h = int(re.search(r'x([0-9]+)', c)[1])
        id = int(re.search(r'\#([0-9]+)', c)[1])

        for i in range(w):
            for j in range(h):
                if spaces[(x + i, y + j)] > 1:
                    overlap = True
        
        if overlap == False:
            print(id)
            break
    

if __name__ == '__main__':
    main()