from collections import defaultdict

def main():
    with open('day8/8.txt', 'r') as open_file:
        instructions = open_file.read().split('\n')
    
    registers = Registers(instructions)
    registers.run()
    registers.get_max()

class Registers():
    def __init__(self, instructions):
        self.instructions = instructions
        self.regs = defaultdict(int)
        self.max_val = -9000
    
    def run(self):
        for i in self.instructions:
            components = i.split(' ')
            check_reg_val = self.regs.get(components[4], 0)
            test_val = int(components[6])
            op = components[5]
            if op == '<=':
                check = check_reg_val <= test_val
            elif op == '>=':
                check = check_reg_val >= test_val
            elif op == '<':
                check = check_reg_val < test_val
            elif op == '>':
                check = check_reg_val > test_val
            elif op == '!=':
                check = check_reg_val != test_val
            elif op == '==':
                check = check_reg_val == test_val
            
            if check == True:
                if components[1] == 'inc':
                    self.regs[components[0]] += int(components[2])
                    self.max_val = max(self.max_val, self.regs[components[0]])
                else:
                    self.regs[components[0]] -= int(components[2])
    
    def get_max(self):
        print('Current max value:', max(list(self.regs.values())))
        print('Maximum value reached:', self.max_val)

if __name__ == '__main__':
    main()