import re

def main():
    with open('day16/16.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    target = {'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1}
        
    sues = {}
    for i, s in enumerate(input_data):
        nums = re.findall(r'\w+\:\ \d+', s)
        d = {}
        for x in nums:
            info = x.split(': ')
            d[info[0]] = int(info[1])
        sues[i + 1] = d
    
    for s, d in sues.items():
        valid = True
        for k in d.keys():
            if k == 'trees' or k == 'cats':
                if target[k] >= d[k]:
                    valid = False
            elif k == 'pomeranians' or k == 'goldfish':
                if target[k] <= d[k]:
                    valid = False
            elif d[k] != target[k]:
                valid = False
        if valid == True:
            print(f'The real Aunt Sue is Aunt #{s}')
if __name__ == '__main__':
    main()