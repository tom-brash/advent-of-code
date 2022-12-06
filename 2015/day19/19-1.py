import re
from collections import defaultdict
from itertools import permutations

def main():
    with open('day19/19.txt', 'r') as open_file:
        input_data = open_file.read().split('\n\n')

    s = input_data[1]
    rs = input_data[0].split('\n')
    replacements = defaultdict(list)
    elems = set() 
    for r in rs:
        info = r.split(' => ')
        replacements[info[0]].append(info[1])
        elems.add(info[0])
    print(replacements)
    print(elems)

    possibilities = set()
    for e in replacements.keys():
        rx = re.compile(e)
        n = len(rx.findall(s))        
        for i in range(n):
            for p in replacements[e]:
                possibilities.add(replacenth(s, e, p, i))
    
    print(len(possibilities))
    

def replacenth(s, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, s)][n]
    before = s[:where]
    after = s[where:]
    after = after.replace(sub, wanted, 1)
    ns = before + after
    return ns




if __name__ == '__main__':
    main()