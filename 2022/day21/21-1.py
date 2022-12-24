import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    monkeys = {}

    for x in input:
        name = x.split(":")[0]
        nums = [int(y) for y in re.findall(r'\d+', x)]
        if len(nums) > 0:
            num = nums[0]
            m1 = None
            m2 = None
            op = None
        else:
            num = None
            ms = re.findall(r'[a-z]+', x.split(": ")[1])
            op = re.findall(r'[*+-/]', x)[0]
            m1 = ms[0]
            m2 = ms[1]
            
        monkeys[name] = Monkey(num, m1, m2, op)

    answer = None
    while not answer:
        for n, m in monkeys.items():
            if not m.result:
                if monkeys[m.m1].result and monkeys[m.m2].result:
                    m.operate(monkeys[m.m1].result , monkeys[m.m2].result)

            if n == "root":
                answer = m.result

    print(answer)


class Monkey:
    def __init__(self, num, m1, m2, op):
        if num:
            self.type = "num"
        else:
            self.type = "monkey"
        
        self.num = num
        self.m1 = m1
        self.m2 = m2
        self.result = num
        self.op = op
    
    def operate(self, a, b):
        if self.op == "+":
            self.result = a + b
        elif self.op == "-":
            self.result = a - b
        elif self.op == "*":
            self.result = a * b
        elif self.op == "/":
            self.result = a // b

if __name__ == "__main__":
    main()
