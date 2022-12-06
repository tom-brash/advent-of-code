import numpy as np

def main():
    with open('10-1-input.txt', 'r') as input_file:
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

    print('Number of stars: ', len(all_stars))

    for i, star in enumerate(all_stars):
        print('testing star ', i)
        origin = star
        all_vectors = stars_to_vecs(all_stars, origin)
        visible_stars = []

        for vector in all_vectors:
            visible_stars.append(check_visible(vector, all_vectors))
        num_visible = sum(visible_stars)

        if (num_visible - 1) > max_visible:
            max_visible = num_visible - 1  # not including the asteroid that the station is on
            best_location = origin

        print('Current best: ', max_visible, ' at ', best_location)

    print(max_visible)
    print(best_location)

    # Best answer: 340 stars visible at [28 29]


def stars_to_vecs(stars, origin):
    vectors = []
    for star in stars:
        vectors.append(star - origin)
    return vectors


def check_visible(check_vector, vector_list):
    visible = True
    for vector in vector_list:
        if (check_vector == vector).all():  # check that we aren't checking vector against itself
            continue

        # if vectors are parallel...
        if np.cross(check_vector, vector) == 0:
            # and reference vector is closer to the origin...
            if np.linalg.norm(vector) < np.linalg.norm(check_vector):
                # and reference vector is on the same side as the check vector...
                if np.sign(check_vector[0]) == np.sign(vector[0]) and np.sign(check_vector[1]) == np.sign(vector[1]):
                    # check vector is a star that is not visible from the origin
                    visible = False

    return visible

if __name__ == '__main__':
    main()