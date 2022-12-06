'''
DAY 23-2: Playing a game of Cups with a million cups (cups = {})

The second part uses the same rules as the first part, but with a million cups and 
ten million moves. The first 9 cups are ordered in the same way, and then the rest 
of the cups just added in order. Though the rules are the same the list method
slows to a crawl as the lists are too large. At approx 4 iterations per second (~16 
if avoiding reordering), it would take many days to finish 10m moves.

Storing the cups as a dictionary solves this problem, with every cup's dictionary 
entry containing the cup it is 'pointing to' (the next cup clockwise). Each move 
only updates three values: the current cup, the destination cup, and the final cup
of the three being shifted. Everything else stays the same. By only updating the 
dictionary we avoid issues like shifting a 1m long list (and conveniently also
avoid the need for modulo operations as the loop is handled in the dictionary).

This speeds it up to ~500,000 moves per second, meaning the code takes ~20 seconds.
'''

import tqdm
import pprint

def main():
    # define parameters of dictionary
    with open('day23/23-1-input.txt', 'r') as open_file:
        input_data = open_file.read()    
    initial_cups = [int(x) for x in input_data]
    high_cup = 1000000
    rounds = 10000000
    
    # create dictionary
    # first entries will be the puzzle input, then sequential numbers
    cups = {}
    for i, c in enumerate(initial_cups):
        cups[c] = initial_cups[(i+1) % len(initial_cups)]

    # add the rest of the numbers   
    for i in range(10, high_cup + 1):
        cups[i] = i + 1

    # include the new entries in the loop
    cups[initial_cups[-1]] = 10
    cups[high_cup] = initial_cups[0]
    
    current_cup = initial_cups[0]
    for _ in tqdm.tqdm(range(rounds)):
        cups, current_cup = play_round(cups, current_cup, high_cup)
    
    print(cups[1] * cups[cups[1]])


# play a single move in the game of cups
def play_round(cups, current_cup, high_cup):
    pointer = current_cup
    removed_cups = []
    for _ in range(3):
        removed_cups.append(cups[pointer])
        pointer = cups[pointer]
        
    dest = current_cup - 1
    while dest in removed_cups or dest < 1:
        if dest < 1:
            dest = high_cup
        else:
            dest -= 1
    
    # update dictionary values
    # temp storage of current versions
    c_current = cups[current_cup]
    c_dest = cups[dest]
    c_final_removed = cups[removed_cups[-1]]

    # update with the current versions
    cups[current_cup] = c_final_removed  # current cup will point where the final shifted cup was pointing
    cups[dest] = c_current  # destination cup will point where the current cup was pointing (first shifted cup)
    cups[removed_cups[-1]] = c_dest  # final shifted cup will point at where the destination cup was pointing

    # update the current cup
    current_cup = cups[current_cup]

    return cups, current_cup

if __name__ == "__main__":
    main()