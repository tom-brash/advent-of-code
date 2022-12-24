import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n\n')

    monkey_group = MonkeyGroup()
    
    for i, m in enumerate(input):
        m_details = m.split('\n')
        starting_items = [int(x) for x in re.findall(r'\d+', m_details[1])]
        operation_full = m_details[2].split('old ')[1]
        operation = operation_full.split(' ')[0]
        op_val = operation_full.split(' ')[1]
        test_val =  int(re.findall(r'\d+', m_details[3])[0])
        true_target = int(re.findall(r'\d+', m_details[4])[0])
        false_target = int(re.findall(r'\d+', m_details[5])[0])
        monkey = Monkey(operation, op_val, test_val, true_target, false_target, starting_items)
        monkey_group.add_monkey(i, monkey)

    monkey_group.set_mod_vals()

    for i in range(10000):
        monkey_group.run_round()

    monkey_group.get_monkey_business()

    

class Monkey:
    def __init__(self, operation, op_val, test_val, true_target, false_target, starting_items=None):
        if not starting_items:
            starting_items = []
        self.items = starting_items
        self.operation = operation
        self.op_val = op_val
        self.test_val = test_val
        self.true_target = true_target
        self.false_target = false_target
        self.items_evaluated = 0
        self.mod_val = None

    def append_item(self, item):
        self.items.append(item)

    def operate(self, item):
        if self.op_val == "old":
            x = item
        else:
            x = int(self.op_val)
        if self.operation == '+':
            item = item + x
        else:
            item = item * x
        return item

    def eval_item(self):
        self.items_evaluated += 1
        item = self.items.pop(0)
        anx_val = self.operate(item)
        anx_val = anx_val % self.mod_val
        if anx_val % self.test_val == 0:
            n = self.true_target
        else:
            n = self.false_target
        return anx_val, n

class MonkeyGroup:
    def __init__(self):
        self.monkeys = {}
        self.mod_val = 1

    def add_monkey(self, i, m):
        self.monkeys[i] = m
        self.mod_val *= m.test_val

    def set_mod_vals(self):
        for m in self.monkeys.values():
            m.mod_val = self.mod_val

    def run_round(self):
        for i in range(len(self.monkeys)):
            self.take_turn(i) 

    def take_turn(self, i):
        monkey = self.monkeys[i]
        while len(monkey.items) > 0:
            item, n = monkey.eval_item()
            self.monkeys[n].append_item(item) 
        self.monkeys[i] = monkey


    def get_monkey_business(self):
        eval_item_list = sorted([m.items_evaluated for m in self.monkeys.values()])
        print(f'Monkey business: {eval_item_list[-1] * eval_item_list[-2]}')


if __name__ == "__main__":
    main()
