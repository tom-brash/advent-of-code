'''
DAY 7-1: How many bags could hold a shiny gold bag

Here we use a recursive function to find the set of bags that would be 'higher' than a shiny gold bag,
and could hold it. We search for all the bags that could directly hold a shiny gold bag, and then
search all the bags that hold those bags, etc.
'''

def main():
    with open('day7/7-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    rules = input_data.split('\n')

    rules = [rule_to_dict(x) for x in rules]

    target = 'shiny gold'

    final_set = find_target(target, rules)
    final_set.remove(target)
    print(len(final_set))


def rule_to_dict(rule):
    rule_dictionary = {}
    rule.replace('.',',')
    rule_dictionary['bag_color'] = rule.split(' bags contain')[0]
    bag_contents = rule.split(' bags contain ')[1].split(', ')
    for i, inner in enumerate(bag_contents):
        rule_dictionary['color_' + str(i + 1)] = inner.split(' ')[1] + ' ' + inner.split(' ')[2]
    return rule_dictionary


def find_target(target, rules, current_set=set()):
    for rule in rules:
        if target in rule.values():
            length = len(current_set)
            current_set.add(rule['bag_color'])
            if len(current_set) != length:
                current_set = find_target(rule['bag_color'], rules, current_set)
    
    return(current_set)
            

if __name__ == '__main__':
    main()


