import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    total = 0

    for x in input:
        total += from_snafu(x)

    print(f'Required code in SNAFU: {to_snafu(total)}')

def from_snafu(x):
    translate = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    d = 1
    total = 0
    for c in x[::-1]:
        total += d * translate[c]
        d *= 5
    return total

def to_snafu(d):
    translate = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}
    max_vals = {0: 2}
    for i in range(1, 25):
        max_vals[i] = 2 * (5 ** i) + max_vals[i - 1]

    started = False
    i = 0
    while not started:
        if d > max_vals[i]:
            i += 1
        else:
            started = True

    total = 0
    snafu_str = ''
    for j in range(i, -1, -1):
        diff = d - total
        val = round(diff / (5 ** j), 0)
        total += val * (5 ** j)
        snafu_str += translate[val]
    return snafu_str
        

if __name__ == "__main__":
    main()
