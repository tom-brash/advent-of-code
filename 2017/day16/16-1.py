import string
import re
from tqdm import tqdm
import copy


def main():
    with open('day16/16.txt', 'r') as open_file:
        instructions = open_file.read().split(',')
    
    s = string.ascii_lowercase[:16]
    dancers = [c for c in s]
    for i in instructions:
        if i[0] == 's':
            dancers = spin(dancers, int(i[1:]))
        elif i[0] == 'x':
            dancers = exchange(dancers, i[1:])
        elif i[0] == 'p':
            dancers = partner(dancers, i[1:])

    print(''.join(dancers))


def spin(dancers, x):
    temp = dancers[-x:]
    temp.extend(dancers[:-x])
    return temp

def exchange(dancers, info):
    vals = [int(i) for i in re.findall(r'\d+', info)]
    dancers[vals[0]], dancers[vals[1]] = dancers[vals[1]], dancers[vals[0]]

    return dancers

def partner(dancers, info):
    vals = re.findall(r'\w+', info)
    ind_1 = dancers.index(vals[0])
    ind_2 = dancers.index(vals[1])
    dancers[ind_1], dancers[ind_2] = dancers[ind_2], dancers[ind_1]
    return dancers

if __name__ == '__main__':
    main()
    