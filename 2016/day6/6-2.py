from collections import Counter

with open('day6/6.txt', 'r') as open_file:
    input_data = open_file.read().split('\n')

cols = {}
for i in range(8):
    cols[i] = []

for code in input_data:
    for i, c in enumerate(code):
        cols[i].append(c)

final_string = ''

for i in range(8):
    col_string = ''.join(cols[i])
    c = Counter(col_string).most_common()
    final_string += c[-1][0]

print(final_string)