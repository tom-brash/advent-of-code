
import time
import copy
from collections import defaultdict

def main():

    # start_time = time.time()
    with open('9/9.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    vecs = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    
    grid = {}
    for i,r in enumerate(input_data):
        for j, c in enumerate(r):
            grid[(i, j)] = int(c)
    
    t = 0
    for i in range(len(input_data)):
        for j in range(len(input_data[1])):
            current = grid[(i, j)]
            low = True
            for y in range(4):
                new_i = i + vecs[y][0]
                new_j = j + vecs[y][1]
                if grid.get((new_i, new_j), 500) <= current:
                    low = False
                    break
            if low:
                print(current)
                t += current + 1

    print(t)
    # input_data = [int(x) for x in input_data]
    
    for i in input_data:
        pass

    for i in range(len(input_data)):
        pass
    
    
    print(t)
    #print(f'Part 1 time taken: {round((time.time() - start_time) * 1000, 3)} ms')


class Thing():
    def __init__(self, data):
        pass
        
    
if __name__ == '__main__':
    main()
    