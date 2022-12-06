'''
DAY 1-2: Check for three number sum

Once we take a number, we can then reframe the question with a new target number
(original target - number) that we are trying to get to with two further numbers.
This allows us to basically reuse the code logic from 1-1.
'''

with open('day1/1-1-input.txt', 'r') as input_data_file:
    input_data = input_data_file.read()

expenses = input_data.split('\n')
expenses.remove('')

expenses = list(map(int, expenses)) 

target_val = 2020

expense_set = set(expenses)

for e1 in expense_set:
    for e2 in expense_set:
        if e1 != e2:
            total = e1 + e2
            if target_val - total in expense_set:
                print(e1 * e2 * (target_val - total))
                break
