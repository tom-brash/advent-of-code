'''
Version done for speed. Aggresively uses heuristic that at any given stage the shortest solution
is the 'closest' to the answer of 'e', which works for this input but may not generally. The
explosion of possible moves at each potential state, and the eventual answer (212) suggests that
unmodified BFS may be non-feasible in this case.
'''

import re
from collections import defaultdict
from collections import deque
import copy

def main():
    with open('day19/19.txt', 'r') as open_file:
        input_data = open_file.read().split('\n\n')

    s = input_data[1]
    rs = input_data[0].split('\n')
    replacements = defaultdict(list)
    for r in rs:
        info = r.split(' => ')
        replacements[info[1]].append(info[0])

    m = Molecule(replacements, s, 'e')
    m.find_molecule()
   
    

class Molecule:
    def __init__(self, replacements, s, t):
        self.replacements = replacements
        self.s = s
        self.t = t


    
    def get_possibilities(self, s, d):
        possibilities = set()
        for e in self.replacements.keys():
            rx = re.compile(e)
            n = len(rx.findall(s))        
            for i in range(n):
                for p in self.replacements[e]:
                    possibilities.add(self.replace(s, e, p, i))
        return [(x, d + 1) for x in list(possibilities)]

    def find_molecule(self):
        sq = deque()
        sq.append((copy.deepcopy(self.s), 0)) # format s, d
        best = {}
        last_d = 0
        i = 0
        while sq:
            s, d = sq.popleft()
            i += 1
            sq = deque(sorted(list(sq), key=(lambda x: len(x[0]))))  # yikes - works here, but shouldn't on general input
            if s == self.t:
                print(d)
                break
            b = best.get(s, 1000000)
            if d >= b:
                continue
            best[s] = d
            sq.extend(self.get_possibilities(s, d))
            

    def replace(self, s, sub, wanted, n):
        where = [m.start() for m in re.finditer(sub, s)][n]
        before = s[:where]
        after = s[where:]
        after = after.replace(sub, wanted, 1)
        ns = before + after
        return ns



if __name__ == '__main__':
    main()