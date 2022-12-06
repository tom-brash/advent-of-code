'''
Day 8-1: Opening up nodes recursively

Here the string gives us the number of nodes that root node contains, and then
the number of pieces of metadata that are attached after the inner nodes (and
so on recursively).

Here we just open up the nodes recursively, keeping track of one long list of
metadata to sum up at the end
'''

from pprint import pprint

def main():
    with open('day8/8-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    bag_data = [int(x) for x in input_data.split(' ')]

    metadata = retrieve_metadata(bag_data)
    total = sum(metadata)
    print('Sum of all metadata values:', total)


def retrieve_metadata(bag_data, metadata=[]):
    num_inner = bag_data.pop(0)
    num_meta = bag_data.pop(0)
    for i in range(num_inner):
        metadata = retrieve_metadata(bag_data, metadata)
    
    for i in range(num_meta):
        metadata.append(bag_data.pop(0))
    return metadata


if __name__ == '__main__':
    main()