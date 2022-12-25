import re
from collections import deque, defaultdict

def main():
    print('\nWorry levels increasing...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n\n')

    monkey_group = MonkeyGroup()

    divis_checks = []
    
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
        divis_checks.append(test_val)

    monkey_group.fix_items(divis_checks)

    for i in range(10000):
        monkey_group.run_round()

    monkey_group.get_monkey_business()


class Item:
    def __init__(self, item_no, divis_checks):
        self.check_reg = {}
        for d in divis_checks:
            self.check_reg[d] = item_no % d


class Monkey:
    def __init__(self, operation, op_val, test_val, true_target, false_target, starting_items=None):
        if not starting_items:
            starting_items = []
        self.items = starting_items
        self.operation = operation
        if op_val == "old":
            self.square = True
        else: 
            op_val = int(op_val)
            self.square = False
        self.op_val = op_val
        self.test_val = test_val
        self.true_target = true_target
        self.false_target = false_target
        self.items_evaluated = 0

    def append_item(self, item):
        self.items.append(item)

    def mod_operate(self, reg_val, c_val):
        if self.square:
            c_val = (c_val ** 2) % reg_val
            return c_val
        if self.operation == '+':
            c_val = (c_val + self.op_val) % reg_val
        else:
            c_val = (c_val * self.op_val) % reg_val
        return c_val

    def eval_item(self):
        self.items_evaluated += 1
        item = self.items.pop(0)
        
        for reg, c_val in item.check_reg.items():
            item.check_reg[reg] = self.mod_operate(reg, c_val)

        if  item.check_reg[self.test_val] == 0:
            n = self.true_target
        else:
            n = self.false_target
        return item, n

class MonkeyGroup:
    def __init__(self):
        self.monkeys = {}

    def add_monkey(self, i, m):
        self.monkeys[i] = m

    def fix_items(self, divis_checks):
        for n in self.monkeys:
            existing_items = self.monkeys[n].items
            self.monkeys[n].items = [Item(item_no, divis_checks) for item_no in existing_items]

    def run_round(self):
        for i in range(len(self.monkeys)):
            self.take_turn(i) 

    def take_turn(self, i):
        monkey = self.monkeys[i]
        while len(monkey.items) > 0:
            item, n = monkey.eval_item()
            #print(f'Moving item {item} to monkey {n}')
            self.monkeys[n].append_item(item) 
        self.monkeys[i] = monkey


    def get_monkey_business(self):
        eval_item_list = sorted([m.items_evaluated for m in self.monkeys.values()])
        print(f'\n(11-2) Monkey business after 10,000 rounds: {eval_item_list[-1] * eval_item_list[-2]}')

if __name__ == "__main__":
    main()
