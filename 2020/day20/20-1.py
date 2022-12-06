'''
DAY 20-1: Finding jigsaw corners

Through some experimentation, one of the keys to this puzzle is that every side can meet
with exactly one other side, much like a real jigsaw puzzle. As a result, we don't
need to try multiple configurations to find the 'single' working version, we just need 
to find which pieces do in fact fit together.

The first part of the puzzle only involves finding the corners. We can do this by just
finding the jigsaw pieces that only have two other connections. Multiplying them
together gives the answer

Codebase here very unoptimized
'''

import re
import pprint

def main():
    with open('day20/20-1-input.txt', 'r') as input_file:
        input_data = input_file.read()
    
    tile_data = input_data.split('\n\n')
    tile_dict = tiles_to_dict(tile_data)

    tile_dict = find_matches(tile_dict)

    corners = []
    for tile in tile_dict:
        check = len(tile_dict[tile]['matches'])
        if check == 4:
            corners.append(tile)
    
    total = 1
    for corner in corners:
        total *= int(corner)
    print(total)
    print(corners)
        

# turn the input into a dictionary. Reversed sides are counted as extra possible 'sides'
def tiles_to_dict(tile_data):
    tile_dictionary = {}
    for tile in tile_data:
        tile_num = re.search(r'([0-9]+)\:', tile).group(1)
        side_0 = tile.split('\n')[1]
        side_1 = get_side(tile, 'right')
        side_2 = tile.split('\n')[-1]
        side_3 = get_side(tile, 'left')
        side_0f = side_0[::-1]
        side_1f = side_1[::-1]
        side_2f = side_2[::-1]
        side_3f = side_3[::-1]
        available_orientations = ['1', '2', '3', '4', '1F', '2F', '3F', '4F']
        sides = [side_0, side_1, side_2, side_3, side_0f, side_1f, side_2f, side_3f]
        tile_dictionary[tile_num] = {'sides': sides, 'available_orientations':available_orientations}
    return tile_dictionary
        

# find the matches to sides of other tiles
def find_matches(tile_dict):
    for key in tile_dict.keys():
        possible_matches = []
        key_sides = tile_dict[key]['sides']
        for j, k_side in enumerate(key_sides):
            for key_s in tile_dict.keys():
                if key != key_s:
                    for i, side in enumerate(tile_dict[key_s]['sides']):
                        if k_side == side:
                            possible_matches.append((j, key_s, i))
        tile_dict[key]['matches'] = possible_matches
    return tile_dict


# helper tool to get a left or right side from input
def get_side(tile, orientation):
    if orientation == 'left':
        i = 0
    else:
        i = -1
    side = ''
    for j in tile.split('\n')[1:]:
        side += j[i]
    return side


if __name__ == "__main__":
    main()