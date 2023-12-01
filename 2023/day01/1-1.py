def main():
    print('==== Day 1 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    total = 0
    for line in lines:
        a = None
        b = None
        st = ''
        for c in line:
            if c.isnumeric():
                if not a:
                    a = c
                b = c
        st = a + b
        total += int(st)

    print(f'\n(1-1) The total sum is: {total}')

if __name__ == "__main__":
	main()
