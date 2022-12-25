import string
def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    total = 0

    for i in range(int(len(input) / 3)):
        elves = []
        for j in range(3):
            elves.append(set([convert(ord(y)) for y in input[i * 3 + j]]))

        total += sum(set.intersection(*elves))
    print(f'\n(3-2) The sum of the priorities of the redundant items between three elf groups is: {total}')

def convert(i):
    if i >= 97:
        return i - 96
    else: return i - 38


if __name__ == "__main__":
    main()
