import time
import copy
from collections import deque

def main():

    # start_time = time.time()
    score = {')' : 1, ']': 2, '}': 3, '>': 4}
    ed = {'(' : ')', '[': ']', '{': '}', '<': '>'}

    with open('10/10.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    scores = []
    
    for x in input_data:
        req = ''
        corrupted = False
        expecting = deque()
        for c in x:
            if c not in ed.keys():
                e = expecting.popleft()
                if c != e:
                    corrupted = True
                    break
            else:
                expecting.appendleft(ed[c])
        v = 0
        if not corrupted:
            for c in expecting:
                req += c
                v *= 5
                v += score[c]
            print(req, v)
            scores.append(v)
        
    print(sorted(scores)[len(scores) // 2])
            
                
    
    for i in range(len(input_data)):
        pass
    


    #print(f'Part 1 time taken: {round((time.time() - start_time) * 1000, 3)} ms')


def parse(s):
    pass

class Thing():
    def __init__(self, data):
        pass
        
    
if __name__ == '__main__':
    main()
    