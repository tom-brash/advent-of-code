'''
DAY 7-2: How many bags does a shiny gold bag contain?

Rather than focusing specifically on the shiny gold bag, this approach 
found how many bags every other bag type contained.

We make the rule dictionary more complex than in 7-1, including a field 
'total' which is the number of bags directly contained in the bag. We also
have a recursive total field 'rtotal', which is initialized to be the same
as total. However, rtotal is updated to include the rtotals of the internal
bags over and over again. Once it stabilizes, we have the number of bags 
contained in each bag.

This is a similar approach to the one employed in reinforcement learning
'''

def main():
    with open('day7/7-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    rules = input_data.split('\n')
    rule_dicts = [rule_to_dict(x) for x in rules]
    rule_dicts = update_totals(rule_dicts)

    #print(rule_dicts)
    target = 'shiny gold'

    print(find_rule(target, rule_dicts)['rtotal'])




def rule_to_dict(rule):
    rule_dictionary = {}
    rule.replace('.',',')
    rule_dictionary['bag_color'] = rule.split(' bags contain')[0]
    if rule.split('contain ')[1] != 'no other bags.':
        bag_contents = rule.split(' bags contain ')[1].split(', ')
        for i, inner in enumerate(bag_contents):
            inner_bag = {}
            inner_bag['color'] = inner.split(' ')[1] + ' ' + inner.split(' ')[2]
            inner_bag['quantity'] = inner.split(' ')[0]
            rule_dictionary['inner_' + str(i + 1)] = inner_bag
    
    rule_dictionary['total'] = sum_digits(rule)
    rule_dictionary['rtotal'] = sum_digits(rule)

    return rule_dictionary


def update_totals(rule_dicts):
    complete = False
    while not complete:
        total_bags = find_total_bags(rule_dicts)
        for rule in rule_dicts:
            rtotal = rule['total']
            for i in range(1, len(rule.keys()) - 2):
                rtotal += int(find_rule(rule['inner_' + str(i)]['color'], rule_dicts)['rtotal']) * int(rule['inner_' + str(i)]['quantity'])
            rule['rtotal'] = rtotal

        if total_bags == find_total_bags(rule_dicts):
            complete = True
    return rule_dicts
    

def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())            


def find_rule(target, rule_dicts):
    for rule in rule_dicts:
        if rule['bag_color'] == target:
            return rule
    return 'not found'


def find_total_bags(rule_dicts):
    total = 0
    for rule in rule_dicts:
        total += rule['rtotal']
    return total

if __name__ == '__main__':
    main()