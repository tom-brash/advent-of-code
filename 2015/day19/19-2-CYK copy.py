'''
An alternative method to 19-2 that takes advantage of the structure of the problem as a context free grammar.
While slower than the greedy approach originally used, it is less reliant on the problem being solvable in 
a greedy manner

'''

import re
from collections import defaultdict

def main():
    with open('day19/19.txt', 'r') as open_file:
        input_data = open_file.read().split('\n\n')

    w = input_data[1]
    rs = input_data[0].split('\n')
    rs = [[x.split(' => ')[0], x.split(' => ')[1]] for x in rs]

    # nonterminals
    V = set()
    for r in rs:
        V.add(r[0])
    V = list(V)

    # terminals
    T = ['C', 'Ar', 'Rn', 'Y']

    # clarify rules into lists of terminals and non-terminals
    rx = re.compile('|'.join(V + T))
    rs = [[r[0], rx.findall(r[1])] for r in rs]

    P = rs

    G = ChomskyGrammar(V, T, P, 'e')
    w = rx.findall(w)
    G.parse(w)
    print(G.get_path(len(w),0))


class ChomskyGrammar:
    def __init__(self, V, T, P, S, convert=True):
        self.V = V
        self.T = T
        self.P = P
        self.S = S
        if convert == True:
            self.P = self.convert_to_chomsky()

    def convert_to_chomsky(self):
        i = 0
        CP = defaultdict(set)
        for t in self.T:
            # CP.add(('T' + str(i), t))
            CP[(t,)].add('T' + str(i))
            i += 1

        updated_rules = []
        for x in self.P:
            l = x[0]
            r = x[1]

            # step 1: remove non-solitary terminals from RHS

            terminals = 0
            for w in r:
                if w in self.T:
                    terminals += 1

            if terminals > 0 and len(r) > 1:
                r = [next(iter(CP[(t,)])) if t in self.T else t for t in r]

            if len(r) == 2:
                CP[tuple(r)].add(l)

            updated_rules.append([l, r])

        # step 2: remove instances of 3+ non terminals from RHS

        i = 0
        for x in updated_rules:
            l = x[0]
            r = x[1]
            if len(r) <= 2:
                continue
            while len(r) > 2:
                y = (r[0], r[1])  # first two non-terminal elements on RHS
                if y not in CP:
                    CP[y].add('X' + str(i))
                    i += 1
                r = [next(iter(CP[y]))] + r[2:]
            CP[tuple(r)].add(l)
        
        # reverse dictionary into regular rules notation
        P = defaultdict(list)
        for k, d in CP.items():
            for x in d:
                P[x].append(k)
        return P


    def parse(self, w):
        print(w)
        CYK_mat = defaultdict(lambda: defaultdict(CNode))

        # set up matrix, with word/phrase as bottom layer

        for j, c in enumerate(w):
            CYK_mat[1][j].T.append(c)

        # searching for lone terminals on layer 1
        for j in range(len(w)):
            for lhs, rule in self.P.items():
                for rhs in rule:
                    if len(rhs) == 1:
                        if rhs[0] == w[j]:
                            CYK_mat[1][j].add_ref(lhs, (0, j), (0, j), (lhs, rhs))
        
        # filling out the rest of the layers using dynamic programming
        for i in range(1, len(w) + 1):
            for j in range(len(w) + 1 - i):
                for k in range(1, i):
                    for lhs, rule in self.P.items():
                        for rhs in rule:
                            if len(rhs) == 2:
                                if rhs[0] in CYK_mat[k][j].T and rhs[1] in CYK_mat[i - k][j + k].T:
                                    CYK_mat[i][j].add_ref(lhs, (k, j), (i - k, j + k), (lhs, rhs))
            if i % 10 == 0:
                print(f'Filled {i} of {len(w)} layers')
        
        self.CYK = CYK_mat
        #self.print_CYK(CYK_mat)
        print()
        print(str(CYK_mat[len(w)][0]))
    
    def get_path(self, i, j):
        if i == 1:
            return 0
        
        l_ref, r_ref, rule = self.CYK[i][j].br[0]
        if rule[0][0] in 'XT':
            current = 0
        else:
            current = 1
        
        l = self.get_path(*l_ref)
        r = self.get_path(*r_ref)
        return current + l + r



    def print_CYK(self, CYK_mat):
        for row in sorted(CYK_mat.keys(), reverse=True):
            row_out = str(row) + ' '
            for node in sorted(CYK_mat[row].keys()):
                row_out += str(CYK_mat[row][node].T)
            print(row_out)

class CNode:
    def __init__(self):
        self.T = []  # possibilities for the cell
        self.br = []  # reference that makes it possible
    
    def add_ref(self, lhs, l_ref, r_ref, rule):
        if lhs not in self.T:
            self.T.append(lhs)
            self.br.append((l_ref, r_ref, rule))
    
    def __str__(self):
        out = 'T: ' + str(self.T) + '\n'
        out += 'Ref: ' + str(self.br)
        return out

if __name__ == '__main__':
    main()
