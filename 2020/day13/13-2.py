'''
DAY 13-2: Finding particular time in the future

Because all of the buses are prime numbers, we can take advantage of some unique relationships.
If we have two numbers (3, 5) the first solution is non-trivial to find - here it is 9 (9 % 3 = 0, (9 + 1) % 5 = 0)
However, all subsequent solutions will be multiples of (3*5) from the first answer (i.e. the second is at 24).

If we add another number (3, 5, 7), it must still conform with the first rules, so we can start searching at 9 and go up in 15s
After finding this solution (54, 54 % 3 = 0, 55 % 5 = 0, 56 % 7 = 0), the next solutions will be going up in (3 x 5 x 7) = 105s

Trying to solve this problem by just going up in 1s (or even 607s) takes far too long, but we can build up one number at a time

First we solve for a list that only features one bus (and a lot of xs), and then use that to make sure we're always incrementing by the maximum possible
'''

def main():
    with open('day13/13-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    input_lines = input_data.split('\n')
    original_buses = input_lines[1].split(',')
    total_running_buses = len([x for x in original_buses if x != 'x'])

    # create working version of the schedule starting with no buses
    current_list = ['x'] * len(original_buses)
    
    # no buses in opening list
    current_buses = []

    # current search parameters
    multiple_to_add = 1
    base = 0

    for i in range(total_running_buses):
        # find next bus to add
        bus_added = find_n_largest(original_buses, i + 1)        
        largest_index = original_buses.index(bus_added)

        # add bus to current working version of the schedule
        current_list[largest_index] = original_buses[largest_index]

        # list of just the buses (no xs) in the current schedule
        current_buses = [int(x) for x in current_list if x != 'x']

        # get the relevant indices for the list
        current_indices = get_indices(current_list)
        
        # find the first answer using just the numbers in the schedule
        base = check_numbers(base, multiple_to_add, current_buses, current_indices)

        # the new number to go up in multiples of should be all of the current bus numbers multiplied together
        multiple_to_add *= int(bus_added)
   
    print(base)
    


def find_n_largest(bus_list, n):
    sorted_list = sorted([x for x in bus_list if x != 'x'])
    return sorted_list[-n]

def get_indices(available_buses):
    original_indices = {}
    for i, bus in enumerate(available_buses):
        if bus != 'x':
            original_indices[int(bus)] = i
    return original_indices
    

def check_numbers(base, multiple_to_add, available_buses, original_indices):
    found = False
    i = 0.0
    while found == False:
        check_num = i * multiple_to_add + base
        found = True
        for bus in available_buses:
            if (check_num + original_indices[bus]) % bus != 0:
                found = False
                i+=1.0
                break
    return(i * multiple_to_add + base)

if __name__ == "__main__":
    main()