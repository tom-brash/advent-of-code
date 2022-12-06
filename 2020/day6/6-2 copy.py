'''
DAY 6-2: How many questions were answered 'yes' to by everyone in the group

This version of the answer has been updated to better use set intersections - each group is 
converted using map to a 
'''

with open('day6/6-1-input.txt', 'r') as input_data_file:
    input_data = input_data_file.read()

groups = input_data.split('\n\n')

groups = [x.split('\n') for x in groups]
groups[-1].remove('')  # get rid of the trailing value at the end of the last group

groups = [set.intersection(*map(set, x)) for x in groups]
print(sum([len(x) for x in groups]))