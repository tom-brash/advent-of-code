'''
DAY 18-2: Equation solving with reversed BEDMAS

This builds on 18-1 by introducing order of operations, but addition
comes before multiplication. The brackets are still evaluated first
like in 18-1.

Here a similar logic to parentheses is used in the expression evaluation,
changing 'x + y' to the answer until there are no more '+' signs in the 
expression.
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
    while re.search(r'[0-9]+\ \+\ [0-9]+', eq) != None:
        replacement = eval_add(re.search(r'[0-9]+\ \+\ [0-9]+', eq).group())
        eq = re.sub(r'[0-9]+\ \+\ [0-9]+', replacement, eq, 1)
    
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


def eval_add(add_eq):
    eq = add_eq.split(' + ')
    return str(int(eq[0]) + int(eq[1]))

if __name__ == "__main__":
    main()