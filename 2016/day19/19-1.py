from collections import deque

def main():
    elf_count = 3004953
    elves = list(range(1, elf_count + 1))
    print(f'Remaining elves...{len(elves)}')
    while len(elves) > 1:
        if len(elves) % 2 == 0:
            elves = [elves[i * 2] for i in range(len(elves) // 2)]
        else:
            elves = [elves[i * 2] for i in range(len(elves) // 2 + 1)]
            elves = deque(elves)
            elves.rotate(1)
            elves = list(elves)
        print(f'Remaining elves...{len(elves)}')
    print(f'Elf that gets all the presents: {elves[0]}')       


if __name__ == '__main__':
    main()
