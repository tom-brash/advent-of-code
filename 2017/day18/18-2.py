from collections import defaultdict
from pprint import pprint

def main():
    with open('day18/18.txt', 'r') as open_file:
        instructions = open_file.read().split('\n')
    
    tab_network = Network(instructions)
    tab_network.run()

class Network():
    def __init__(self, instructions):
        self.tablet_a = Registers(instructions, 0)
        self.tablet_b = Registers(instructions, 1)
        self.strike_one = False
    
    def run(self):
        while True:
            a_val = self.tablet_a.step()
            if a_val != None:
                self.tablet_b.rcv_queue.append(a_val)
            b_val = self.tablet_b.step()
            if b_val != None:
                self.tablet_a.rcv_queue.append(b_val)
            
            if self.tablet_a.waiting and self.tablet_b.waiting:
                if not self.strike_one:
                    self.strike_one = True
                else:
                    break
        
        print(f'Total sent by tablet 1: {self.tablet_b.sent_count}')

class Registers():
    def __init__(self, instructions, id=0):
        self.instructions = []
        self.regs = defaultdict(int)
        self.regs['p'] = id
        self.rcv_queue = []
        self.current = 0
        self.waiting = False
        self.sent_count = 0
        self.id = id
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
            

    def step(self):
        i = self.instructions[self.current]
        f = i['f']
        sent_val = None
        if f != 'rcv':
            self.waiting = False
        if f == 'snd':
            sent_val = self.f_send(i['x'])
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
        if sent_val != None:
            return sent_val

            
    def f_send(self, x):
        if isinstance(x, str):
            x = self.regs[x]
        print(f'Tablet {self.id} sends value {x}')
        self.sent_count += 1
        return x

    
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
        if len(self.rcv_queue) == 0:
            self.current -= 1
            self.waiting = True
        else:
            self.waiting = False
            self.regs[x] = self.rcv_queue.pop(0)
       
    
    def f_jump(self, x, y):
        if isinstance(x, str):
            x = self.regs[x]
        if isinstance(y, str):
            y = self.regs[y]
        if x > 0:
            self.current += y -1


if __name__ == '__main__':
    main()