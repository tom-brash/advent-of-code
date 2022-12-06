'''
DAY 3-1: Check for hitting trees

As the tree pattern is repeated infinitely going to the right, we can just use
modulo function to keep 'wrapping' around to the left once we go off the map on the right.

From there it is just a matter of continuing to move by the vector input and check whether
a tree is present
'''

with open('day3/3-1-input.txt', 'r') as input_data_file:
    input_data = input_data_file.read()

rows = input_data.split('\n')
rows.remove('')

h = 3
v = 1

total_cols = len(rows[0])
cols = []
for i in range(total_cols):
    col = ''
    for row in rows:
        col = col + row[i]
    cols.append(col)

pos = [0, 0]

trees = 0
while pos[0] < len(rows):
    c = pos[1] % total_cols
    r = pos[0]
    if cols[c][r] == '#':
        trees += 1
    pos[0] = pos[0] + v
    pos[1] = pos[1] + h

print(trees)