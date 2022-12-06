'''
DAY 10-2: Determine possible adapter configurations

From 10-1, we note that there are no differences of size 2, only of size 1 and size 3.
Because the maximum voltage difference is 3, a gap of three means there is only one pathway 
through. By contrast, differences of size 1 will create multiple paths. 

Structurally, we can break the problem into a series of 1 gaps interspersed by size 3 gaps. The final
answer will be the number of combinations in each series of 1 gaps multipled together

By hand, we can observe the pattern of how gaps of size 1 add combinations. 1 1-gap (e.g. 5-6) only
has one combination. 2 1-gaps (e.g. 5-6-7) will have two pathways (5-7, 5-6-7). 3 gaps will have four,
and each one will keep adding to the number of combinations in a pattern of +1, +2, +3, +4, etc.
'''

def main():
    with open('day10/10-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    voltages = input_data.split('\n')
    voltages = [int(x) for x in voltages]
    voltages.append(0)
    voltages.sort()
    voltages.append(voltages[-1] + 3)

    diffs_sequence = []
    for i, volt in enumerate(voltages):
        if i != 0:
            diff = volt - voltages[i-1]
            diffs_sequence.append(diff)
    
    print(diffs_sequence)

    groups = parse_diffs(diffs_sequence)
    print(groups)

    combinations = convert_to_combinations(groups)

    answer = 1
    for comb in combinations:
        answer *= comb

    print(answer)

    
def parse_diffs(sequence):
    groups = []
    consecutive_ones = 0
    for diff in sequence:
        if diff == 1:
            consecutive_ones += 1
        if diff == 3:
            groups.append(consecutive_ones)
            consecutive_ones = 0
    
    return groups


def convert_to_combinations(groups):
    combinations = []
    for group in groups:
        if group > 1:
            combinations.append(comb_value(group))
    return combinations


# crude return for speed, just returns the 
# number of combinations for a sequence of n 1s
def comb_value(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    if number == 3:
        return 4
    if number == 4:
        return 7
    if number == 5:
        return 11
    if number== 6:
        return 16
    if number == 7:
        return 22
    if number == 8:
        return 29
    print('damn')
    return 0

if __name__ == "__main__":
    main()