import re
from collections import defaultdict
from itertools import permutations

def main():
    with open('day13/13.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    prefs = defaultdict(dict)
    name_list = set()
    for i in input_data:
        names = re.findall(r'[A-Z]\w+', i)
        change = re.findall(r'\w+\ \d+', i)[0].split()
        if change[0] == 'gain':
            change = int(change[1])
        else:
            change = -1 * int(change[1])
        name_list.add(names[0])
        prefs[names[0]][names[1]] = change
    
    name_list = list(name_list)
    perm = list(permutations(name_list, len(name_list)))
    best = 0
    for p in perm:
        h = test_happiness(p, prefs)
        if h > best:
            best = h
    
    print(best)

def test_happiness(perm, prefs):
    total = 0
    l = len(perm)
    for i, p in enumerate(perm):
        total += prefs[p][perm[(i + 1) % l]]
        total += prefs[p][perm[(i - 1) % l]]
    return total

if __name__ == '__main__':
    main()