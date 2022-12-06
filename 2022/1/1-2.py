def main():
    with open('input', 'r') as open_file:
	    elves = open_file.read().strip().split('\n\n')

    weights = []

    for elf in elves:
        stuff = elf.split('\n')
        total = sum([int(x) for x in stuff])
        weights.append(total)

    print(sum(sorted(weights)[-3:]))

if __name__ == "__main__":
	main()
