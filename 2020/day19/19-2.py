'''
DAY 19-2: Finding strings matching rules that have loops

This question extends 19-1 by changing two rules. Rule 8 was formerly just a link to rule 42, and 
rule 11 was a link to rule 42 followed by rule 31. Now rule 8 can be an arbitrarily long sequence of 
'42's, and 11 is an arbitrarily long sequence of '42's followed by an *equally* long string of '31's.

The recursive approach was challenging here, because the way I had it set up made it easy to greedily
get 42's (or 42s followed by 31s), but that was often not the pathway to being valid. A greedy match 
may use more characters than it should, meaning that the string doesn't return as valid. A solution was
attempted using lists of possibilities as part of the recursion, but ultimately it was more difficult
to comprehend and spiraled in complexity.

The regex solution, on the other hand, extends easily, as it looks forward as well as back, though it
does not completely generalize. The arbitrarily long sequence (for rule 8) is simply a matter of putting
a capturing group around the existing regex and using a '+' character.

Rule 11 is more of a hack. Unfortunately, there doesn't seem to be a way in regex to specify that a 
sequence of 42s must be followed by an *equally* long sequence of 31s, and so using + characters doesn't work.
Instead, to a depth of 6 (experimentally confirmed to work with input) the options 42 31, 42 42 31 31, etc. 
are added to the regex as options
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
    rule_dict = update_pt_2(rule_dict)

    r = rule_dict['0']['regex'] + '$'
    print('Regex string to use: ', r)
    r = re.compile(r)
    valid_tests = 0
    for test in tests:
        if r.match(test) != None:
            valid_tests += 1
    
    print(valid_tests)


def process_rules_list(rules):
    rules_dict = {}
    for rule in rules:       
        rule_num = re.match(r'([0-9]+)\:', rule).group(1)
        if re.search(r'[a-z]', rule) != None:
            details = re.search(r'[a-z]', rule).group()
            regex = details            
        else:
            details = []
            for match in re.finditer(r'(?<=\:\ )[0-9]+(?!\ [0-9]|[0-9])|[0-9]+\ [0-9]+|(?<=\|\ )[0-9]+(?!\ [0-9]|[0-9])', rule):  # include rules that singly match one other rule
                rule_option = match.group().split(' ')
                details.append(rule_option)
            regex = ''
        
        rules_dict[rule_num] = {'details':details, 'regex':regex}
        
    
    return rules_dict


# iteratively update the dictionary until stable to get regular expressions for all rules. Same as part 1
def update_dict(rules_dict):
    stable = False
    while not stable:
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


# manually update rules for rule 8 and rule 11
def update_pt_2(rules_dict):
    rules_dict['8']['regex'] = '(' + rules_dict['8']['regex'] + ')+'
    regex_42 = '(' + rules_dict['42']['regex'] + ')'
    regex_31 = '(' + rules_dict['31']['regex'] + ')'
    regex_11 = ''

    # manually add options for rule 11 to depth specified in range
    for i in range(1, 6):
        regex_11 += '(' + regex_42 * i + regex_31 * i + ')|'
    
    rules_dict['11']['regex'] = regex_11[:-1]

    rules_dict['0']['regex'] = '(' + rules_dict['8']['regex'] + ')(' + rules_dict['11']['regex'] + ')'
    return rules_dict


if __name__ == "__main__":
    main()