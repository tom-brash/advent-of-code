import copy

def main():
    with open('day18/18.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    lights = ConwayLights(input_data)
    for _ in range(100):
        lights.update()
    print(lights.count_lights())

class ConwayLights:
    def __init__(self, config):
        self.graph = {}
        self.h = len(config)
        self.w = len(config[0])
        for y, row in enumerate(config):
            for x, c in enumerate(row):
                self.graph[(x, y)] = c

    def update(self):
        new_g = copy.deepcopy(self.graph)
        for y in range(self.h):
            for x in range(self.w):
                current = self.graph[(x, y)]
                on = self.get_on_n(x, y)
                if current == '#':
                    if on < 2 or on > 3:
                        new_g[(x, y)] = '.'
                else:
                    if on == 3:
                        new_g[(x, y)] = '#'
        self.graph = new_g
    
    def get_on_n(self, x, y):
        t = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if self.graph.get((x + i, y + j), '.') == '#':
                    t += 1
        return t
    
    def count_lights(self):
        total = 0
        for y in range(self.h):
            for x in range(self.w):
                if self.graph[(x, y)] == '#':
                    total += 1
        return total
    
    def print_out(self):
        for y in range(self.h):
            row = ''
            for x in range(self.w):
                row += self.graph[(x, y)]
            print(row)

if __name__ == '__main__':
    main()