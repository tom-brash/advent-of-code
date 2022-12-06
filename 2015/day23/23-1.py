import re

def main():
    with open('day23/23.txt', 'r') as open_file:
        ins = open_file.read().split('\n')

    regs = {'a': 0, 'b': 0}
    n = 0
    while n < len(ins):
        i = ins[n].split()
        s = i[0]
        r = i[1]
        if s == 'inc':
            regs[r] += 1
        elif s == 'tpl':
            regs[r] *= 3
        elif s == 'hlf':
            regs[r] /= 2
        elif s == 'jmp':
            n += int(r)
            n -= 1
        elif s == 'jio':
            if regs[r[0]] == 1:
                n += int(i[2])
                n -= 1
        elif s == 'jie':
            if regs[r[0]] % 2 == 0:
                n += int(i[2])
                n -= 1
        n += 1
    
    print(regs['b'])
        

        

if __name__ == '__main__':
    main()