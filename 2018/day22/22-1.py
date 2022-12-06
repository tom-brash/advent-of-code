'''
Day 22-1: Finding risk index of cave

The target is sufficiently close that we can evaluate the geologic index and corresponding terrain 
type for every tile between the origin and the target tile naively, and then get the risk index
by summing up the terrain types.
'''

def main():
    with open('day22/22-1-input.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    depth = int(input_data[0].split(' ')[1])
    target = input_data[1].split(' ')[1]
    target = tuple([int(x) for x in target.split(',')])

    cave = Cave(depth, target)
    print(cave.get_risk(cave.target_x, cave.target_y))

class Cave():
    def __init__(self, depth, target):
        self.depth = depth
        self.target_x = target[0]
        self.target_y = target[1]
        self.grid = {}
        self.stage_one_load()
    
    def stage_one_load(self):
        for y in range(self.target_y + 1):
            for x in range(self.target_x + 1):
                g = self.get_geologic_index(x, y)
                e = (g + self.depth) % 20183
                t = e % 3
                self.grid[(x, y)] = {'g': g, 'e': e, 't': t}
    
    def get_risk(self, x, y):
        total = 0
        for y in range(y + 1):
            for x in range(x + 1):
                total += self.grid[(x, y)]['t']
        return total
    
    def get_geologic_index(self, x, y):
        if x == 0 and y == 0:
            return 0
        if x == self.target_x and y == self.target_y:
            return 0
        if y == 0:
            return x * 16807
        if x == 0:
            return y * 48271
        return self.grid[(x - 1, y)]['e'] * self.grid[(x, y - 1)]['e']

if __name__ == '__main__':
    main()