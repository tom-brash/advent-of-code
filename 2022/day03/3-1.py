def main():
    print('====Day 3====')
    print('Rearranging the packing before going on the expedition...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    total = 0

    for x in input:
        l = int(len(x)/2)
        a = x[:l]
        b = x[l:]
        a = set([convert(ord(y)) for y in a])
        b = set([convert(ord(y)) for y in b])

        total += sum(a.intersection(b))

    print(f'\n(3-1) The sum of the priorities of items that appear in both backpack halves is: {total}')

def convert(i):
    if i >= 97:
        return i - 96
    else: return i - 38


if __name__ == "__main__":
    main()
