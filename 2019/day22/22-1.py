'''
DAY 22-1: Shuffling a deck of 10,007 cards

This is relatively straightforward, and can be done by keeping track of the whole
deck at once. Each operation can be easily executed using list slicing.

Here I naievely created a Deck class, thinking that the cleaner the code was, the 
easier it would be to crack the infamous 21-2. It came to naught, but is why this
code is somewhat over-engineered for what it does.
''' 

import re

def main():
    with open('day22/22-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    instructions = input_data.split('\n')
    print(instructions)
    deck = Deck(10007)
    for instruction in instructions:
        n = re.search(r'(\-?[0-9]+)', instruction)
        if n is None:
            deck.stack()
        else:
            n = int(n[0])
            if re.match(r'deal with increment', instruction) is not None:
                deck.deal(n)
            elif re.match(r'cut', instruction) is not None:
                deck.cut(n)
        
    print('Index of card 2019: ', deck.state.index(2019))
    

class Deck:
    def __init__(self, size):
        self.size = size
        self.state = list(range(size))

    def deal(self, n):
        new_list = [0] * self.size
        for i, card in enumerate(self.state):
            new_list[(i * n) % self.size] = card
        self.state = new_list
        print('deal', n)        

    def cut(self, n):
        print('cut', n)
        if n <= 0:
            n = self.size + n        
        cut_stack = self.state[:n]
        remaining_stack = self.state[n:]
        self.state = remaining_stack + cut_stack

    def stack(self):              
        print('stack')
        self.state.reverse() 

if __name__ == "__main__":
    main()