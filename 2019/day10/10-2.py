import numpy as np
import math
from collections import defaultdict


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

    print('Number of stars: ', len(all_stars))

    origin = np.array([28, 29])
    all_stars = [x for x in all_stars if not (x==origin).all()]  # remove origin from list of stars
    all_vectors = stars_to_vecs(all_stars, origin)

    direction_list = defaultdict(list)

    for vector in all_vectors:
        direction = round(find_direction(vector), 3)
        direction_list[direction].append([vector, np.linalg.norm(vector)])

    all_directions = (sorted(direction_list.keys()))

    for direction in all_directions:
        direction_list[direction].sort(key=lambda x:x[1])

    obliterated_asteroids = []

    stable = False
    while not stable:
        stable = True
        for direction in all_directions:
            if len(direction_list[direction]) > 0:
                obliterated_asteroids.append(direction_list[direction].pop(0))
                stable = False

    voi = obliterated_asteroids[199]  # vector of interest
    aoi = [origin[0] + voi[0][0], origin[1] - voi[0][1]]  # asteroid of interest
    print('The 200th asteroid to be obliterated is located at: ', aoi)
    print('The code is therefore: ', aoi[0] * 100 + aoi[1])


def find_direction(vector):
    # Find direction in degrees of vector where 0 is due North
    init_direction = math.atan2(vector[1], vector[0]) * 180 / math.pi
    normalized_direction = (90 - init_direction) % 360
    return normalized_direction


def stars_to_vecs(stars, origin):
    vectors = []
    for star in stars:
        vectors.append(np.array([star[0] - origin[0], origin[1] - star[1]]))
    return vectors


if __name__ == '__main__':
    main()