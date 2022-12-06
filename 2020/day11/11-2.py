'''
DAY 11-2: Determine which airport seats remain empty in stable state (new rules)

The difference now is that the definition of 'adjacent seats' has changed. We
could accomplish this by just updating the find_adjacent_seats function from 11-1, but 
given that this will be somewhat more expensive than just the nearest 8 seats (as it 
will involve searching in each direction for a seat), we'd rather avoid doing this operation
every time we go over a seat. The visible seats from each seat will never change, after all.

We set up a dictionary at the start and fill it with the seats that are visible from each
seat. Then we loop through pretty much the same way as in 11-1.
'''

import copy
import pprint


def main():
    with open('day11/11-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    seats = input_data.split('\n')
    for i, seat_row in enumerate(seats):
        seats[i] = [char for char in seat_row]

    visible_dictionary = create_visible_dictionary(seats)

    stable = False
    while stable == False:
        stable, seats = update_all_seats(seats, visible_dictionary)
    
    print_seats(seats)
    print(count_occupied(seats))
      

def count_occupied(seats):
    occupied = 0
    for seat_row in seats:
        for char in seat_row:
            if char == '#':
                occupied += 1
    return occupied


def print_seats(seats):
    for seat_row in seats:
        print (''.join(seat_row))


def update_all_seats(seats, visible_dictionary):
    updated_seats = copy.deepcopy(seats)
    for y, seat_row in enumerate(seats):
        for x, seat in enumerate(seat_row):
            adjacent_seats = find_adjacent(y, x, seats, visible_dictionary)
            updated_seats[y][x] = update_seat(seat, adjacent_seats)
    
    stable = updated_seats == seats
    return stable, updated_seats


def create_visible_dictionary(seats):
    visible_dictionary = {}
    
    directions = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i !=0 or j != 0:
                directions.append((i, j))
    
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            visible_dictionary[(y, x)] = find_visible_seats(y, x, seats, directions)

    return visible_dictionary


def find_visible_seats(y, x, seats, directions):
    visible_seats = []
    for direction in directions:
        visible_found = False
        check_vector = [0, 0]
        while visible_found == False:
            check_vector[0] += direction[0]
            check_vector[1] += direction[1]
            if y + check_vector[0] < 0 or y + check_vector[0] >= len(seats) or x + check_vector[1] < 0 or x + check_vector[1] >= len(seats[0]):
                visible_found = True
                visible_seats.append(None)
            elif seats[y + check_vector[0]][x + check_vector[1]] != '.':
                visible_found = True
                visible_seats.append((y + check_vector[0], x + check_vector[1]))
    return visible_seats
                

def find_adjacent(y, x, seats, visible_dictionary):
    adjacent_seats = []
    visible_seats = visible_dictionary[(y, x)]
    for seat in visible_seats:
        if seat == None:
            adjacent_seats.append('.')
        else:
            y = seat[0]
            x = seat[1]
            adjacent_seats.append(seats[y][x])
                
    return adjacent_seats

def update_seat(seat_state, adjacent_seats):
    filled_adjacent = 0
    for seat in adjacent_seats:
        if seat == '#':
            filled_adjacent += 1
    
    if seat_state == "#":
        if filled_adjacent >= 5:
            return 'L'
    
    if seat_state == 'L':
        if filled_adjacent == 0:
            return '#'
    
    return seat_state
        

if __name__ == "__main__":
    main()