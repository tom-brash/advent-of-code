'''
Day 19-2: Processing opcodes with jumps (modified starting register)

Changing the first register's starting value to 1 means that waiting for it to finish is not feasible 
(best estimates are many thousand years), meaning that we need to dig into what the opcode is actually 
doing and try and circumvent it. 

What turns out to be happening is that the first ~17 instructions are entirely for the purpose of putting a
'target' value in the fifth register. From there the code loops over several instructions over and over until
the program exits.

The program is, roughly:

total = 0
for i in range(target):
    for j in range(target):
        if i * j == target:
            total += i

In other words, it sums up the factors of the number, in an extremely inefficient manner. Knowing this though, we
can just run the first 17 steps of the program, extract the target, and just sum the factors ourselves.
'''

from itertools import chain

def main():
    with open('day19/19-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    comp = OpcodeComputer(input_data.split('\n'))
    comp.run_n(17)  # sufficient to get the fifth register to the target number
    target = comp.registers[5]
    print('Sum of factors of target number and answer to this puzzle:', sum(factors(target)))
    

class OpcodeComputer:
    def __init__(self, instructions):
        self.registers = [1, 0, 0, 0, 0, 0]
        self.instructions = [[int(c) if c.isdigit() else c for c in i.split(' ')] for i in instructions if '#' not in i]
        self.available_indices = range(len(self.instructions))
        self.instruction_pointer = 0
        self.instruction_register = 0
        self.running = True
        for i in instructions:
            if '#' in i:
                self.instruction_register = int([c for c in i if c.isdigit()][0])
    
    def run_n(self, n):
        for i in range(n):
            if self.instruction_pointer not in self.available_indices:
                self.running = False
                break
            self.registers[self.instruction_register] = self.instruction_pointer
            #print(self.instruction_pointer, self.instructions[self.instruction_pointer])
            self.process(self.instructions[self.instruction_pointer])
            #print(self.registers)
            self.instruction_pointer = self.registers[self.instruction_register] + 1
            

    def run(self):
        while self.running:
            if self.instruction_pointer not in self.available_indices:
                self.running = False
                break
            self.registers[self.instruction_register] = self.instruction_pointer
            print(self.instruction_pointer, self.instructions[self.instruction_pointer])
            self.process(self.instructions[self.instruction_pointer])
            print(self.registers)
            self.instruction_pointer = self.registers[self.instruction_register] + 1

    def process(self, instruction):
        i = instruction[0]
        
        try:
            reg_A = self.registers[instruction[1]]
        except:
            reg_A = None
        try:
            reg_B = self.registers[instruction[2]]
        except:
            reg_B = None
        val_A = instruction[1]
        val_B = instruction[2]
        outcome = instruction[3]

        if i == 'addr':
            self.registers[outcome] = (reg_A + reg_B)
        
        elif i == 'addi':
            self.registers[outcome] = (reg_A + val_B)
        
        elif i == 'mulr':
            self.registers[outcome] = (reg_A * reg_B)
        
        elif i == 'muli':
            self.registers[outcome] = (reg_A * val_B)
        
        elif i == 'banr':
            self.registers[outcome] = (reg_A & reg_B)
        
        elif i == 'bani':
            self.registers[outcome] = (reg_A & val_B)
        
        elif i == 'borr':
            self.registers[outcome] = (reg_A | reg_B)

        elif i == 'bori':
            self.registers[outcome] = (reg_A | val_B)

        elif i == 'setr':
            self.registers[outcome] = reg_A

        elif i == 'seti':
            self.registers[outcome] = val_A

        elif i == 'gtir':
            self.registers[outcome] = int(val_A > reg_B)

        elif i == 'gtri':
            self.registers[outcome] = int(reg_A > val_B)
        
        elif i == 'gtrr':
            self.registers[outcome] = int(reg_A > reg_B)
        
        elif i == 'eqir':
            self.registers[outcome] = int(val_A == reg_B)
        
        elif i == 'eqri':
            self.registers[outcome] = int(reg_A == val_B)
        
        elif i == 'eqrr':
            self.registers[outcome] = int(reg_A == reg_B)

def factors(n):
    return chain.from_iterable([[i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0])


if __name__ == '__main__':
    main()