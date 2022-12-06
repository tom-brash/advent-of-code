'''
Day 5-1: Reducing string according to rules

Here we just use a single regex expression for all of the letter pairs,
and run it over the string using re.sub until it stops changing. Not ultra
efficient, but works in 1-2 seconds and is a fairly tidy way of doing it
from code perspective
'''

import re
import string

def main():
    with open('day5/5-1-input.txt', 'r') as open_file:
        code = open_file.read()

    r = ''
    for c in string.ascii_lowercase:
        r += c + c.upper() + '|' + c.upper() + c +'|'
    r = re.compile(r[:-1])

    code = react_polymer(code, r)
    print('Length of remaining code after substitutions:', len(code))    


def react_polymer(code, r):
    stable = False
    while not stable:
        stable = True
        last_code = code
        code, n = re.subn(r, '', code)
        if n != 0:
            stable = False   
    return code

if __name__ == '__main__':
    main()