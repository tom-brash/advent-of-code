from collections import defaultdict
from collections import deque
import re

def main():
    with open('day9/9.txt', 'r') as open_file:
        input_data = open_file.read()

    dmap = DistanceMap(input_data)
    best = 0
    for c in dmap.cities:
        d = dmap.find_shortest_path(c)
        if d > best:
            best = d
    print(best)


class DistanceMap:
    def __init__(self, input_data):
        self.distances = defaultdict(list)
        self.cities = sorted(list(set(re.findall(r'[A-Z][a-zA-Z]+', input_data))))
        distances = input_data.split('\n')
        for c in self.cities:
            for i in distances:
                if c in i:
                    other_cities = re.findall(r'[A-Z][a-zA-Z]+', i)
                    n = int(re.findall(r'\d+', i)[0])
                    other_cities.remove(c)
                    other = other_cities[0]
                    self.distances[c].append((other, n))
    
    def find_shortest_path(self, start):
        dq = deque()
        dq.append((start, 1 << self.cities.index(start), 0))
        target = (1 << len(self.cities)) - 1
        best_distances = {}
        best_achieved = 0
        while dq:
            loc, visited, d = dq.popleft()
            if visited == target:
                if d > best_achieved:
                    best_achieved = d
                continue
            best = best_distances.get((loc, visited), 0)
            if d < best:
                continue
            best_distances[(loc, visited)] = d
            dq.extend(self.get_moves(loc, visited, d))
        return best_achieved
        
    def get_moves(self, loc, visited, d):
        options = self.distances[loc]
        possible_moves = []
        
        for o in options:
            city_bit = 1 <<self.cities.index(o[0])
            if city_bit & visited:
                continue
            else:
                possible_moves.append((o[0], visited | city_bit, d + o[1]))
        return possible_moves


if __name__ == '__main__':
    main()