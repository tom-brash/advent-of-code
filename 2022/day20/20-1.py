import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    file = deque()
    order = []
    total_nums = len(input)

    for i, x in enumerate(input):
        print(i, x)
        n = int(x) + i / 11000
        file.append(n)
        order.append(n)

    i = 0
    for j in range(total_nums):
        total_rot = 0
        n = order[j % total_nums]
        ni = round(n)
        ix = file.index(n)
        file.rotate(-ix)
        temp = file.popleft()
        file.rotate(-ni)
        file.appendleft(temp)


    file_l = [round(x) for x in file]
    zix = file_l.index(0)
    
    total = sum([file_l[(zix + n) % total_nums] for n in [1000, 2000, 3000]])
        
    print(total)


if __name__ == "__main__":
    main()
