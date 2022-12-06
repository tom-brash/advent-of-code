import math

combs = []

def main():
    with open('day24/24.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    presents = [int(x) for x in input_data]
    target = sum(presents) / 4
    subset_sum(presents, presents, target)

    combs.sort(key=lambda x: (len(x), math.prod(x)))
    
    print(f'{len(combs)} possible configurations found with 6 or less presents in central group')
    print(f'Best configuration is {combs[0]} with quantum entanglement score of: {math.prod(combs[0])}')

# Store all possible subsets in global combs list
def subset_sum(numbers, presents, target, partial=[]):
    s = sum(partial)
    if len(partial) > 5:  # heuristic to limit search. We're looking for minimum, meaning that it must be 9 or fewer. 7 is a further reduction that would be lifted if no results found
        return

    # check if the partial sum is equals to target
    if s == target: 
        rem_presents = [x for x in presents if x not in partial]
        valid = check_subset(rem_presents, presents, target, partial)
        if valid:
            combs.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, presents, target, partial + [n]) 


# Binary check if possible subset exists
def check_subset(numbers, presents, target, used, partial=[], terminal=False):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        if not terminal:
            used = used.copy() + partial.copy()
            rem_presents = [x for x in presents if x not in used]
            valid = check_subset(rem_presents, presents, target, used, terminal=True)
            if valid:
                return True
        else:
            return True
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        if check_subset(remaining, presents, target, used, partial + [n], terminal) == True:
            return True


if __name__ == '__main__':
    main()