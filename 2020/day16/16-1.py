'''
DAY 16-1: Finding invalid tickets

We can find invalid tickets by just looping through each ticket
and testing each value against the entire list of rules. It does
not exclude any rules from any positions, as we do not yet know 
which tickets are invalid
'''

import re

def main():
    with open('day16/16-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    input_blocks = input_data.split('\n\n')
    ticket_fields = input_blocks[0].split('\n')
    ticket_rules = {}
    for field in ticket_fields:
        rule_name = re.search(r'([A-Z]+)\:', field, re.I).group(1)
        rule_options = re.findall(r'([0-9]+)\-([0-9]+)', field)
        rule_options = [[int(x) for x in list(rule_options[0])], [int(x) for x in list(rule_options[1])]]
        ticket_rules[rule_name] = rule_options
            
    nearby_tickets = [x.split(',') for x in input_blocks[2].split('\n')[1:]]

    total = 0
    for ticket in nearby_tickets:
        ticket = [int(x) for x in ticket]
        total += ticket_scan_error(ticket, ticket_rules)
    
    print(total)


def ticket_scan_error(ticket, ticket_rules):
    total = 0
    for val in ticket:
        valid = False
        for rule in ticket_rules.values():
            for option in rule:
                if val >= option[0] and val <= option[1]:
                    valid = True
        if valid == False:
            total += val
    
    return total


if __name__ == "__main__":
    main()