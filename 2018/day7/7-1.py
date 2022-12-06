'''
Day 7-1: Doing work in particular order

Here we create a dictionary of prerequisites that are needed to do particular steps.
We craete a queue of the tasks that are currently available (in alpha order) and keep
doing the leftmost one, adding the newly unblocked tasks to the queue accordingly
'''

import re
from collections import defaultdict
import string

def main():
    with open('day7/7-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    step_d = dict()
    for c in string.ascii_uppercase:
        step_d[c] = []
    info = input_data.split('\n')
    r1 = re.compile(r'([A-Z]) must')
    r2 = re.compile(r'([A-Z]) can')
    for i in info:
        step_d[re.search(r2, i)[1]].append(re.search(r1, i)[1])

    to_do = []
    done = ''
    to_do = get_available(to_do, step_d, done)    
    while len(to_do) > 0:
        n = to_do.pop(0)
        done += n
        step_d = remove_from_dicts(n, step_d)
        to_do = get_available(to_do, step_d, done)
    
    print(done)


def get_available(to_do, step_d, done):
    for key, val in step_d.items():
        if len(val) == 0:
            if key not in to_do and key not in done:
                to_do.append(key)
    
    to_do.sort()
    return(to_do)


def remove_from_dicts(c, step_d):
    for key, val in step_d.items():
        if c in val:
            step_d[key] = [x for x in val if x != c]
    
    return step_d

if __name__ == '__main__':
    main()