from collections import defaultdict

def main():
    with open('day23/23.txt', 'r') as open_file:
        instructions = open_file.read().split('\n')
    
    tablet = Registers(instructions)
    tablet.run()
    print(f'Muliplication instructions executed: {tablet.mul_instructions}')

class Registers():
    def __init__(self, instructions):
        self.instructions = []
        self.regs = defaultdict(int)
        self.current = 0
        self.mul_instructions = 0
        for i in instructions:
            d = i.split()
            f =  d[0]
            if d[1].isalpha():
                x = d[1]
            else:
                x = int(d[1])
            if len(d) > 2:
                if d[2].isalpha():
                    y = d[2]
                else:
                    y = int(d[2])
                self.instructions.append({'f': f, 'x': x, 'y': y})
            else:
                self.instructions.append({'f': f, 'x': x})
            
    def run(self):
        while self.current in range(len(self.instructions)):
            
            i = self.instructions[self.current]
            f = i['f']
            if f == 'set':
                self.f_set(i['x'], i['y'])
            elif f == 'sub':  
                self.f_sub(i['x'], i['y'])
            elif f == 'mul':
                self.mul_instructions += 1
                self.f_mul(i['x'], i['y'])
            elif f == 'jnz':
                self.f_jump(i['x'], i['y'])
            self.current += 1

    
    def f_set(self, x, y):
        if isinstance(y, str):
            y = self.regs.get(y, 0)
        self.regs[x] = y
    
    def f_sub(self, x, y):
        if isinstance(y, str):
            y = self.regs.get(y, 0)
        self.regs[x] -= y

    def f_mul(self, x, y):
        if isinstance(y, str):
            y = self.regs.get(y, 0)
        self.regs[x] *= y

    
    def f_jump(self, x, y):
        if isinstance(x, str):
            x = self.regs[x]
        if isinstance(y, str):
            y = self.regs[y]
        if x != 0:
            self.current += y - 1


if __name__ == '__main__':
    main()