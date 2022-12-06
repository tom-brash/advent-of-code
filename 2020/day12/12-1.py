'''
DAY 12-1: Process turtle instructions for ferry

The first problem just involves taking instructions like the old turtle instructions.
By keeping track of current direction and location, we can fairly easily process
each instruction as it comes in
'''

def main():
    with open('day12/12-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    instructions = input_data.split('\n')

    location = [0, 0]
    facing = 0

    for i, instruction in enumerate(instructions):
        location, facing = turtle_instruct(instruction, location, facing)
        print(str(i) + ': ' + str(location) + ' facing ' + degree_to_direction(facing))
    
    print(location)
    print(facing)
    print(abs(location[0]) + abs(location[1]))


def turtle_instruct(instruction, location, facing):
    direction = instruction[0]
    value = int(instruction[1:])

    if direction == 'F':
        direction = degree_to_direction(facing)

    if direction == 'N':
        location[1] += value
    if direction == 'S':
        location[1] -= value
    if direction == 'E':
        location[0] += value
    if direction == 'W':
        location[0] -= value
    
    if direction == 'L':
        facing = (facing + value) % 360
    if direction == 'R':
        facing = (facing - value) % 360
    
    return location, facing
    

def degree_to_direction(clockwise_degree_from_east):
    if clockwise_degree_from_east == 0:
        return 'E'
    if clockwise_degree_from_east == 90:
        return 'N'
    if clockwise_degree_from_east == 180:
        return 'W'
    if clockwise_degree_from_east == 270:
        return 'S'

if __name__ == "__main__":
    main()