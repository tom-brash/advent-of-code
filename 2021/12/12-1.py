from collections import defaultdict
from collections import deque
import copy

def main():
    with open('12/12.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    routes = defaultdict(list)
    for x in input_data:
        a = x.split('-')[0]
        b = x.split('-')[1]
        routes[a].append(b)
        routes[b].append(a)

    options = []

    sq = deque()

    sq.append((['start'], 1))
    best_distances = {}
    while sq:
        route, d = sq.popleft()
        small_caves = [c for c in route if c.islower()]
        if len(set(small_caves)) != len(small_caves):
            continue
        if route[-1] == 'end':
            options.append(route)
            continue
        route_str = ''.join(route)
        prev_best = best_distances.get(route_str, 10000)
        if d >= prev_best:
            continue
        best_distances[route_str] = d
        for n in routes[route[-1]]:
            next_route = copy.deepcopy(route)
            next_route.append(n)
            sq.append((next_route, d + 1))

    print(len(options))

    
    

class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()