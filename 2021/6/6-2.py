from collections import defaultdict
import time

def main():

    
    with open('6/6.txt', 'r') as open_file:
        input_data = open_file.read().split(',')
    
    school = defaultdict(int)
    start_time = time.time()
    for i in input_data:
        school[int(i)] += 1
    
    for i in range(256):
        new_school = defaultdict(int)
        for k, v in school.items():
            if k == 0:
                new_school[6] += v
                new_school[8] += v
            else:
                new_school[k - 1] += v
        school = new_school
    
    print(sum(school.values()))
    print(f'Part 2 time taken: {round((time.time() - start_time) * 1000, 3)} ms')

class Lantern():
    def __init__(self, n):
        self.n = n
        self.new = False
    
    def step(self):
        if self.n == 0:
            self.n = 6
            return Lantern(8)
        self.n -= 1
        return None
        
    
if __name__ == '__main__':
    main()
    