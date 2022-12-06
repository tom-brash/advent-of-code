
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
    basin_sizes = []
    for i in range(len(input_data)):
        for j in range(len(input_data[1])):
            current = grid[(i, j)]
            low = True
            for d in range(4):
                new_i = i + vecs[d][0]
                new_j = j + vecs[d][1]
                if grid.get((new_i, new_j), 500) <= current:
                    low = False
                    break
            if low:
                basin = set()
                basin.add((i, j))
                updated = True
                while updated:
                    updated_basin = basin.copy()
                    for coord in basin:
                        x, y = coord
                        current = grid[(x, y)]
                        for d in range(4):                            
                            new_x = x + vecs[d][0]
                            new_y = y + vecs[d][1]
                            val = grid.get((new_x, new_y), 9)
                            if val > current and val != 9:
                                updated_basin.add((new_x, new_y))
                    if updated_basin == basin:
                        updated = False
                    basin = updated_basin.copy()
                
                basin_sizes.append(len(basin))

    top_3 = sorted(basin_sizes, reverse=True)[:3]
    print(top_3[0] * top_3[1] * top_3[2])

        
    
if __name__ == '__main__':
    main()
    