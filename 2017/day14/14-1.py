import re
from functools import reduce

def main():
    key_string = 'xlqgujun'  # puzzle input
    defrag = Grid(key_string)
    print(defrag.total)

class Grid:
    def __init__(self, key_string):
        self.key_string = key_string
        self.grid = {}
        self.total = 0
        self.check_tiles = []
        self.groups = 0
        for i in range(128):
            primary = self.key_string + '-' + str(i)
            knot_code = self.knot_hash(primary)
            bin_string = self.knot_hash_to_bin(knot_code)
            for j, c in enumerate(bin_string):
                if c == '1':
                    self.grid[(j, i)] = '#'
                    self.total += 1
                    self.check_tiles.append((j, i))
                else:
                    self.grid[(j, i)] = '.'
        print('Grid created')


    def knot_hash_to_bin(self, knot_code):
        vals = [c for c in knot_code]
        bin_string = ''
        for c in vals:
            bin_num = format(int(c, base=16), '04b')
            bin_string += bin_num
        return bin_string

    def find_groups(self):
        print(f'Groups found: {self.groups}... Remaining active tiles: {len(self.check_tiles)}')
        while len(self.check_tiles) > 0:
            self.find_group(self.check_tiles[0])

    def find_group(self, tile):
        queue = [tile]
        group = []
        while len(queue) > 0:
            x = queue.pop(0)
            group.append(x)
            new_tiles = [self.move(x, i) for i in range(4) if self.grid.get(self.move(x, i), '.') == '#']
            new_tiles = [t for t in new_tiles if t not in queue and t not in group]
            queue.extend(new_tiles)
        
        self.groups += 1
        for t in group:
            self.check_tiles.remove(t)
    
    def move(self, tile, d):
        vecs = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}
        vec = vecs[d]
        destination = (tile[0] + vec[0], tile[1] + vec[1])
        # destination = self.grid.get(check_tile, '.')
        return destination

    def knot_hash(self, in_string):
        instructions = [ord(c) for c in in_string]
        instructions.extend([17, 31, 73, 47, 23])
        instructions = instructions * 64

        s = {x:x for x in range(256)}

        current = 0
        skip = 0

        # sparse hash
        for i in instructions:
            marks = list(range(current, current + i))
            seq = [s[x % 256] for x in marks]
            for x, m in enumerate(marks):
                s[m % 256] = seq[-(x + 1)]
            
            current = (current + i + skip) % 256
            skip += 1

        # dense hash

        encoded_string = ''
        for i in range(16):
            vals = [s[x] for x in range(i * 16, (i + 1) * 16)]
            res = reduce(lambda x, y: x ^ y, vals)
            hex_string = format(res, '02x')
            encoded_string += hex_string

        return(encoded_string)
        
        
if __name__ == '__main__':
    main()
