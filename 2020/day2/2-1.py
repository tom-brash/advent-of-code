'''
DAY 2-1: Check for passport validity

We start by parsing the input, using split as opposed to regex (though regex should probably
be used here). We can then check which character is being looked for in each password, and see how many
times that character appears in the password by using .count on the password string
'''


import pprint as pp

with open('day2/2-1-input.txt', 'r') as input_data_file:
    input_data = input_data_file.read()

lines = input_data.split('\n')
lines.remove('')

passwords = []
for line in lines:
    min_char = int(line.split('-')[0])
    max_char = int(line.split('-')[1].split(' ')[0])
    pass_char = line.split(' ')[1][0]
    seq = line.split(' ')[-1]
    password = {'min_char': min_char, 'max_char': max_char, 'pass_char': pass_char, 'seq': seq}
    passwords.append(password)

valid_passwords = 0

for password in passwords:
    instances = password['seq'].count(password['pass_char'])
    if instances >= password['min_char'] and instances <= password['max_char']:
        valid_passwords += 1


print(valid_passwords)
    
