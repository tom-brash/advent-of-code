'''
DAY 25-1: (Intcode) Text Adventure 

This is a little unlike other problems as the Intcode machine creates a short text adventure. As the intent
appeared to be to actually play it (given the amount of flavor text etc) a hybrid approach was used here.
First the space was mapped, manually looking around the adventure space, and all of the possible items 
identified (excluding trap items which end the game immediately).

The final door needs some arbitrary combination of items. Once getting to the door, we switch back to a 
programmatic approach to avoid having to search through a lot of combinations.

To rapidly play the game and get the answer, cheat codes have been added, as follows:
    - are we there yet?: from the opening state, skip immediately to door with all items in possession
    - try ALL the things!: brute force the door (assuming all items are currently held)
    - up up etc.: reference to the Konami code, from the opening state win the game with maximum efficiency

There is no part 2 to this day (part 2 is getting the other 48 stars on previous days)
''' 
import sys
import os
import pprint
import itertools
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day25/25-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    starting_memory = [int(x) for x in input_data.split(',')]

    adventure_game = Intcode_computer(memory=starting_memory, input_queue=[], suppress_notifications=True)
    
    # play the adventure game
    while True:
        adventure_game.run()
        print_ascii_output(adventure_game.output_queue)
        adventure_game.clear_output_queue()
        command = input()  # get user command
        if command == "are we there yet?":  # shortcut from opening directly to the door with all items
            get_to_door(adventure_game)        
        elif command == "try ALL the things!":  # brute force the door
            brute_force(adventure_game)
            break
        elif command == "up up etc.":
            konami_code(adventure_game)
            break            
        else:  # process the user input as intended
            adventure_game.add_to_input_queue(to_instruction(command), add_list=True)


# try all possible combinations of items
def brute_force(adventure_game):
    combinations = list(itertools.product([0, 1], repeat=8))
    # keep track of items in possession to avoid unnecessary moves
    items = ['monolith', 'fixed point', 'easter egg', 'planetoid', 'candy cane', 'ornament', 'spool of cat6', 'hypercube']
    inv = items.copy()
    for c in combinations:  # hold the right combination of items...
        for i in range(len(items)):
            if c[i] == 1:
                if items[i] not in inv:
                    command = 'take ' + items[i]
                    inv.append(items[i])

            else:
                if items[i] in inv:
                    command = 'drop ' + items[i]
                    inv.remove(items[i])

    
            adventure_game.add_to_input_queue(to_instruction(command), add_list=True)
            adventure_game.run()
            adventure_game.clear_output_queue()
        command = 'west'  # ... and try the door
        adventure_game.add_to_input_queue(to_instruction(command), add_list = True)
        adventure_game.run()

        # check the output to see if there was an alert (combination failed)
        output_string = print_ascii_output(adventure_game.output_queue, printout=False)
        if "Alert" not in output_string:
            print(output_string)
            return 1
        adventure_game.clear_output_queue()

def get_to_door(adventure_game):
    instructions = ['south', 'take fixed point',
                    'north',
                    'north', 'take spool of cat6',
                    'north', 'take monolith',
                    'north', 'take hypercube',
                    'south', 
                    'west', 'take planetoid',
                    'east',
                    'south',
                    'east',
                    'north', 'take candy cane',
                    'south',
                    'east', 'take easter egg',
                    'east',
                    'south', 'take ornament',
                    'west']
    for instruction in instructions:
        adventure_game.add_to_input_queue(to_instruction(instruction), add_list=True)
    adventure_game.run()
    adventure_game.clear_output_queue()
    
    adventure_game.add_to_input_queue(to_instruction('south'), add_list=True)
    adventure_game.run()
    print_ascii_output(adventure_game.output_queue)
    adventure_game.clear_output_queue()


def konami_code(adventure_game):
    instructions = ['north',
                    'north', 'take monolith',
                    'north', 'take hypercube',
                    'south', 
                    'south',
                    'east',
                    'east', 'take easter egg',
                    'east',
                    'south', 'take ornament',
                    'west',
                    'south']
    for instruction in instructions:
        adventure_game.add_to_input_queue(to_instruction(instruction), add_list=True)
    adventure_game.run()
    adventure_game.clear_output_queue()
    
    adventure_game.add_to_input_queue(to_instruction('west'), add_list=True)
    adventure_game.run()
    print_ascii_output(adventure_game.output_queue)
    adventure_game.clear_output_queue()


def print_ascii_output(output, printout=True):
    print_string = ''
    for i in output:
        if i != 'halt':
            print_string += chr(i)
    if printout == True:
        print(print_string)
    return print_string


def to_instruction(s):
    s = to_ascii(s)
    s.append(10)
    return s


def to_ascii(s):
    return [ord(c) for c in s]


if __name__ == "__main__":
    main()