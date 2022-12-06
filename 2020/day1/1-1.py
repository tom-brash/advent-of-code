'''
DAY 1-1: Check for two number sum

For any given target number, each number must have a specific partner to get to
2020. We just need to check if that number exists in the list, which is trivial
to do.
'''


with open('day1/1-1-input.txt', 'r') as input_data_file:
    input_data = input_data_file.read()

expenses = input_data.split('\n')
expenses.remove('')

expenses = list(map(int, expenses)) 

target_val = 2020

expense_set = set(expenses)

for expense in expense_set:
    if target_val - expense in expense_set:
        print(expense * (target_val - expense))
        break

