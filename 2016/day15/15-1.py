import re
def main():
    with open('day15/15.txt', 'r') as open_file:
        disc_info = open_file.read().split('\n')
    
    discs = []
    for d in disc_info:
        nums = [int(x) for x in re.findall(r'\d+', d)]
        discs.append((nums[1], nums[3]))
    print(discs)

    n = 0
    found = False
    while not found:
        broken = False
        for i, d in enumerate(discs):
            if (d[1] + (i + 1) + n) % d[0] != 0:
                broken = True
                break
        if not broken:
            found = True
        else:
            n += 1
    
    print(n)

if __name__ == '__main__':
    main()