from collections import deque

def main():
    elf_count = 3004953
    elves = list(range(1, elf_count + 1))
    n = 0
    i = 0
    # print(elves, n)
    while len(elves) > 1:
        current_e = elves[n]
        del elves[(n + elf_count // 2) % elf_count]
        elf_count -= 1
        if n >= elf_count:
            n = 0
        elif current_e == elves[n]:
            n = (n + 1) % elf_count 
        # print(elves, n)        
        i += 1
        if i % 100000 == 0:
            print(f'Elves removed from the circle: {i}')
    print(f'Last remaining elf: {elves[0]}')

if __name__ == '__main__':
    main()
