import re

def main():
    with open('day15/15.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    ings = {}
    for i, n in enumerate(['a', 'b', 'c', 'd']):
        nums = tuple([int(x) for x in re.findall(r'-?\d+', input_data[i])])
        ings[n] = nums
    
    best = 0
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                total = get_score(a, b, c, d, ings)
                if total > best:
                    best = total
    
    print(best)
    
def get_score(a, b, c, d, ings):
    total = 1
    cal = 0
    cal += ings['a'][4] * a
    cal += ings['b'][4] * b
    cal += ings['c'][4] * c
    cal += ings['d'][4] * d
    if cal != 500:
        return 0
    
    for i in range(4):
        
        x = 0
        x += ings['a'][i] * a
        x += ings['b'][i] * b
        x += ings['c'][i] * c
        x += ings['d'][i] * d
        total *= max(0, x)

    return total


if __name__ == '__main__':
    main()