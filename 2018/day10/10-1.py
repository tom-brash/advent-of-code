'''
Day 10-1: Tracking the movement of stars

Here we create a number of star objects and track their position.
As we are not given numerical information about what the final picture
might look like (the stars could even be several spaces apart in the final
picture) this requires some experimentation.

However, we can assume that in the final state the stars will be very close
to each other. The Constellation class builds in a method to check the 
x and y range of the stars. When they start getting acceptably low (<300
was trialled) the constellation is printed out (reduced to 80 by experimentation).
'''

import re

def main():
    with open('day10/10-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    star_data = input_data.split('\n')
    constellation = Constellation(star_data)
    found = False
    while not found:
        constellation.step()
        dims = constellation.max_distance()
        if sum(dims) < 80:
            constellation.printout()
            found = True
        

class Constellation:
    def __init__(self, star_data):
        self.stars = []
        r_coord = re.compile(r'position\=\<(\-?[0-9]+)\,(\-?[0-9]+)')
        r_velo = re.compile(r'velocity\=\<(\-?[0-9]+)\,(\-?[0-9]+)')
        for line in star_data:
            line = line.replace(' ','')
            coords = re.search(r_coord, line)
            x = int(coords.group(1))
            y = int(coords.group(2))
            velocity = re.search(r_velo, line)
            x_vel = int(velocity.group(1))
            y_vel = int(velocity.group(2))
            self.stars.append(Star(x, y, x_vel, y_vel))
        self.steps = 0
    
    def step(self):
        for star in self.stars:
            star.x += star.x_vel
            star.y += star.y_vel
        self.steps += 1
    
    def max_distance(self, get_all=False):
        min_x = 1000000
        max_x = -1000000
        min_y = 1000000
        max_y = -1000000
        for star in self.stars:
            if star.x < min_x:
                min_x = star.x
            if star.x > max_x:
                max_x = star.x
            if star.y < min_y:
                min_y = star.y
            if star.y > max_y:
                max_y = star.y

        if get_all:
            return max_x - min_x, max_y - min_y, min_x, min_y
        
        return max_x - min_x, max_y - min_y
    
    def printout(self):
        x_range, y_range, min_x, min_y = self.max_distance(get_all=True)
        rows = []
        row = ['.'] * (x_range + 1)
        for y in range(y_range + 1):           
            rows.append(row.copy())
        for star in self.stars:
            x = star.x - min_x
            y = star.y - min_y
            rows[y][x] = '#'
        
        print('\nPrinting constellation after %d steps...\n' % self.steps)
        for row in rows:
            print(''.join(row))


class Star:
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel


if __name__ == '__main__':
    main()