def main():
    with open('day4/4.txt', 'r') as open_file:
        passwords = open_file.read().split('\n')

    print(len(passwords))
    valid = 0

    for p in passwords:
        words = p.split(' ')
        words = [''.join(sorted(w)) for w in words]
        w_set = set(words)
        if len(words) == len(w_set):
            valid += 1

    print(valid)

if __name__ == '__main__':
    main()