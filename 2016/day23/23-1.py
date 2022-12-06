'''
Part 1 is solvable 'naively' by just running the instructions (it takes approximately 44k instruction runs). 
The part 2 solution solves it much more efficiently, but this version has been left alone to show the process.
'''

def main():
    with open('day23/23.txt', 'r') as open_file:
        input_data = open_file.read()

    assembunny = AssembunnyComp(input_data)
    easter_eggs = 7
    assembunny.registers['a'] = easter_eggs
    assembunny.run()
    a = assembunny.registers['a']
    print(f'Assembunny output for {easter_eggs} eggs: {a}')
    

class AssembunnyComp:
    def __init__(self, instructions):
        self.instructions = instructions.split('\n')
        self.registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
        self.i = 0
        self.tgl_vals = {'inc': 'dec', 'tgl': 'inc', 'dec': 'inc', 'cpy': 'jnz', 'jnz': 'cpy'}

    def run(self):
        while self.i in range(0, len(self.instructions)):
            args = self.instructions[self.i].split()
            if args[0] == 'jnz':
                if args[2] in self.registers:
                    jump_val = int(self.registers[args[2]])
                else:
                    jump_val = int(args[2])
                if args[1] in self.registers:
                    if self.registers[args[1]] != 0:
                        self.i += jump_val
                        continue
                elif args[1] != 0:
                    self.i += jump_val
                    continue
            if args[0] == 'tgl':
                index = self.registers[args[1]] + self.i
                if index < len(self.instructions):
                    self.instructions[index] = self.tgl_vals[self.instructions[index][:3]] + self.instructions[index][3:]
            if args[0] == 'cpy':
                if args[2] in self.registers:
                    if args[1] in self.registers:
                        self.registers[args[2]] = self.registers[args[1]]
                    else:
                        self.registers[args[2]] = int(args[1])
            if args[0] == 'inc':
                self.registers[args[1]] += 1
            if args[0] == 'dec':
                self.registers[args[1]] -= 1
            self.i += 1


if __name__ == '__main__':
    main()
