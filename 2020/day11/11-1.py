'''
DAY 11-1: Determine which airport seats remain empty in stable state

We can accomplish this through a variety of helper functions. We basically
want to loop over every position, get a list of the 8 adjacent seats, and 
update the seats accordingly to the rules provided (fill if no filled seats
adjacent, empty if 4 or more adjacent seats are full).

Once the system stops updating, we can count and return the occupied seats.

To produce output and compare it against test results, we make a helper 
function to print the final (or intermediate) seat configurations in a neat
way
'''

import copy
def main():
    with open('day11/11-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    seats = input_data.split('\n')
    for i, seat_row in enumerate(seats):
        seats[i] = [char for char in seat_row]

    stable = False
    while stable == False:
        stable, seats = update_all_seats(seats)
    
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


def update_all_seats(seats):
    updated_seats = copy.deepcopy(seats)
    for y, seat_row in enumerate(seats):
        for x, seat in enumerate(seat_row):
            adjacent_seats = find_adjacent(y, x, seats)
            updated_seats[y][x] = update_seat(seat, adjacent_seats)
    
    stable = updated_seats == seats
    return stable, updated_seats


def find_adjacent(y, x, seats):
    adjacent_seats = []
    for i in [-1, 0, 1]:
        if y + i >= 0 and y + i < len(seats):
            for j in [-1, 0, 1]:
                if x + j >= 0 and x + j < len(seats[0]):
                    if (i != 0 or j != 0):
                        adjacent_seats.append(seats[y + i][x + j])
    return adjacent_seats

def update_seat(seat_state, adjacent_seats):
    filled_adjacent = 0
    for seat in adjacent_seats:
        if seat == '#':
            filled_adjacent += 1
    
    if seat_state == "#":
        if filled_adjacent >= 4:
            return 'L'
    
    if seat_state == 'L':
        if filled_adjacent == 0:
            return '#'
    
    return seat_state
        

if __name__ == "__main__":
    main()