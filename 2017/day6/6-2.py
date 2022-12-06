def main():
    with open('day6/6.txt', 'r') as open_file:
        mem = open_file.read().split('\t')

    mem = [int(i) for i in mem]
    print(mem)

    previous_states = [mem.copy()]
    mem_l = len(mem)
    cycles = 0
    while True:
        x = max(mem)
        max_idx = mem.index(x)
        mem[max_idx] = 0
        i = max_idx
        
        while x > 0:
            i = (i + 1) % mem_l
            mem[i] += 1
            x -= 1
        cycles += 1
        
        try:
            rpt_idx = previous_states.index(mem)
            print(cycles - rpt_idx)
            break
        except:
            previous_states.append(mem.copy())
            

if __name__ == '__main__':
    main()