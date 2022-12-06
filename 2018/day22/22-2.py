'''
Day 22-2: Optimal pathfinding

BFS works here, though it likely isn't ideal. To avoid going infinitely far out in the x_axis 
we also need to put in place some boundaries that may limit the generality of the solution.

On the journey, the BFS keeps track of x and y positions as well as the currently equipped tool and
the time taken

Even so, this solution is slow.
'''

from collections import deque

def main():
    with open('day22/22-1-input.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    depth = int(input_data[0].split(' ')[1])
    target = input_data[1].split(' ')[1]
    target = tuple([int(x) for x in target.split(',')])

    cave = Cave(depth, target)
    cave.pathfind(target)

class Cave():
    def __init__(self, depth, target):
        self.depth = depth
        self.target_x = target[0]
        self.target_y = target[1]
        self.grid = {}
        self.equipment = {0: [1, 2], 1: [0, 1], 2: [0, 2]}
        self.stage_one_load()
    
    def stage_one_load(self):        
        for y in range(self.target_y + 500):
            for x in range(self.target_x + 500):
                g = self.get_geologic_index(x, y)
                e = (g + self.depth) % 20183
                t = e % 3
                self.grid[(x, y)] = {'g': g, 'e': e, 't': t}
    
    def pathfind(self, target):
        best_time = 1200
        best_states = {}
        sq = deque()
        sq.append((0, 0, 2, 0))  # format x, y, equipment, time

        while sq:
            x, y, e, t = sq.popleft()
            # if x < 0 or y < 0:
            #     continue
            if t >= best_time:
                continue
            if x >= 100:
                continue
            # if y == 785:
            #     print('hi')
            if (x, y) == target:
                if e != 2:
                    t += 7
                if t < best_time:
                    best_time = t
                continue
            previous_best = best_states.get((x, y, e), 100000)
            if t >= previous_best:
                continue
            else:
                best_states[(x, y, e)] = t
            sq.extend(self.possible_moves(x, y, e, t))
        
        print('Best time to target:', best_time)
    
    def possible_moves(self, x, y, equip, time):
        terrain = self.grid[(x, y)]['t']
        possible_states = []
        for vec in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x = x + vec[0]
            next_y = y + vec[1]
            if next_x < 0 or next_y < 0:
                continue
            next_terrain = self.grid[(next_x, next_y)]['t']
            if equip in self.equipment[next_terrain]:
                possible_states.append((next_x, next_y, equip, time + 1))
            else:
                possible_states.extend([(next_x, next_y, e, time + 8) for e in self.equipment[next_terrain] if e in self.equipment[terrain]])
        return possible_states





    
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