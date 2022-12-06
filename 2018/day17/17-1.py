'''
Day 17-1: Flowing wells of water

One of the coolest Day 1 problems I've seen. Here we have water flowing down a groundwell, getting caught in
a number of 'buckets', overflowing, and continuing to sink deeper.

In modeling the behavior, we can observe that water only really has two states:
 - going straight down
 - spreading out left and right, which breaks down again to:
    - when there are barriers on both sides
    - when there is no barrier on at least one side, in which case it will go straight down again.

I chose to use this to model a 'water jet' function, where water goes straight down, and when it impacts, 
spreads out if there are barriers on both sides, and if not, creates one or two more water jets (calling
the function recursively). By repeately calling this water jet function until there are no more changes,
we can get a sense of the end state.

This is one of the few problems I've left the printout on by default, though the window should be made dramatically
smaller if it is to print correctly
'''

import re
from collections import deque
from tqdm import tqdm

def main():
    with open('day17/17-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    instructions = input_data.split('\n')
    well = GroundWell(instructions)
    for i in tqdm(range(1000)):
        well.drop()

    well.print_well()
    well.print_answer()


class GroundWell:
    def __init__(self, instructions):
        self.min_x = 500
        self.max_x = 500
        self.min_y = 100
        self.max_y = 0      
        self.drops = 0  
        self.grid = {}
        self.visited = set()
        r = re.compile(r'(x|y)\=([0-9]+)\,\ (x|y)\=([0-9]+)\.\.([0-9]+)')
        for instruction in instructions:
            m = re.match(r, instruction)
            if m.group(1) == 'x':
                x1 = int(m.group(2))
                x2 = x1 + 1
                y1 = int(m.group(4))
                y2 = int(m.group(5)) + 1
            else:
                y1 = int(m.group(2))
                y2 = y1 + 1
                x1 = int(m.group(4))
                x2 = int(m.group(5)) + 1            
            for x in range(x1, x2):
                for y in range(y1, y2):
                    self.grid[(x, y)] = '#'
            if x1 < self.min_x:
                self.min_x = x1
            if (x2 - 1) > self.max_x:
                self.max_x = (x2 - 1)
            if y1 < self.min_y:
                self.min_y = y1
            if (y2 - 1) > self.max_y:
                self.max_y = (y2 - 1)
    
    def print_answer(self):
        valid_visited = {v for v in self.visited if v[1] >= self.min_y}  # only include the ones that are above min_y (max_y already excluded)
        print(len(valid_visited))

    def print_well(self, x_range=None, y_range=None):
        if x_range == None:
            x_range = (self.min_x - 1, self.max_x + 2)
        if y_range == None:
            y_range = (self.min_y, self.max_y + 1)
        print('min_y:', self.min_y)
        print('max_y:', self.max_y)
        print(f'State after {self.drops} drops')
        print_string = ''
        for y in range(y_range[0], y_range[1]):            
            for x in range(x_range[0], x_range[1]):            
                if (x, y) in self.grid:
                    print_string += self.grid[(x, y)]
                elif (x, y) in self.visited:
                    print_string += '|'
                else:
                    print_string += ' '
            print_string += str(y)
            print_string += '\n'
        print(print_string)

    def drop(self):
        self.launch_jet(500, 0)
        self.stream_set = set()
        self.drops += 1

    def launch_jet(self, x, y):
        impact = self.find_floor(x, y)
        if impact == None:
            visited = set([(x, i) for i in range(y, self.max_y + 1)])  # get the overflow until y > max_y
            self.visited |= visited
            return
        else:
            impact_x, impact_y = impact
            visited = set([(x, i) for i in range(y, impact_y)])  # get all the vertical tiles the water fell
            self.visited |= visited


        visited, new_streams, left_edge, right_edge = self.find_sides(impact_x, impact_y)  # check if there are sides
        self.visited |= visited  # add the spreading water
        if len(new_streams) == 0:
            for x in range(left_edge, right_edge + 1):
                self.grid[(x, impact_y)] = '~'
        else:
            for stream in new_streams:
                if stream not in self.stream_set:
                    self.stream_set.add(stream)
                    self.launch_jet(stream[0], stream[1])
                
    
    def find_sides(self, x, y):  # check what is on the left or right of water impacting something
        visited = set()
        new_streams = []
        left_edge = None
        right_edge = None
        # check left
        x_check = x
        found = False        
        while not found:
            if (x_check, y + 1) not in self.grid:
                new_streams.append((x_check, y + 1))
                found = True
            elif (x_check - 1, y) in self.grid:
                found = True
                left_edge = x_check
            visited.add((x_check, y))
            x_check -= 1
        
        # check right
        x_check = x
        found = False
        while not found:
            if (x_check, y + 1) not in self.grid:
                new_streams.append((x_check, y + 1))
                found = True
            elif (x_check + 1, y) in self.grid:
                found = True
                right_edge = x_check
            visited.add((x_check, y))
            x_check += 1
        
        return visited, new_streams, left_edge, right_edge
    
    def find_floor(self, x, y):
        while True:
            y += 1
            if (x, y) in self.grid:
                return (x, y - 1)
            if y > self.max_y:
                return None
    

if __name__ == '__main__':
    main()