'''
DAY 18-1: Equation solving without BEDMAS

This question asks to process equations without the normal BEDMAS rules,
processing addition and multiplication in the order they appear. Parentheses
work as normal.

The core here is a helper function that evaluates equations without brackets
(eval_expression). After that regex is used with this function to evaluate
each internal set of brackets and replace it in the equation string by the 
answer
'''

import re

def main():
    with open('day18/18-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    equations = input_data.split('\n')
    grand_total = 0
    for eq in equations:
        while re.search(r'\([0-9\ \+\*]+\)', eq) != None:
            replacement = eval_expression(re.search(r'\([0-9\ \+\*]+\)', eq).group())
            eq = re.sub(r'\([0-9\ \+\*]+\)', replacement, eq, 1)
        grand_total += int(eval_expression(eq))
    print(grand_total)

def eval_expression(eq):
    eq = re.sub(r'[\(\)]', '', eq)
    eq = eq.split(' ')
    total = int(eq.pop(0))
    for _ in range(0, len(eq) // 2):
        operation = eq.pop(0)
        value = eq.pop(0)
        if operation == '+':
            total += int(value)
        elif operation == '*':
            total *= int(value)
    return str(total)


if __name__ == "__main__":
    main()