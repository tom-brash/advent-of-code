'''
DAY 15-1: Finding the 2020th number in the pattern

With such a small target number, we can do this simply by just storing
a list of all numbers, and using reverse indexing to find the time 
a number was most recently spoken.

Note that the 15-2 approach will also work (better) for this problem, as
15-1 and 15-2 are identicial problems except for the magnitude of the 
index being returned
'''

from tqdm import tqdm

def main():
    with open('day15/15-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    starting_numbers = input_data.split(',')

    spoken_numbers = starting_numbers.copy()
    spoken_numbers = [int(x) for x in spoken_numbers]

    for _ in tqdm(range(25 - len(starting_numbers))):
        last_occurence = list_rindex(spoken_numbers[:-1], spoken_numbers[-1])
        if last_occurence != 0:
            spoken_numbers.append(len(spoken_numbers) - last_occurence)
        else:
            spoken_numbers.append(0)

    print(spoken_numbers)
    print(spoken_numbers[-1])

def list_rindex(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i + 1
    return 0


if __name__ == "__main__":
    main()