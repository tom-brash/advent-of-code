'''
Day 13-1: Mine carts

A very neat problem, based on carts going around cavern tracks and taking different
decisions at each intersection. As long as carts are created as separate classes, this
doesn't turn out to be difficult - each one can keep track of its last decision.

The initial code is slightly cumbersome in both 'laying tracks' underneath carts and defining
corner behavior manually - but it works out well in the end. Collisions need to be checked for
after every move, rather than at the end of each 'tick'
'''

def main():
    with open('day13/13-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    input_data = input_data.split('\n')

    cart_track = CartTrack(input_data)
    while not cart_track.collision:
        cart_track.cycle()
    

class CartTrack:
    def __init__(self, grid_data):
        self.grid = {}
        self.carts = []
        underlying = {'>': '-', '<': '-', '^': '|','v': '|'}
        direction = {'>': 1, '<': 3, '^': 0,'v': 2}
        for y, row in enumerate(grid_data):
            for x, c in enumerate(row):
                if c in underlying:
                    self.grid[(x, y)] = underlying[c]
                    self.carts.append(Cart(x, y, direction[c]))
                else:
                    self.grid[(x, y)] = c
        self.moves_made = 0
        self.collision = False

    def cycle(self):
        self.carts.sort(key=lambda c: (c.y, c.x))
        for cart in self.carts:
            tile = self.grid[(cart.x, cart.y)]
            cart.step(tile)
            self.collision_check()
        self.moves_made += 1
    
    def collision_check(self):
        cart_locs = set()
        for cart in self.carts:
            loc = (cart.x, cart.y)
            if loc in cart_locs:
                print('Collision found at:', loc, 'after', self.moves_made, 'moves')
                self.collision = True
                return 1
            cart_locs.add(loc)
    
        
class Cart:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.turn_count = 0
        self.v_dict = {3: (-1, 0), 1: (1, 0), 0: (0, -1), 2: (0, 1)}
    
    def step(self, tile):
        if tile == '\\':
            self.d = (3 - self.d) % 4
        elif tile == '/':
            self.d = (1 - self.d) % 4
        elif tile == '+':
            cycle_turn = self.turn_count % 3
            if cycle_turn == 0:
                self.d = (self.d - 1) % 4
            elif cycle_turn == 2:
                self.d = (self.d + 1) % 4
            self.turn_count += 1            
        
        vec = self.v_dict[self.d]
        self.x += vec[0]
        self.y += vec[1]
        

if __name__ == '__main__':
    main()

