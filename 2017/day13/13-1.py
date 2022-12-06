import re

def main():
    with open('day13/13.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    firewall = Firewall(input_data)
    firewall.run()
    

class Firewall:
    def __init__(self, info):
        self.layers = {}
        for l in info:
            details = re.findall(r'\d+', l)
            self.layers[int(details[0])] = int(details[1])
        self.loc = -1
        self.time = 0
        self.severity = 0
        self.last_layer = max(self.layers.keys())
    
    def step(self):
        self.loc += 1
        r = self.layers.get(self.loc, 0)
        if r != 0:
            if self.time % ((r - 1) * 2) == 0 and self.time != 0:
                print('Caught! Severity:', self.loc * r)
                print('Time', self.time)
                self.severity += self.loc * r
        self.time += 1
    
    def run(self, delay=0):
        while self.loc < self.last_layer:
            self.step()
        
        print('Severity of trip:', self.severity)
        
        
        
if __name__ == '__main__':
    main()