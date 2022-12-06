import re
from collections import deque
import itertools
import copy

def main():
    with open('day11/11.txt', 'r') as open_file:
        input_data = open_file.read()
    
    tower = Tower(input_data.split('\n'))
    tower.find_best_path()
    

class Tower:
    def __init__(self, input_data):
        self.start_floors = dict()
        self.total_objects = 0
        self.object_list = []
        self.loc = 1
        for i in range(1, 5):
            self.start_floors[i] = re.findall(r'\w+(?:\-compatible|\ generator)', input_data[i-1])
            self.total_objects += len(self.start_floors[i])
            self.object_list.extend(self.start_floors[i])
        self.object_list = tuple(sorted(self.object_list))

    def find_best_path(self):
        best_total = 1000000
        iterations = 0
        best_states = {}
        sq = deque()
        sq.append((1, self.start_floors, 0)) 
        while sq:
            iterations += 1
            loc, floors, d = sq.popleft()
            if iterations % 10000 == 0:    
                print(iterations, d)
            if d >= best_total:
                continue
            floor_string = self.string_rep(floors)
            if loc == 4:
                if len(floors[4]) == self.total_objects:
                    print(f'Took {d} steps to move all objects to fourth floor')
                    best_total = d
                                
            previous_best = best_states.get((loc, floor_string), 1000000)
            if d >= previous_best:
                continue
            best_states[(loc, floor_string)] = d
            sq.extend(self.possible_moves(loc, floors, d))
            if iterations % 10000 == 0:
                print(f'Current queue length after {iterations} iterations...{len(sq)}')
                sq_list = list(sq)
                seen = set()
                sq_list = [(loc, floors, d) for loc, floors, d in sq_list if not ((loc, self.string_rep(floors), d) in seen or seen.add((loc, self.string_rep(floors), d)))]
                sq = deque(sq_list)
                print(f'After cleaning, queue length...{len(sq)}')
                # sq_list = list(sq)
                # sq_list.sort(key = lambda x: self.string_rep(x[1], score=True), reverse=True)
                # sq = deque(sq_list)
        print('Queue empty!')


    def possible_moves(self, loc, floors, d):
        possible_moves = []
        movable_items = floors[loc]
        for i in movable_items:
            if loc < 4:
                temp_floors_u = copy.deepcopy(floors)
                temp_floors_u[loc].remove(i)
                temp_floors_u[loc + 1].append(i)
                possible_moves.append((loc + 1, temp_floors_u, d + 1))
            if loc > 1:
                temp_floors_d = copy.deepcopy(floors)
                temp_floors_d[loc].remove(i)
                temp_floors_d[loc - 1].append(i)
                possible_moves.append((loc - 1, temp_floors_d, d + 1))
        
        for c in list(itertools.combinations(movable_items, 2)):
            if loc < 4:
                temp_floors_u = copy.deepcopy(floors)
                temp_floors_u[loc] = [x for x in temp_floors_u[loc] if x not in c]
                temp_floors_u[loc + 1].extend(list(c))
                possible_moves.append((loc + 1, temp_floors_u, d + 1))
            if loc > 1:
                temp_floors_d = copy.deepcopy(floors)
                temp_floors_d[loc] = [x for x in temp_floors_d[loc] if x not in c]
                temp_floors_d[loc - 1].extend(list(c))
                possible_moves.append((loc - 1, temp_floors_d, d + 1))
        
        possible_moves = [f for f in possible_moves if self.check_legal(f) == True]
        # possible_moves.sort(key = operator.itemgetter(0), reverse=True)
        return possible_moves
    

    def check_legal(self, move):
        _, floors, _ = move
        for f in range(1, 5):
            current_items = [re.split(r'\-|\ ', x) for x in floors[f]]
            current_chips = [x[0] for x in current_items if x[1] == 'compatible']
            current_gens = [x[0] for x in current_items if x[1] == 'generator']
 
            
            for c in current_chips:
                if c in current_gens:
                    continue
                if len(current_gens) > 0:
                    return False
        return True
        
    
    def string_rep(self, floors, score=False):
        s = [0] * self.total_objects
        for i, e in enumerate(self.object_list):
            for f in range(1, 5):
                if e in floors[f]:
                    s[i] = f
                    break

        if score == True:
            s = [int(x) for x in s]
            return sum(s)
        
        s = [(s[i], s[i+1]) for i in range(0, len(s), 2)]
        s.sort()
        return tuple(s)


# class Device:
#     def __init__(self, e, d_type):
#         self.element = e
#         self.d_type = d_type


if __name__ == '__main__':
    main()