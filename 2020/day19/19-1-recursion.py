'''
DAY 19-1b: Finding strings matching rules

This question requires finding strings that match a series of nested rules,
primarily revolving around stitching two other rules together, and having 
multiple options of what this could look like.

This was my first attempt, and became too complicated in its existing form 
to easily extend into 19-2. However, it does work for this problem efficiently.

This approach uses recursion, continually using the function 'check_rule' and 
popping the start of the string off where there has been a successful rule match.
If going through the rules results in matching all of them and leaving an empty 
string behind, then we have a match.

The regex solution is, in my view, easier to understand
'''

import re
from collections import defaultdict
import pprint

def main():
    with open('day19/19-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    segments = input_data.split('\n\n')
    rules = segments[0].split('\n')
    tests = segments[1].split('\n')

    rule_dict = process_rules_list(rules)
    
    pprint.pprint(rule_dict)
    print(len(tests))
    

    valid_tests = 0
    for test in tests:
        valid, remaining = check_rule(rule_dict, '0', test)
        if valid == True and len(remaining) == 0:
            valid_tests += 1

    print(valid_tests)

def process_rules_list(rules):
    rules_dict = defaultdict(list)
    for rule in rules:       
        rule_num = re.match(r'([0-9]+)\:', rule).group(1)
        if re.search(r'[a-z]', rule) != None:
            rules_dict[rule_num] = re.search(r'[a-z]', rule).group()
        else:
            for match in re.finditer(r'(?<=\:\ )[0-9]+(?!\ [0-9]|[0-9])|[0-9]+\ [0-9]+|(?<=\|\ )[0-9]+(?!\ [0-9]|[0-9])', rule):  # include rules that singly match one other rule
                rule_option = match.group().split(' ')
                rules_dict[rule_num].append(rule_option)
    
    return rules_dict


def check_rule(rule_dict, test_rule, test):
    rule_contents = rule_dict[test_rule]
    if rule_contents == 'a' or rule_contents == 'b':
        if len(test) < 1:
            return False, test        
        if test[0] == rule_contents:
            return True, test[1:]
        else:
            return False, test
    else:
        for option in rule_contents:
            test_copy = test
            for rule in option:                
                valid, test_copy = check_rule(rule_dict, rule, test_copy)
                if not valid:
                    break
            if valid:
                test = test_copy
                return True, test
        return False, test


if __name__ == "__main__":
    main()