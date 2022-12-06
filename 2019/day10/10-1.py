# same problem as previous done through using directions
# taking advantage of the fact that every unblocked direction will represent a single observable asteroid
# this version gets to the same answer, but has greater than a 100x speed increase

import numpy as np
from collections import defaultdict
import math


def main():
    with open('day10/10-1-input.txt', 'r') as input_file:
        input_data = input_file.read()

    input_rows = input_data.split('\n')
    input_rows.remove('')

    all_stars = []
    for y, row in enumerate(input_rows):
        for x, val in enumerate(row):
            if val == '#':
                all_stars.append(np.array([x, y]))

    max_visible = 0
    best_location = np.array([0,0])

    for i, star in enumerate(all_stars):
        origin = star
        all_vectors = stars_to_vecs(all_stars, origin)
        all_vectors = [x for x in all_vectors if not (x == origin).all()]
        direction_list = defaultdict(list)

        for vector in all_vectors:
            direction = round(find_direction(vector), 3)
            direction_list[direction].append([vector, np.linalg.norm(vector)])

        num_visible = len(direction_list.keys())

        if num_visible > max_visible:
            max_visible = num_visible  # not including the asteroid that the station is on
            best_location = origin

    print('Maximum number of visible asteroids:', max_visible)
    print('Best location for the space station:', best_location)

    # Best answer: 340 stars visible at [28 29]


def stars_to_vecs(stars, origin):
    vectors = []
    for star in stars:
        vectors.append(star - origin)
    return vectors


def find_direction(vector):
    # Find direction in degrees of vector where 0 is due North
    init_direction = math.atan2(vector[1], vector[0]) * 180 / math.pi
    normalized_direction = (90 - init_direction) % 360
    return normalized_direction


if __name__ == '__main__':
    main()