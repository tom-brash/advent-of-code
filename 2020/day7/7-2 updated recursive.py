'''
DAY 7-2 updated: How many bags does a shiny gold bag contain?

Updated to use a more efficient approach, at least for a single example. The original version
is more powerful in that it solves for more bags, which means that repeated calls will be more
efficient, but this is quicker to just solve for the shiny gold bags.

A human approach is used here, opening one type of bag at a time. A minor efficiency is gained
through using a default dictionary to ensure there aren't multiple types of the same bag
in the queue at the same time, as it's faster to do them together
'''

import re
from collections import defaultdict

def main():
    with open('day7/7-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    rules = input_data.split('\n')
    bag_info = {}
    for rule in rules:
        color, info = bag_to_dict(rule)
        bag_info[color] = info

    print(count_bags('shiny gold', bag_info))

def count_bags(bag, bag_info):
    if bag_info[bag] == 'none':
        return 0
    total = 0
    for key, val in bag_info[bag].items():
        total += val
        total += val * count_bags(key, bag_info)
    return total


def bag_to_dict(rule):
    bag_dict = {}
    matches = re.findall(r'(\w+\s\w+)\sbag', rule)
    if 'no other' in rule:
        return matches[0], 'none'
    numbers = re.findall(r'\d+', rule)
    for i in range(1, len(matches)):
        bag_dict[matches[i]] = int(numbers[i - 1])
    return matches[0], bag_dict
    

if __name__ == '__main__':
    main()