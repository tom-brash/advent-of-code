'''
Day 13-2: Exploding mine carts

The bones of the code are left largely unchanged from Part 1, except that now carts 
are removed when they crash. Given we are looking for collisions in any case as Part 1,
this is fairly straightforward to do.
'''

def main():
    with open('day13/13-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    input_data = input_data.split('\n')

    cart_track = CartTrack(input_data)
    while cart_track.alive:
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
        self.alive = True

    def cycle(self):
        self.carts.sort(key=lambda c: (c.y, c.x))
        for cart in self.carts:
            tile = self.grid[(cart.x, cart.y)]
            cart.step(tile)
            self.collision_check()
        self.moves_made += 1
        if len(self.carts) == 1:
            self.alive = False
            print('Final cart located at:', (self.carts[0].x, self.carts[0].y))
    
    def collision_check(self):
        cart_locs = set()
        locs_to_remove = []
        for cart in self.carts:
            loc = (cart.x, cart.y)
            if loc in cart_locs:
                print('Collision found at:', loc, 'after', self.moves_made, 'moves')
                self.collision = True
                locs_to_remove.append(loc)
            cart_locs.add(loc)
        
        if len(locs_to_remove) > 0:
            self.carts = [cart for cart in self.carts if (cart.x, cart.y) not in locs_to_remove]
            print('%d carts remaining!' % len(self.carts))
        
        
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

