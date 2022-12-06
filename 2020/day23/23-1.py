'''
DAY 23-1: Playing a game of Cups (updated)

The first part involve taking a sequence of ten cups and making a move repeatedly:
taking the three cups to the right of a specified current cup and moving them to 
the right of a destination cup (the current cup - 1, looping as necessary), and
then updating the current cup by moving one clockwise.

This is an updated version of the code using the same logic as part 2. While there
are so few cups the speed up is trivial, it is still more efficient to use the 
dictionary approach (now only using the original cups)
'''

def main():
    # define parameters of dictionary
    with open('day23/23-1-input.txt', 'r') as open_file:
        input_data = open_file.read()    
    initial_cups = [int(x) for x in input_data]
    high_cup = 9
    rounds = 100
    
    # create dictionary
    # first entries will be the puzzle input, then sequential numbers
    cups = {}
    for i, c in enumerate(initial_cups):
        cups[c] = initial_cups[(i+1) % len(initial_cups)]
    
    current_cup = initial_cups[0]
    for _ in range(rounds):
        cups, current_cup = play_round(cups, current_cup, high_cup)
    
    answer_string = ''
    current_cup = 1
    while cups[current_cup] != 1:
        answer_string += str(cups[current_cup])
        current_cup = cups[current_cup]

    print(answer_string)


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