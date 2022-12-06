import numpy as np


def main():
    with open('day3/3-1-input.txt','r') as input_file:
        input_data = input_file.read()

    input_lines = input_data.split('\n')  # separate into two distinct wires

    line_1 = input_lines[0].split(',')  # split each wire into individual instructions
    line_2 = input_lines[1].split(',')

    # split each wire into a series of orthogonal line segments (horizontal or vertical)
    # note segments are all, by convention, left to right / bottom to top
    segments_1 = input_to_line_segments(line_1)
    segments_2 = input_to_line_segments(line_2)

    # identify intersection between two sets of segments
    # only intersections between horizontal and vertical segments considered
    intersections = identify_intersections(segments_1, segments_2)

    # identify closest intersection using manhattan distance from origin
    closest = np.inf
    for intersection in intersections:
        distance = np.abs(intersection[0]) + np.abs(intersection[1])
        if distance < closest:
            closest = distance

    print(closest)


def input_to_line_segments(line_data):
    segments = []
    starting_point = np.array([0,0])

    dmap = {'U':np.array([1,0]),  # dictionary notes what direction movement should be in along [x, y] axis
            'D':np.array([-1,0]),
            'L':np.array([0,-1]),
            'R':np.array([0,1])}

    for line in line_data:
        direction = line[0]
        distance = int(line[1:])
        ending_point = starting_point + dmap[direction] * np.array([distance, distance])

        # add segments. By convention, segments are added as left to right and down to up to simplify later calcs
        if starting_point[0] < ending_point[0] or starting_point[1] < ending_point[1]:
            segments.append([starting_point, ending_point])
        else:
            segments.append([ending_point, starting_point])

        starting_point = ending_point

    return segments


def identify_intersections(segments_1, segments_2):
    intersections = []
    for i in segments_1:
        # check orientation of line segment 1
        if i[0][0] == i[1][0]:
            orient_i = 'v'
        else:
            orient_i = 'h'

        for j in segments_2:
            # check orientation of line segment 2
            if j[0][0] == j[1][0]:
                orient_j = 'v'
            else:
                orient_j = 'h'

            if orient_i == orient_j:
                continue  # do not look for intersection between two vertical lines or two horizontal lines

            # otherwise, check to see if line segments intersect
            elif orient_i == 'v':
                if j[0][1] >= i[0][1] and j[1][1] <= i[1][1] and j[0][0] <= i[0][0] <= j[1][0]:
                    intersections.append([i[0][0], j[0][1]])
            elif orient_i == 'h':
                if j[0][0] >= i[0][0] and j[1][0] <= i[1][0] and j[0][1] <= i[0][1] <= j[1][1]:
                    intersections.append([i[0][1], j[0][0]])

    return intersections


if __name__ == '__main__':
    main()