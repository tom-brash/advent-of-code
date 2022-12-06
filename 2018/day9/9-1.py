'''
Day 9-1: The Marble game (Lists are for suckers)

Having done questions of this nature before, going straight to dictionaries made more
sense to track which marbles were where. An initial approach was tried only keeping 
track of the next marble clockwise, but moving back counter clockwise was too slow
(in particular {v: k for k, v in dict.items()} works but is slow when called 
repeatedly).

As such, for each insertion or removal, the required marbles are updated in both the
clockwise and anticlockwise direction. Still can be optimized further, but this works
for both part 1 and part 2
'''


import re
from collections import defaultdict
from pprint import pprint
from tqdm import tqdm

def main():
    with open('day9/9-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    matches = re.search(r'([0-9]+).*?([0-9]+)', input_data)
    p = int(matches.group(1))
    n = int(matches.group(2)) + 1
    print(p, 'players')
    print(n, 'marbles')

    current_marble = 0
    current_player = 1
    attributes = {'clockwise': None, 'counterclockwise': None}
    marbles = defaultdict(attributes.copy)
    marbles[0] = {'clockwise': 0, 'counterclockwise': 0}
    players = defaultdict(int)

    for i in tqdm(range(1, n)):
        if i % 23 == 0:            
            marbles, removed, current_marble = remove_seven_cc(marbles, current_marble)
            players[current_player] += i + removed

        else:                        
            t1 = marbles[current_marble]['clockwise']
            t2 = marbles[t1]['clockwise']
            
            marbles[t1]['clockwise'] = i
            marbles[t2]['counterclockwise'] = i
            marbles[i]['clockwise'] = t2
            marbles[i]['counterclockwise'] = t1
            
            current_marble = i
        current_player = (current_player + 1) % p  
    
    top = max(players.values())
    print('Top score:', top)


def remove_seven_cc(marbles, placeholder):
    for _ in range(6):
        placeholder = marbles[placeholder]['counterclockwise']
    
    current = placeholder
    placeholder = marbles[placeholder]['counterclockwise']
    removed = placeholder
    placeholder = marbles[placeholder]['counterclockwise']
    marbles[placeholder]['clockwise'] = current
    marbles[current]['counterclockwise'] = placeholder

    return marbles, removed, current


if __name__ == '__main__':
    main()