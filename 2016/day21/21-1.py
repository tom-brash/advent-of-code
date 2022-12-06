import re
from collections import deque

def main():
    with open('day21/21.txt', 'r') as open_file:
        instructions = open_file.read().split('\n')
    scrambler = Scrambler('abcdefgh', instructions)
    scrambler.setup()
    scrambler.run()
    print(''.join(scrambler.password))


class Scrambler:
    def __init__(self, password, instructions):
        self.instructions_raw = instructions
        self.password = [c for c in password]
        self.instructions = []

    def setup(self):
        for i in self.instructions_raw:
            details = i.split()
            if i[:13] == 'swap position':
                i_type = 'pos_swap'
                self.instructions.append((i_type, (int(details[2]), int(details[5]))))
            elif i[:11] == 'swap letter':
                i_type = 'let_swap'
                self.instructions.append((i_type, (details[2], details[5])))
            elif i[:12] == 'rotate based':
                i_type = 'rel_rotate'
                self.instructions.append((i_type, (details[6])))
            elif i[:7] == 'reverse':
                i_type = 'rev'
                self.instructions.append((i_type, (int(details[2]), int(details[4]))))
            elif i[:4] == 'move':
                i_type = 'move'
                self.instructions.append((i_type, (int(details[2]), int(details[5]))))
            elif i[:8] == 'rotate l' or i[:8] == 'rotate r':
                i_type = 'rotate'
                self.instructions.append((i_type, (details[1], int(details[2]))))

    def run(self):
        for i in self.instructions:
            i_type = i[0]
            if i_type == 'rotate':
                self.rotate(*i[1])
            elif i_type == 'rel_rotate':
                self.rel_rotate(*i[1])
            elif i_type == 'pos_swap':
                self.pos_swap(*i[1])
            elif i_type == 'let_swap':
                self.let_swap(*i[1])
            elif i_type == 'rev':
                self.rev(*i[1])
            elif i_type == 'move':
                self.move(*i[1])

    def rotate(self, d, n):
        dq = deque(self.password)
        if d == 'left':
            n *= -1
        dq.rotate(n)
        self.password = list(dq)

    def rel_rotate(self, a):
        i = self.password.index(a)
        if i >= 4:
            i += 1
        self.rotate('right', i + 1)

    def pos_swap(self, x, y):
        t = self.password[x]
        self.password[x] = self.password[y]
        self.password[y] = t

    def let_swap(self, x, y):
        i_x = self.password.index(x)
        i_y = self.password.index(y)
        self.pos_swap(i_x, i_y)

    def rev(self, x, y):
        self.password = self.password[:x] + self.password[x:y+1][::-1] + self.password[y+1:]

    def move(self, x, y):
        t = self.password[x]
        del self.password[x]
        self.password.insert(y, t)



if __name__ == '__main__':
    main()
