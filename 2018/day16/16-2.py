'''
Day 16-2: Opcode processing II

One of the longest codebases I've had to write for a relatively simple problem. In an effort to make both
the first part (ascertaining possible codes) and then the second part (actually running code) relatively
efficient, they are implemented as separate functions - but it doubles the length of the code.

The major difference from part I here is that basic logic needs to be implemented to narrow down the opcodes. As we 
go we build a dictionary of possible codes, taking the intersection of past possibilities an the current instruction.
This turns out to be sufficient to make them uniquely identifiable
'''

from collections import defaultdict
from pprint import pprint
import copy

def main():
    with open('day16/16-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    examples = input_data.split('\n\n')[:-2]
    opcode_mapping = {}

    # check which numbers can correspond to each opcode
    for example in examples:
        lines = example.split('\n')
        input_registers = [int(c) for c in lines[0] if c.isdigit()]
        instruction = [int(c) for c in lines[1] if c.isdigit()]
        if len(instruction) > 4:
            instruction = [int(str(instruction[0]) + str(instruction[1]))] + instruction[2:]
        output_registers = [int(c) for c in lines[2] if c.isdigit()]

        p = try_opcode(input_registers, instruction, output_registers)
        i = instruction[0]
        if i not in opcode_mapping:
            opcode_mapping[i] = set(p)
        else:
            opcode_mapping[i] &= set(p)  # mapping should be updated to the intersection of possibilities
    
    # map the opcodes to the correct operations
    changing = True
    while changing:
        changing = False
        updated = copy.deepcopy(opcode_mapping)
        for c in opcode_mapping:
            if len(opcode_mapping[c]) == 1:
                locked = next(iter(opcode_mapping[c]))
                for k in opcode_mapping:
                    if k != c:
                        updated[k].discard(locked)
                
                if updated != opcode_mapping:
                    changing = True
                    opcode_mapping = updated
    
    for k in opcode_mapping:
        opcode_mapping[k] = next(iter(opcode_mapping[k]))
    
    # process program using mapping determined above
    comp = OpcodeComputer(opcode_mapping)
    program = input_data.split('\n\n')[-1].split('\n')
    for line in program:
        instruction = [int(c) for c in line.split(' ')]
        comp.process(instruction)
    
    print(comp.registers)

def try_opcode(input_registers, instruction, output_registers):
    possibilities = []
    
    
    try:
        reg_A = input_registers[instruction[1]]
    except:
        reg_A = None
    try:
        reg_B = input_registers[instruction[2]]
    except:
        reg_B = None
    val_A = instruction[1]
    val_B = instruction[2]
    
    target_output = output_registers[instruction[3]]


    # seti
    if target_output == val_A:
        possibilities.append('seti')

    if reg_A != None:       
        # addi
        if target_output == (reg_A + val_B):
            possibilities.append('addi')

        # muli
        if target_output == (reg_A * val_B):
            possibilities.append('muli')
        
        # bori
        if target_output == (reg_A | val_B):
            possibilities.append('bori')

        # setr
        if target_output == reg_A:
            possibilities.append('setr')
        
        # bani
        if target_output == (reg_A & val_B):
            possibilities.append('bani')

        # eqri
        if target_output == (reg_A == val_B):
            possibilities.append('eqri')       
                
        # gtri
        if target_output == (reg_A > val_B):
            possibilities.append('gtri')
    
    if reg_B != None:
        # gtir
        if target_output == (val_A > reg_B):
            possibilities.append('gtir')
        
        # eqir
        if target_output == (val_A == reg_B):
            possibilities.append('eqir')
    
    if reg_A != None and reg_B != None:
        # addr
        if target_output == (reg_A + reg_B):
            possibilities.append('addr')
        
        # mulr
        if target_output == (reg_A * reg_B):
            possibilities.append('mulr')
        
        # banr
        if target_output == (reg_A & reg_B):
            possibilities.append('banr')
        
        # borr
        if target_output == (reg_A | reg_B):
            possibilities.append('borr')

        
        # gtrr
        if target_output == (reg_A > reg_B):
            possibilities.append('gtrr')
        
        # eqrr
        if target_output == (reg_A == reg_B):
            possibilities.append('eqrr')
    
    return possibilities
    

class OpcodeComputer:
    def __init__(self, mapping):
        self.registers = [0, 0, 0, 0]
        self.mapping = mapping


    def process(self, instruction):
        i = self.mapping[instruction[0]]
        
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
            self.registers[outcome] = (val_A > reg_B)

        elif i == 'gtri':
            self.registers[outcome] = (reg_A > val_B)
        
        elif i == 'gtrr':
            self.registers[outcome] = (reg_A > reg_B)
        
        elif i == 'eqir':
            self.registers[outcome] = (val_A == reg_B)
        
        elif i == 'eqri':
            self.registers[outcome] = (reg_A == val_B)
        
        elif i == 'eqrr':
            self.registers[outcome] = (reg_A == reg_B)


if __name__ == '__main__':
    main()