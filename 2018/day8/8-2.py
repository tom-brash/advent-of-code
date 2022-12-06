'''
Day 8-2: Scoring nodes recursively

Here we need to assign a value to each node, based on the values of the inner
nodes. The recursive approach used in Part 1 serves well here, as each node can be scored
before needing to go to the outer layers metadata, and the lowest level nodes can be 
scored without reference to other nodes
'''

from pprint import pprint

def main():
    with open('day8/8-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    bag_data = [int(x) for x in input_data.split(' ')]
    bag_dict = {}
    root_value = retrieve_value(bag_data)
    print('Value of root node:', root_value)


def retrieve_value(bag_data, current_bag=0):
    num_inner = bag_data.pop(0)
    num_meta = bag_data.pop(0)
    bag_info = {'contained_values':[], 'metadata':[]}
    for i in range(num_inner):
        current_bag += 1
        bag_info['contained_values'].append(retrieve_value(bag_data))
    
    for i in range(num_meta):
        bag_info['metadata'].append(bag_data.pop(0))
    
    value = 0
    if len(bag_info['contained_values']) == 0:
        value = sum(bag_info['metadata'])
    else:
        for i in bag_info['metadata']:
            try:
                value += bag_info['contained_values'][i - 1]
            except:
                pass
    
    return value


if __name__ == '__main__':
    main()