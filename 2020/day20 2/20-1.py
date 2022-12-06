import re
from collections import defaultdict

def main():
    with open('day20 2/20.txt') as open_file:
        input_data = open_file.read()
    
    tile_data = input_data.split('\n\n')
    tiles = []

    for t in tile_data:
        
        id = int(re.search(r'\d+', t.split('\n')[0]).group(0))
        tiles.append(Tile(id, t.split('\n')[1:]))
        reverse_t = [x[::-1] for x in t.split('\n')[1:]]
        tiles.append(Tile(id, reverse_t))
    
    jigsaw = Jigsaw(tiles)
    jigsaw.assemble_jigsaw()

class Jigsaw:
    def __init__(self, tiles):
        self.tiles = tiles
        self.grid = defaultdict(dict)
        self.n = int((len(tiles) / 2) ** 0.5)
    
    def assemble_jigsaw(self):
        self.start_jigsaw()
        for i in range(self.n - 1):
            found = False
            current = self.grid[0][i]
            req = ''.join([x[-1] for x in current.details[::-1]])
            for tile in self.tiles:
                if tile.id == current.id:
                    continue
                for j in range(4):
                    if tile.sides[j] == req:
                        found = True
                        self.grid[0][i + 1] = Tile(tile.id, self.rot(tile.details, 3 - j))
                        break
                if found == True:
                    break
        
        for i in range(self.n - 1):
            for j in range(self.n):
                found = False
                current = self.grid[i][j]
                req = current.details[-1]
                for tile in self.tiles:
                    if tile.id == current.id:
                        continue
                    for k in range(4):
                        if tile.sides[k] == req:
                            found = True
                            self.grid[i + 1][j] = Tile(tile.id, self.rot(tile.details, k))
                            break
                    if found == True:
                        break



    def start_jigsaw(self):
        for tile in self.tiles:
            valid = set()
            details = tile.details
            for j in range(4):
                req = ''.join([x[-1] for x in details[::-1]])
                for check in self.tiles:
                    if check.id == tile.id:
                        continue
                    for i in range(4):
                        if check.sides[i] == req:
                            valid.add(j)
                            break
                details = self.rot(details, 1)
            
            if len(valid) == 2:
                if 0 in valid and 1 in valid:
                    self.grid[0][0] = tile
                    print(tile.id, valid)
                    break


    def rot(self, tile_details, n):
        for _ in range(n):
            details =  [''.join(list(reversed(x))) for x in zip(*tile_details)]
        return details


class Tile:
    def __init__(self, id, details):
        self.id = id
        self.details = details
        north = self.details[0]
        east = ''.join([x[-1] for x in self.details])
        south = self.details[-1][::-1]
        west = ''.join([x[0] for x in self.details[::-1]])
        self.sides = (north, east, south, west)
        self.corner = False
    
        
    
     


if __name__ == '__main__':
    main()