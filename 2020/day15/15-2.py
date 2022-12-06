'''
DAY 15-2: Finding the 30,000,000th number in the pattern

The simple approach in 15-1 no longer works, as the list gets much too
long to rapidly sort through. Instead, we get efficiencies from just
storing a dictionary of the most recent time a number was spoken.

To avoid getting into a repetitive sequence of 1s, this means we need 
to get the next number in the sequence before storing the previous one 
in the dictionary. 
'''

from tqdm import tqdm

def main():
    with open('day15/15-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    starting_numbers = [int(x) for x in input_data.split(',')]
    most_recently_spoken = {}
    last_spoken = starting_numbers[-1]

    for i, starting in enumerate(starting_numbers[:-1]):
        most_recently_spoken[starting] = i + 1

    print(most_recently_spoken)

    # play out the game to 30m iterations
    for round_n in tqdm(range(len(starting_numbers) + 1, 30000001)):        
        if last_spoken not in most_recently_spoken:
            next_number = 0
        else:
            next_number = (round_n - 1) - most_recently_spoken[last_spoken]
        most_recently_spoken[last_spoken] = round_n - 1
        last_spoken = next_number 

    print(last_spoken)

def list_rindex(recent_li, li, x):
    for i in reversed(range(len(recent_li))):
        if recent_li[i] == x:
            return len(li) + i + 1
    
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i + 1
    return 0


if __name__ == "__main__":
    main()