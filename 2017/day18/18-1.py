from collections import defaultdict
from pprint import pprint

def main():
    with open('day18/18.txt', 'r') as open_file:
        instructions = open_file.read().split('\n')
    
    tablet = Registers(instructions)
    tablet.run()


class Registers():
    def __init__(self, instructions):
        self.instructions = []
        self.last_sound = None
        self.regs = defaultdict(int)
        self.recovered = False
        self.current = 0
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
        while not self.recovered:
            i = self.instructions[self.current]
            f = i['f']
            if f == 'snd':
                self.f_sound(i['x'])
            elif f == 'set':
                self.f_set(i['x'], i['y'])
            elif f == 'add':
                self.f_add(i['x'], i['y'])
            elif f == 'mul':
                self.f_mul(i['x'], i['y'])
            elif f == 'mod':
                self.f_mod(i['x'], i['y'])
            elif f == 'rcv':
                self.f_recover(i['x'])
            elif f == 'jgz':
                self.f_jump(i['x'], i['y'])
            self.current += 1
            #pprint(self.regs)
            
    
    def f_sound(self, x):
        if isinstance(x, str):
            x = self.regs[x]
        print(f'Play sound at freq {x}')
        self.last_sound = x
    
    def f_set(self, x, y):
        if isinstance(y, str):
            y = self.regs.get(y, 0)
        self.regs[x] = y
    
    def f_add(self, x, y):
        if isinstance(y, str):
            y = self.regs.get(y, 0)
        self.regs[x] += y
    
    def f_mul(self, x, y):
        if isinstance(y, str):
            y = self.regs.get(y, 0)
        self.regs[x] *= y
    
    def f_mod(self, x, y):
        if isinstance(y, str):
            y = self.regs.get(y, 0)
        self.regs[x] = self.regs.get(x, 0) % y
    
    def f_recover(self, x):
        if isinstance(x, str):
            x = self.regs[x]
       
        if x != 0:
            print(f'Recovered value: {self.last_sound}')
            self.recovered = True
    
    def f_jump(self, x, y):
        if isinstance(x, str):
            x = self.regs[x]
        if isinstance(y, str):
            y = self.regs[y]
        if x > 0:
            self.current += y -1

    


if __name__ == '__main__':
    main()