import re
combs = []

def main():
    with open('day17/17.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    nums = [int(x) for x in input_data]
    subset_sum(nums, 150)
    combs.sort(key=lambda x: len(x))
    best = len(combs[0])
    print(len([c for c in combs if len(c) == best]))


def subset_sum(nums, target, partial=[]):
    s = sum(partial)

    if s == target:
        combs.append(partial)
    
    if s >= target:
        return
    
    for i in range(len(nums)):
        n = nums[i]
        remaining = nums[i + 1:]
        subset_sum(remaining, target, partial + [n])

if __name__ == '__main__':
    main()