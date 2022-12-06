'''
Neat problem. Nice hook that the first solution you find using the obvious method is almost certainly not the lowest possible
answer - need to keep going to find more answers until the current value of n exceeds the best value found (as we will never
find a better answer)
'''

from collections import defaultdict

def main():
    with open('day20/20.txt', 'r') as open_file:
        g = int(open_file.read())
    
    n = 1
    houses = defaultdict(int)
    found = False
    best = 100000000
    while n < best:
        t = n
        for i in range(1, 51):
            houses[t * i] += n * 11
            if houses[t * i] >= g:
                if t * i < best:
                    best = t * i
                    print(f'Current best: {best}')
        n += 1
    
    print(f'Best possible: {best}')


if __name__ == '__main__':
    main()