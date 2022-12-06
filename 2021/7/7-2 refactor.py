import time

def main():

    start_time = time.time()
    with open('7/7.txt', 'r') as open_file:
        input_data = open_file.read().split(',')
    
    input_data = [int(x) for x in input_data]

    min_h = min(input_data)
    max_h = max(input_data)
    best = 100000000000
    for i in range(min_h, max_h):
        t=  0
        for x in input_data:
            dist = abs(x- i)
            t += dist * (dist + 1) / 2
            if t > best:
                break
        if t < best:
            best = t
    
    print(best)
    
    print(f'Part 2 time taken: {round((time.time() - start_time) * 1000, 3)} ms')



class Thing():
    def __init__(self, data):
        pass
        
    
if __name__ == '__main__':
    main()
    