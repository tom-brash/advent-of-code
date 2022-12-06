import re

def main():
    with open('day14/14.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    reindeer = {}
    for r in input_data:
        nums = [int(x) for x in re.findall(r'\d+', r)]
        n = r.split()[0]
        reindeer[n] = (nums[0], nums[1], nums[2])
    
    best = 0
    for n in reindeer.keys():
        r = Reindeer(*reindeer[n])
        r.fly(2503)
        print(n, r.loc)
        if r.loc > best:
            best = r.loc
    
    print(f'\nDistance of winning reindeer: {best}')

class Reindeer:
    def __init__(self, s, t, r):
        self.s = s
        self.t = t
        self.r = r
        self.loc = 0
        self.resting = False
        self.rd = 0
        self.fd = 0
    
    def fly(self, f):
        for _ in range(f):
            if self.resting:
                if self.rd == self.r:
                    self.rd = 0
                    self.resting = False
                    self.fd += 1
                    self.loc += self.s
                    continue
                else:
                    self.rd += 1
                    continue
            else:
                if self.fd == self.t:
                    self.fd = 0
                    self.resting = True
                    self.rd += 1
                else:
                    self.loc += self.s
                    self.fd += 1


if __name__ == '__main__':
    main()