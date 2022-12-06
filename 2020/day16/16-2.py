'''
DAY 16-2: Uniquely identifying train ticket fields

We can modify the 16-1 code slightly so that the ticket validity check simply
 returns True/False to remove the invalid tickets.

We then create a new dictionary for the possible placements of each rule - by
default, they could be at any possible index on the ticket. By looping through
the tickt set, we reduce the number of possible placements.

This does not uniquely identify the fields: there are some fields that multiple
placements would have been valid. We then use a 'sudoku' like slicing pattern:
i.e. if one field can ONLY be in position 7, we remove 7 from the possibilities
list for all other fields
'''

import re
import numpy as np


def main():
    # parse the input
    with open('day16/16-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    input_blocks = input_data.split('\n\n')
    ticket_fields = input_blocks[0].split('\n')
    ticket_rules = {}
    for field in ticket_fields:
        rule_name = re.search(r'([A-Z\ ]+)\:', field, re.I).group(1)
        rule_options = re.findall(r'([0-9]+)\-([0-9]+)', field)
        rule_options = [[int(x) for x in list(rule_options[0])], [int(x) for x in list(rule_options[1])]]
        ticket_rules[rule_name] = rule_options
            
    your_ticket = [int(x) for x in input_blocks[1].split('\n')[1].split(',')]
    nearby_tickets = [x.split(',') for x in input_blocks[2].split('\n')[1:]]  # get all nearby tickets from input
    nearby_tickets = [[int(y) for y in x] for x in nearby_tickets]  # convert to integer

    valid_tickets = [x for x in nearby_tickets if check_ticket_validity(x, ticket_rules) != False]  # remove invalid tickets
    
    # determine possible placements
    rule_placements = {}
    for key in ticket_rules.keys():
        rule_placements[key] = list(np.arange(1, len(ticket_rules.keys()) + 1, 1))

    for ticket in valid_tickets:
        rule_placements = refine_rule_placements(rule_placements, ticket_rules, ticket)
    
    # refine placements further using slicing
    rule_placements = sudoku_slice(rule_placements)
    print(rule_placements)

    # get the final total
    departure_index_list = []
    for rule in rule_placements.keys():
        if rule[0:9] == 'departure':
            departure_index_list.append(rule_placements[rule])
    
    final_total = 1
    for index in departure_index_list:
        final_total *= your_ticket[index[0] - 1]

    print(final_total)


# check if a ticket is valid
def check_ticket_validity(ticket, ticket_rules):
    for val in ticket:
        valid = False
        for rule in ticket_rules.values():
            for option in rule:
                if val >= option[0] and val <= option[1]:
                    valid = True
        if valid == False:
            return False
    
    return True


# given a set of possible placements and a tickets, refine the list of placements
def refine_rule_placements(rule_placements, ticket_rules, ticket):
    for rule in rule_placements.keys():
        current_options = rule_placements[rule]
        for option in current_options:
            val = ticket[option - 1]
            if check_possible(val, ticket_rules[rule]) == False:
                current_options.remove(option)
        rule_placements[rule] = current_options
    
    return rule_placements


# check if a value can fit within multiple rule options, sent as a list [[x-y], [x-y]]
def check_possible(value, rule_options):
    for option in rule_options:
        if value >= option[0] and value <= option[1]:
            return True
    return False


# sudoku style slice on the rule placements
def sudoku_slice(rule_placements):
    changes_made = True
    while changes_made == True:
        changes_made = False
        for rule in rule_placements.keys():
            if len(rule_placements[rule]) == 1:
                force_rule = rule_placements[rule][0]
                for i in rule_placements.keys():
                    if i!= rule:
                        original_value = rule_placements[i].copy()
                        rule_placements[i] = [x for x in rule_placements[i] if x != force_rule]
                        if rule_placements[i] != original_value:
                            changes_made = True
    return rule_placements

if __name__ == "__main__":
    main()