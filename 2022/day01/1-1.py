def main():
    print('==== Day 1 ====')
    print('Seeking fifty stars to feed reindeer!')
    print('\nPlanning expedition and counting calories...')
    with open('input', 'r') as open_file:
	    elves = open_file.read().strip().split('\n\n')

    max = 0

    for elf in elves:
        stuff = elf.split('\n')
        total = sum([int(x) for x in stuff])
        if total > max:
            max = total

    print(f'\n(1-1) The elf with the most calories has: {max} calories')

if __name__ == "__main__":
	main()
