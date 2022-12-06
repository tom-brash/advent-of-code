
import time
import copy

def main():

    start_time = time.time()
    with open('8/8.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    # input_data = [int(x) for x in input_data]
    t = 0
    for i in input_data:
        x = i.split(' | ')[1]
        for v in x.split():
            if len(v) in [2, 3, 4, 7]:
                t +=1

    for i in range(len(input_data)):
        pass
    
    
    print(t)
    #print(f'Part 1 time taken: {round((time.time() - start_time) * 1000, 3)} ms')


class Thing():
    def __init__(self, data):
        pass
        
    
if __name__ == '__main__':
    main()
    