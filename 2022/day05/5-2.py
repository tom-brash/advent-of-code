import re
from collections import deque, defaultdict

def main():
    print(f'\nSwitching crane to the CrateMover 9001...')
    with open('input', 'r') as open_file:
        input = open_file.read().rstrip().split('\n')
    stacks = defaultdict(list)

    for line in input:
        if len(line) == 0: continue
        if line[0] != 'm':
            for i, c in enumerate(line[1::4], start=1):
                if not c.isalpha(): continue
                stacks[i] = [c] + stacks[i]
        else:
            nums = [int(i) for i in re.findall(r'[0-9]+', line)]
            stacks = move(*nums, stacks)

    output = ''
    for i in range(1, 10):
        output += stacks[i][-1]
    print(f'\n(5-2) After rearranging all the crates, the stack shows the message: {output}')


def move(a, b, c, stacks):
    temp = stacks[b][-a:]
    stacks[c].extend(temp)
    stacks[b] = stacks[b][:-a]
    return stacks
 
if __name__ == "__main__":
    main()
