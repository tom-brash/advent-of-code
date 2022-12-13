import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    cpu = aoc_cpu(input)
    cpu.run()
    cpu.print_grid()

class aoc_cpu:
    def __init__(self, instructions):
        self.instructions = instructions
        self.i_pointer = 0
        self.cycle = 0
        self.registers = {'x': 1}
        self.execution_wait = 0
        self.future_state = {'x': 1}
        self.grid = {y: ['.' for x in range(40)] for y in range(1, 7)}
        self.process_instruction()

    def run(self):
        while self.cycle <= 240:
            self.progress_cycle()
    
    def print_grid(self):
        for y, row in self.grid.items():
            row_repr = ''.join(row)
            print(row_repr)

    def progress_cycle(self):
        self.cycle += 1
        x_reg = self.registers['x']
        x_pos = (self.cycle - 1) % 40  
        y_pos = self.cycle // 40 + 1
        
        if x_pos in [x_reg - 1, x_reg, x_reg + 1]:
            self.grid[y_pos][x_pos] = '#'

        if self.execution_wait > 0:
            self.execution_wait -=1
        if self.execution_wait == 0:
            self.registers = self.future_state.copy()
            self.i_pointer += 1
            self.process_instruction()

    def process_instruction(self):
        if self.i_pointer >= len(self.instructions):
            return
        instruction = self.instructions[self.i_pointer]
        if instruction[:3] == "add":
            n = int(instruction.split(' ')[1])
            r = instruction[3]
            self.future_state[r] = self.registers[r] + n
            self.execution_wait = 2
        elif instruction[:4] == "noop":
            self.execution_wait = 1


if __name__ == "__main__":
    main()
