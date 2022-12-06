'''
Day 7-2: Doing work with multiple workers

Verbose code and execution, but wanted to create the classes for workers and
for the workforce, making the actual execution fairly tidy. Much of the code
is for easy access to the current details of the classes
'''

import re
from collections import defaultdict
from pprint import pprint
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

    total_tasks = len(step_d.keys())
    time = 0

    elves = Workforce(5)    
    to_do = elves.assign(to_do)
    print('Working on:', elves.in_progress())
    elves.print_out()
    
    while len(done) < total_tasks:
        d = elves.run()
        time += 1
        if len(d) > 0:
            for i in d:
                done += i
                step_d = remove_from_dicts(i, step_d)
                to_do = get_available(to_do, step_d, done, elves.in_progress())
                print(done)
                elves.print_out()
                print(to_do)
            to_do = elves.assign(to_do)
        
    print(done)
    print('Time taken:', time)
    

# create a group of workers
class Workforce:
    def __init__(self, n):
        self.workers = []
        self.size = n
        for i in range(n):
            self.workers.append(Worker())
    
    def run(self, s=1):
        completed = []
        for _ in range(s):
            for i in range(self.size):
                x = self.workers[i].run()
                if x != None:
                    completed.append(x)
        return completed
    
    def in_progress(self):
        p = ''
        for i in range(self.size):
            x = self.workers[i].working_on
            if x != None:
                p += x
        return p

    def available(self):
        total = 0
        next_worker = None
        found_next = False
        for i in range(self.size):
            if self.workers[i].busy == False:
                total += 1
                if found_next == False:
                    found_next = True
                    next_worker = i
        return total, next_worker
    
    def assign(self, queue):
        while self.available()[0] > 0 and len(queue) > 0:
            self.workers[self.available()[1]].assign(queue.pop(0))
        return queue    
   
    def print_out(self):
        for i in range(self.size):
            print('Worker', i, self.workers[i].get_status())


# create a worker
class Worker:
    def __init__(self):
        self.busy = False
        self.remaining_time = 0
        self.working_on = None


    def assign(self, c):
        self.working_on = c
        self.remaining_time = ord(c) - 4
        self.busy = True

    def run(self, s=1):
        self.remaining_time -= s
        if self.remaining_time == 0:
            self.busy = False
            c = self.working_on
            self.working_on = None
            return c
        else:
            return None
    
    def get_status(self):
        if not self.busy:
            return('not doing anything!')
        else:
            return('is working on %s with %d seconds remaining' %(self.working_on, self.remaining_time))


def get_available(to_do, step_d, done, in_progress=''):
    for key, val in step_d.items():
        if len(val) == 0:
            if key not in to_do and key not in done and key not in in_progress:
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