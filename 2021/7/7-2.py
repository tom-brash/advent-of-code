import time

def main():

    start_time = time.time()
    with open('7/7.txt', 'r') as open_file:
        input_data = open_file.read().split(',')
    
    input_data = [int(x) for x in input_data]

    min_h = min(input_data)
    max_h = max(input_data)
    best = 100000000000
    fuel_dict = {}
    a = 0
    b = 0
    for i in range(min_h, max_h):
        t=  0
        for x in input_data:
            dist = abs(x- i)
            if dist in fuel_dict:
                a += 1
                t += fuel_dict[dist]
            else:
                b += 1
                y = get_fuel(dist)
                t += y
                fuel_dict[dist] = y
            if t > best:
                break
        if t < best:
            best = t
    
    print(best)
    
    print(f'Calculated manually: {b}\nCalculated using memoization: {a}')
    print(f'Part 2 time taken: {round((time.time() - start_time) * 1000, 3)} ms')

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
    