import re
from collections import deque, defaultdict

def main():
    print('====Day 10====')
    print('Lost contact with the elves after the rope bridge snapped!')
    print('Using *device* to connect up with the elves')
    print('*Device* broken... Designing a replacement for the video screen...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    cpu = aoc_cpu(input)
    cpu.run()
    print(f'\n(10-1) Deciphered signal sent by the CPU: {cpu.total_signal_strength}')

class aoc_cpu:
    def __init__(self, instructions):
        self.instructions = instructions
        self.i_pointer = 0
        self.cycle = 0
        self.registers = {'x': 1}
        self.interesting_cycles = [20, 60, 100, 140, 180, 220]
        self.execution_wait = 0
        self.future_state = {'x': 1}
        self.total_signal_strength = 0
        self.process_instruction()

    def run(self):
        while self.cycle < 230:
            self.progress_cycle()
    
    def progress_cycle(self):
        # print('starting cycle...', self.cycle)
        self.cycle += 1
        if self.cycle in self.interesting_cycles:
            # print(f'Signal strength at cycle {self.cycle}: {self.cycle * self.registers["x"]}')
            self.total_signal_strength += self.cycle * self.registers['x']
        if self.execution_wait > 0:
            self.execution_wait -=1
        if self.execution_wait == 0:
            self.registers = self.future_state.copy()
            self.i_pointer += 1
            self.process_instruction()

    def process_instruction(self):
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
