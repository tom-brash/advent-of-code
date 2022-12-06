import time
import copy
from collections import deque

def main():

    # start_time = time.time()
    score = {')' : 3, ']': 57, '}': 1197, '>': 25137}
    ed = {'(' : ')', '[': ']', '{': '}', '<': '>'}

    with open('10/10.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    t = 0
    
    for x in input_data:
        fine = True
        expecting = deque()
        for c in x:
            if c not in ed.keys():
                e = expecting.popleft()
                if c != e:
                    print(f'expected {e} found {c}')
                    print(score[c])
                    t += score[c]
                    break
            else:
                expecting.appendleft(ed[c])
                
    
    for i in range(len(input_data)):
        pass
    

    print(t)

    #print(f'Part 1 time taken: {round((time.time() - start_time) * 1000, 3)} ms')


def parse(s):
    pass

class Thing():
    def __init__(self, data):
        pass
        
    
if __name__ == '__main__':
    main()
    