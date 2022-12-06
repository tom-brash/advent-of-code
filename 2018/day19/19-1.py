'''
Day 19-1: Processing opcodes with jumps

This code does the problem 'fairly' (or naively, depending on how you look at it) - executing the instructions until the
instruction pointer goes beyond the available instructions. As a result, it is relatively slow (~10s). 

The code for Part 2 can complete this in <0.1s by just changing the starting register, but this has been left here as
a record of the alternative full process
'''

def main():
    with open('day19/19-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    comp = OpcodeComputer(input_data.split('\n'))
    comp.run()
    print('Value of first register:',comp.registers[0])
    

class OpcodeComputer:
    def __init__(self, instructions):
        self.registers = [0, 0, 0, 0, 0, 0]
        self.instructions = [[int(c) if c.isdigit() else c for c in i.split(' ')] for i in instructions if '#' not in i]
        self.available_indices = range(len(self.instructions))
        self.instruction_pointer = 0
        self.instruction_register = 0
        self.running = True
        for i in instructions:
            if '#' in i:
                self.instruction_register = int([c for c in i if c.isdigit()][0])
    
    def run(self):
        while self.running:
            if self.instruction_pointer not in self.available_indices:
                self.running = False
                break
            self.registers[self.instruction_register] = self.instruction_pointer
            #print(self.instructions[self.instruction_pointer])
            self.process(self.instructions[self.instruction_pointer])
            #print(self.registers)
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


if __name__ == '__main__':
    main()