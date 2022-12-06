from collections import defaultdict

def main():
    with open('day12/12.txt', 'r') as open_file:
        input_data = open_file.read()
    
    assembunny = AssembunnyComp(input_data)
    assembunny.run()
    print(assembunny.registers['a'])


class AssembunnyComp:
    def __init__(self, instructions):
        self.instructions = instructions.split('\n')
        self.registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        self.i = 0
    
    def run(self):
        while self.i in range(0, len(self.instructions)):
            args = self.instructions[self.i].split()
            if args[0] == 'jnz':
                if args[1] in self.registers:
                    if self.registers[args[1]] != 0:
                        self.i += int(args[2])
                        continue                
                elif args[1] != 0:
                    self.i += int(args[2])
                    continue
            if args[0] == 'cpy':
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