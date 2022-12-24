import re
import ast
from sympy import solve, parse_expr, Symbol
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    monkeys = {}

    for x in input:
        rx = re.search(r'(\w+):\s(?:(\w+)\s([*\/\+\-])\s(\w+)|(\d+))', x)
        name = rx.group(1)
        m1 = rx.group(2)
        op = rx.group(3)
        m2 = rx.group(4)
        num = rx.group(5)
        if name == "humn":
            num = None
        monkeys[name] = Monkey(num, m1, m2, op)

        if name == "root":
            f1 = m1
            f2 = m2

    monkeys["humn"].result = "x"
    
    simplified = False
    while not simplified:
        for name, monkey in monkeys.items():
            if not monkey.result and name not in ["root", "humn"]:
                a = monkeys[monkey.m1].result
                b = monkeys[monkey.m2].result
                if a and b:
                    monkey.update(a, b)
        if monkeys[f1].result and monkeys[f2].result:
            simplified = True

    eq_string = f'{monkeys[f1].result} - {monkeys[f2].result}'
    x = Symbol('x')
    print(f'Simplified to the following equation...')
    print(eq_string)
    print('\nSolving equation...')

    print(f'Final answer: {solve(parse_expr(eq_string))[0]}')

class Monkey:
    def __init__(self, num, m1, m2, op):
        self.m1 = m1
        self.m2 = m2
        if num:
            num = int(num)
        self.result = num
        self.op = op

    def update(self, a, b):
        if isinstance(a, str) or isinstance(b, str):
            self.result = f'({a}) {self.op} ({b})'
        else:
            self.result = parse_expr(f'{a} {self.op} {b}')

if __name__ == "__main__":
    main()
