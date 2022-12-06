'''
Day 25-1: Finding constellations

Here for every star we find the stars that are within range (4D manhattan distance of 3) of them, and 
store them as a set. This takes up the bulk of the runtime.

Then we iterate over the stars, creating a new constellation each time and adding to the constellation set
all stars in range of the first star. We then keep looping over the constellation stars, adding all stars
that are in range of *those* stars, until the constellation stops changing. We remove those stars from
consideration by giving them a constellation number and then create the next constellation, until there are 
no stars left.

Speed of code here isn't super efficient (a few seconds) but works fairly well.

As per tradition, there is no part 2 here. 
''' 

import copy

def main():
    with open('day25/25-1-input.txt', 'r') as open_file:
        stars = open_file.read().split('\n')
    
    cluster = Cluster(stars)
    cluster.find_constellations()
    print(len(cluster.constellations.keys()))

class Cluster:
    def __init__(self, star_data):
        self.stars = []
        self.constellations = {}
        for s in star_data:
            s_int = list(map(int, s.split(',')))
            self.stars.append(Star(s_int[0], s_int[1], s_int[2], s_int[3]))
        self.find_closest()

    def find_closest(self):
        for star in self.stars:
            star.stars_in_range = set([s for s in self.stars if s != star and star.check_in_range(s)])

    def find_constellations(self):
        unattached_stars = self.stars
        i = 0
        while len(unattached_stars) > 0:
            i += 1
            print(f'Creating constellation {i}')
            self.constellations[i] = set([unattached_stars[0]])
            changing = True
            while changing:
                changing = False
                check_set = len(self.constellations[i])
                for star in list(self.constellations[i]):
                    self.constellations[i] |= star.stars_in_range
                if len(self.constellations[i]) != check_set:
                    changing = True
            
            for star in self.constellations[i]:
                star.constellation = i
            
            unattached_stars = [s for s in self.stars if s.constellation == None]
        

class Star:
    def __init__(self, w, x, y, z, radius=3):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.stars_in_range = set()
        self.constellation = None
    
    def check_in_range(self, star):
        manhattan = abs(star.w - self.w) + abs(star.x - self.x) + abs(star.y - self.y) + abs(star.z - self.z)
        if manhattan <= self.radius:
            return True
        return False

if __name__ == '__main__':
    main()