'''
Day 16-1: Opcode processing I

Here we need to assess which opcodes each operation could be, for the newly minted opcode language.
The code is somewhat longwinded, as we need to implement 16 different opcodes, but it is still straightforward.
We just test every possible opcode for each instruction, and keep track of which each could be. 

'''

def main():
    with open('day16/16-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    examples = input_data.split('\n\n')[:-2]

    total = 0
    for example in examples:
        lines = example.split('\n')
        input_registers = [int(c) for c in lines[0] if c.isdigit()]
        instruction = [int(c) for c in lines[1] if c.isdigit()]
        if len(instruction) > 4:
            instruction = [int(str(instruction[0]) + str(instruction[1]))] + instruction[2:]
        output_registers = [int(c) for c in lines[2] if c.isdigit()]


        p = try_opcode(input_registers, instruction, output_registers)
        if len(p) >= 3:
            total += 1
        
    print('Total examples that could be 3 or more opcodes:', total)
    

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
    

if __name__ == '__main__':
    main()