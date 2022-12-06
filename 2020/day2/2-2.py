'''
DAY 2-2: Check for passport validity (by index location)

We can parse the input in the same way as in 2-1, except now we want to use the min-max as two 
indices instead. It is trivial to check the password indices for the required character value,
and see whether exactly one of them contains the right character.
'''

import pprint as pp

with open('day2/2-1-input.txt', 'r') as input_data_file:
    input_data = input_data_file.read()

lines = input_data.split('\n')
lines.remove('')

passwords = []
for line in lines:
    index_1 = int(line.split('-')[0])
    index_2 = int(line.split('-')[1].split(' ')[0])
    pass_char = line.split(' ')[1][0]
    seq = line.split(' ')[-1]
    password = {'index_1': index_1, 'index_2': index_2, 'pass_char': pass_char, 'seq': seq}
    passwords.append(password)

valid_passwords = 0

for password in passwords:
    matches = 0
    i1 = password['index_1'] - 1  # adjust to zero index
    i2 = password['index_2'] - 1
    if password['seq'][i1] == password['pass_char']:
        matches += 1
    if password['seq'][i2] == password['pass_char']:
        matches += 1
    
    if matches == 1:
        valid_passwords += 1

print(valid_passwords)
    
