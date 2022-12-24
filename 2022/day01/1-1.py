def main():
    with open('input', 'r') as open_file:
	    elves = open_file.read().strip().split('\n\n')

    max = 0

    for elf in elves:
        stuff = elf.split('\n')
        total = sum([int(x) for x in stuff])
        if total > max:
            max = total

    print(max)

if __name__ == "__main__":
	main()
