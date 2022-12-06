'''
DAY 6-2: How many questions were answered 'yes' to by everyone in the group

This is similar to the previous problem, and can reuse the bulk of the code
setting up the sets, which is what we iterate through to see which are included
in each answer.

This time we keep track of the lists themselves so we can test them against the groups.
'''

with open('day6/6-1-input.txt', 'r') as input_data_file:
    input_data = input_data_file.read()

groups = input_data.split('\n\n')


group_sets = [set(x.replace('\n', '')) for x in groups]
groups = [x.split('\n') for x in groups]

groups[-1].remove('')  # get rid of the trailing value at the end of the last group


total = 0
for i, group in enumerate(groups):
    for letter in group_sets[i]:
        in_all = True
        for person in group:
            if letter not in person:
                in_all = False
                break
        if in_all == True:
            total += 1


print(total)