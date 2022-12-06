from tqdm import tqdm

def main():
    with open('day22/22.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    cluster = Cluster(input_data)
    cluster.run()
    print(f'{cluster.infecting_bursts} bursts of activity caused an infection')


class Cluster():
    def __init__(self, input_data):
        self.grid = {}
        self.c_dict = {'#': 2, '.': 0}
        self.turn_dict = {0: -1, 1: 0, 2: 1, 3: 2}
        for y, row in enumerate(input_data):
            for x, c in enumerate(row):
                self.grid[(x, y)] = self.c_dict[c]
        
        mid = int(len(input_data) / 2)
        self.loc = (mid, mid)
        self.vecs = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
        self.d = 0
        self.infecting_bursts = 0
    
    def burst(self):
        t = self.grid.get(self.loc, 0)
        if t == 1:
            self.infecting_bursts += 1
        self.grid[self.loc] = (t + 1) % 4
        self.d = (self.d + self.turn_dict[t]) % 4

        self.move(self.d)
    
    def run(self, n=10000000):
        for i in tqdm(range(n)):
            self.burst()

    def move(self, d):
        v = self.vecs[d]
        self.loc = (self.loc[0] + v[0], self.loc[1] + v[1])


if __name__ == '__main__':
    main()