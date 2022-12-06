'''
DAY 19-1: Finding strings matching rules

This question requires finding strings that match a series of nested rules,
primarily revolving around stitching two other rules together, and having 
multiple options of what this could look like.

This can be approximated by dynamically building regular expressions. By 
iteratively updating the dictionary in a method similar to that used in 
reinforcement learning, we can define the terminal regex rules ('a' or 'b')
and then keep updating the keys. Each time, the one upstream will compile,
until we have all the rules.

The regex string for the rule that is actually being tested is far too long
to manually parse, but still works very quickly
'''

import re
from collections import defaultdict
import pprint
import copy

def main():
    with open('day19/19-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    segments = input_data.split('\n\n')
    rules = segments[0].split('\n')
    tests = segments[1].split('\n')

    rule_dict = process_rules_list(rules)   
    rule_dict = update_dict(rule_dict)

    r = rule_dict['0']['regex'] + '$'
    r = re.compile(r)
    valid_tests = 0
    for test in tests:
        if r.match(test) != None:
            valid_tests += 1
    
    print('final regex used: ', rule_dict['0']['regex'])
    print(valid_tests)


def process_rules_list(rules):
    rules_dict = {}
    for rule in rules:       
        rule_num = re.match(r'([0-9]+)\:', rule).group(1)
        if re.search(r'[a-z]', rule) != None:
            details = re.search(r'[a-z]', rule).group()
            # create regex string for these terminal rules
            regex = details            
        else:
            details = []
            # find possible rules using regex
            # want to find rules of the form ': #', '| #', and '# #'
            for match in re.finditer(r'(?<=\:\ )[0-9]+(?!\ [0-9]|[0-9])|[0-9]+\ [0-9]+|(?<=\|\ )[0-9]+(?!\ [0-9]|[0-9])', rule):  
                rule_option = match.group().split(' ')
                details.append(rule_option)
            # create blank regex string
            regex = ''
        
        rules_dict[rule_num] = {'details':details, 'regex':regex}
        
    return rules_dict


def update_dict(rules_dict):
    stable = False
    while not stable:
        # iterate over dictionary and update regex based on the ones in the deeper rules until the dictionary stops changing
        copy_dict = copy.deepcopy(rules_dict)
        for ruleset in rules_dict:
            regex = ''
            if rules_dict[ruleset]['details'] == 'a' or rules_dict[ruleset]['details'] == 'b':
                continue
            for option in rules_dict[ruleset]['details']:
                for rule in option:
                    if rules_dict[rule]['regex'] != '':
                        regex += '(' + rules_dict[rule]['regex'] + ')'
                regex += '|'
            rules_dict[ruleset]['regex'] = regex[:-1]
        if copy_dict == rules_dict:
            stable = True
    return rules_dict



if __name__ == "__main__":
    main()