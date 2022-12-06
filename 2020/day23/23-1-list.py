'''
DAY 23-1: Playing a game of Cups (list implementation)

The first part involve taking a sequence of ten cups and making a move repeatedly:
taking the three cups to the right of a specified current cup and moving them to 
the right of a destination cup (the current cup - 1, looping as necessary), and
then updating the current cup by moving one clockwise.

It can be solved in any number of ways. This was my first implementation, keeping 
track of the ten cups as a list. As a reordering function was necessary to read
out the answer string, it was also used in the play_round function to keep 
reordering around the current string, conveniently avoiding the indices of removed
cups ever being out of range.

However, the method used for part 2 is both neater and more efficient
'''

def main():
    with open('day23/23-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    cups = [int(x) for x in input_data]
    current_cup = cups[0]
    
    print('starting cups: ', cups)
    for _ in range(100):
        cups, current_cup = play_round(cups, current_cup)

    cups = reorder_cups(cups, 1)
    print(''.join([str(x) for x in cups][1:]))


# make a single move in the game of cups
def play_round(cups, current_cup):
    current_index = cups.index(current_cup)
    max_cup = max(cups)
    
    # create list of removed cups
    removed_cups = []
    for _ in range(3):
        removed_cups.append(cups.pop(current_index + 1))
    
    # determine destination cup
    destination_cup = current_cup - 1
    while destination_cup <= 0 or destination_cup in removed_cups:
        if destination_cup == 0:
            destination_cup = max_cup
        else:
            destination_cup -= 1
    
    # add in removed cups
    for _ in range(3):
        cups.insert(cups.index(destination_cup) + 1, removed_cups.pop(-1))
    
    # update current cup and return the reordered list
    current_cup = cups[current_index + 1]
    cups = reorder_cups(cups, current_cup)
    return cups, current_cup


# reorder cups around a specified cup
def reorder_cups(cups, first):
    reordered_cups = []
    ind = cups.index(first)
    for _ in range(len(cups)):
        reordered_cups.append(cups[ind])
        ind += 1
        if ind == len(cups):
            ind = 0
    return reordered_cups


if __name__ == "__main__":
    main()