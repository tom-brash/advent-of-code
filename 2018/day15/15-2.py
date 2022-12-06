'''
Day 15-1: Of Goblins and Elves

Wow. Quite the dramatic step up from previous days - this one took several hours, in
part because of the complexity of the rules.

Multiple attempts to memoize or otherwise make this more efficient were discarded, partly
because BFS turns out to be plenty fast enough, but also because movements depend on the
positions of other units, making the 'grid' unique each time.

After initializing the cavern, BFS is used to determine the closest target. In order, the 
tiebreaks used are:
 - Distance to target
 - Reading order of target cell
 - Reading order of potential move

For attacks, the following tiebreaks are used (in order):
 - remaining HP
 - reading order of unit


'''
from collections import deque

def main():
    with open('day15/15-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    input_data = input_data.split('\n')
    
    victory_found = False
    handicap = 0
    while not victory_found:
        cavern = Cavern(input_data, handicap)
        while cavern.state == 'ongoing':
            cavern.take_turn()
        if cavern.state == 'complete':
            victory_found = True
            cavern.print_grid()
        else:
            handicap += 1

    # cavern = Cavern(input_data)
    # while cavern.state == 'ongoing':
    #     cavern.take_turn()
    
# create cavern class to manage units and movement
class Cavern:
    def __init__(self, grid_data, handicap=0):
        self.width = len(grid_data[-1])
        self.height = len(grid_data)
        self.traversable = {}  # grid of traversable tiles and links between them
        self.units = []
        self.grid = {}  # current positions of cavern
        self.turns_taken = 0
        self.state = 'ongoing'
        self.handicap = handicap
        for y, row in enumerate(grid_data):
            for x, c in enumerate(row):
                if c == ' ':
                    break
                if c == 'G':
                    self.units.append(Unit(x, y, c))                
                if c == 'E':
                    self.units.append(Unit(x, y, c, attack=3 + handicap))
                if c != '#':
                    self.traversable[(x, y)] = []
                self.grid[(x, y)] = c
        
        for loc in self.traversable:  # add possible moves to the traversable dictionary for rapid access
            self.traversable[loc].extend([self.move(loc, d) for d in range(4) if self.move(loc, d) in self.traversable])

    # take a position and move it by a cardinal vector
    def move(self, loc, d):
        vector_dict = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        x, y = loc
        return (x + vector_dict[d][1], y + vector_dict[d][0])
    
    # take an entire turn (move all units in turn)
    def take_turn(self):
        self.units.sort(key=lambda u: (u.y, u.x))  # sort units in reading order
        alive_units = [u for u in self.units if u.status == 'alive']  # don't take turns for dead units
        for i, unit in enumerate(alive_units):
            self.move_unit(unit)
            if i < (len(alive_units) - 1):  # if this is the final unit, the turn should be ended before checking state
                self.check_state()
        self.turns_taken += 1
        self.check_state()

    # check if the simulation is complete
    def check_state(self):
        if self.state == 'failure':
            return
        
        if self.state == 'complete':
            return
        units_alive = [u for u in self.units if u.status == 'alive']
        goblins = [u for u in units_alive if u.type == 'G']
        elves = [u for u in units_alive if u.type == 'E']
        if len(goblins) == 0:
            self.report_answer('E')
            self.state = 'complete'
        if len(elves) == 0:
            self.report_answer('G')
            self.state = 'complete'
    
    # if the simulation is complete, report an answer
    def report_answer(self, unit_type):
        total_hp = sum([u.hp for u in self.units if u.type == unit_type and u.status == 'alive'])
        print('Final answer: ', total_hp * self.turns_taken)
        print('Rounds completed:', self.turns_taken)
        print('Total hp remaining:', total_hp)

    # move a single unit
    def move_unit(self, unit):
        # if a unit is dead (since the start of the turn), do nothing
        if unit.status == 'dead':
            return

        # get list of all enemies
        enemies = [e for e in self.units if e.type != unit.type and e.status == 'alive']
        
        # Check if we are already in position to attack something
        adjacent_spaces = [self.move((unit.x, unit.y), d) for d in range(4) if self.move((unit.x, unit.y), d) in self.traversable]
        adjacent_enemies = [e for e in enemies if (e.x, e.y) in adjacent_spaces]

        # Attack and end the move if there is a neighboring enemy
        if len(adjacent_enemies) > 0:
            self.attack_command(unit, adjacent_enemies)             
            return

        # Otherwise move closer to an enemy

        # Find target squares
        targets = set([self.move((e.x, e.y), d) for e in enemies for d in range(4) if self.grid[self.move((e.x, e.y), d)] == '.' ])
        if len(targets) == 0:
            return  # if there are no valid targets, don't bother moving

        # breadth first search
        best_distance = 10000
        best_target = (300, 300)
        best_move = None
        possible_moves = [x for x in adjacent_spaces if self.grid[x] == '.']
        possible_moves.sort(key=lambda m: (m[1], m[0]))  # sort moves according to reading order
        for move in possible_moves:
            sq = deque()
            sq.append(move + (0,))  # format (x, y, d)
            best_states = {}
            
            while sq:
                x, y, d = sq.popleft()
                if self.grid[(x, y)] != '.':
                    continue
                if d > best_distance:  # if we are over the best distance achieved, cut off branch
                    continue
                if (x, y) in targets:
                    if d <= best_distance:
                        if d < best_distance:  # if distance is strictly better, update best
                            best_target = (x, y)
                            best_distance = d
                            best_move = move
                        elif self.compare_reading_order((x, y), best_target) == 1:  # if a better target can be reached in same number of moves, update
                            best_target = (x, y)
                            best_distance = d
                            best_move = move
                        # do not break here as there may be other possible targets
                    
                previous_best = best_states.get((x, y), 1000000)
                if d >= previous_best:
                    continue
                best_states[(x, y)] = d
                sq.extend([x + (d + 1,) for x in self.traversable[(x, y)]])
        
        if best_move != None:  # move unit
            new_x, new_y = best_move
            self.grid[(unit.x, unit.y)] = '.'
            unit.x = new_x
            unit.y = new_y            
            self.grid[(new_x, new_y)] = unit.type
        
        # check for possible attacks again
        adjacent_spaces = [self.move((unit.x, unit.y), d) for d in range(4) if self.move((unit.x, unit.y), d) in self.traversable]
        adjacent_enemies = [e for e in enemies if (e.x, e.y) in adjacent_spaces]

        # Attack and end the move if there is a neighboring enemy
        if len(adjacent_enemies) > 0:
            self.attack_command(unit, adjacent_enemies)

    # attack an enemy according to predetermined tiebreakers
    def attack_command(self, unit, adjacent_enemies):
        adjacent_enemies.sort(key=lambda e: (e.hp, e.y, e.x))  # sort by HP, then by reading order
        targeted_enemy = adjacent_enemies[0]
        targeted_enemy.hp -= unit.attack
        if targeted_enemy.hp <= 0:  # destroy enemy if <0 health
            self.grid[(targeted_enemy.x, targeted_enemy.y)] = '.'
            targeted_enemy.status = 'dead'
            if targeted_enemy.type == 'E':
                self.state = 'failure'
                print('Elf died with an attack of', targeted_enemy.attack)      

    # check if t1 is strictly earlier in reading order than t2, otherwise return 0
    def compare_reading_order(self, t1, t2):
        if t1[1] < t2[1]:
            return 1
        if t2[1] < t1[1]:
            return 0
        # if y is equal...
        if t1[0] < t2[0]:
            return 1
        return 0

    # print out current state of grid
    def print_grid(self):
        print('State after', self.turns_taken, 'rounds')
        print_string = ''
        for y in range(self.height):
            for x in range(self.width):
                print_string += self.grid[(x, y)]
            print_string += '\n'
        
        print(print_string)
    
# create a unit, storing position, type, health, and attack
class Unit:
    def __init__(self, x, y, type, attack=3):
        self.type = type
        self.x = x
        self.y = y
        self.attack = attack
        self.hp = 200
        self.status = 'alive'


if __name__ == '__main__':
    main()