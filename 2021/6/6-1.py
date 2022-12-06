import time

def main():

    start_time = time.time()
    with open('6/6.txt', 'r') as open_file:
        input_data = open_file.read().split(',')
    
    school = []

    for i in input_data:
        school.append(Lantern(int(i)))
    
    for i in range(80):
        news = []
        for f in school:
            new = f.step()
            if new != None:
                news.append(new)
        school = school + news
    
    print(len(school))
    print(f'Part 1 time taken: {round((time.time() - start_time) * 1000, 3)} ms')



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
    