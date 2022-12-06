# First ever leaderboard time: 81st (1.45)

import time

def main():

    start_time = time.time()
    with open('7/7.txt', 'r') as open_file:
        input_data = open_file.read().split(',')
    
    input_data = [int(x) for x in input_data]

    min_h = min(input_data)
    max_h = max(input_data)
    best = 1000000
    for i in range(min_h, max_h):
        t=  0
        for x in input_data:
            t += abs(x - i)
            if t > best:
                break
        if t < best:
            best = t
    
    print(best)
    
    
    print(f'Part 1 time taken: {round((time.time() - start_time) * 1000, 3)} ms')

def get_fuel(a):
    t = 00
    x = 1
    for a in range(a):
        t += x
        x += 1
    return t


class Thing():
    def __init__(self, data):
        pass
        
    
if __name__ == '__main__':
    main()
    