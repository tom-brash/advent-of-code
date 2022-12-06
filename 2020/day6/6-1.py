'''
DAY 6-1: How many questions were answered 'yes' to by at least one person in the group

This is straightforward, using list comprehension to turn each group of answers into a 
set of letters, and then adding the length of all of the sets
'''

with open('day6/6-1-input.txt', 'r') as input_data_file:
    input_data = input_data_file.read()

groups = input_data.split('\n\n')
groups = [set(x.replace('\n', '')) for x in groups]
print(sum([len(x) for x in groups]))