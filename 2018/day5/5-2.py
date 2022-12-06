'''
Day 5-2: Finding best letter to remove

Tidy piece of code, but relatively slow execution, following on from the regex method
of 5-1. Tests each string individually, meaning the time is ~26x that of the previous
method (sub 1min, but still relatively slow).

There are definitely improvements possible, but I like the neatness of the regex method
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

    min_length = 1000000
    for c in string.ascii_lowercase:
        test_string = remove_blocker(code, c)
        l = len(react_polymer(test_string, r))
        if l < min_length:
            min_length = l

    print('Minimum length:', min_length)    


def remove_blocker(code, c):
    r = re.compile(c + '|' + c.upper())
    return re.sub(r, '', code)


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