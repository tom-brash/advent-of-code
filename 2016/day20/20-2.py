import re

def main():
    with open('day20/20.txt', 'r') as open_file:
        blacklist_info = open_file.read()

    blacklist_info = [x.split('-') for x in blacklist_info.split('\n')]
    blacklist = [(int(x[0]), int(x[1])) for x in blacklist_info]

    # find number of possible IP addresses
    n = 0
    total = 0
    while n < 4294967295:
        next_base = find_next_base_interval(n, blacklist)  # find the next listed interval
        total += next_base[0] - n  # add numbers in the clear
        next_end = find_interval_end(next_base, blacklist)  # find the end of the interval, including any overlaps
        n = next_end + 1 # move the pointer forwards
    print(f'Total number of IP addresses allowed by blacklist: {total}')


def find_next_base_interval(n, blacklist):
    blacklist = [x for x in blacklist if x[0] >= n]
    blacklist.sort()
    return blacklist[0]


def find_interval_end(base_interval, blacklist):
    interval_end = base_interval[1]
    while True:
        overlapping = [x for x in blacklist if x[0] <= interval_end + 1 and x[1] > base_interval[0]]
        overlapping.sort(key=lambda x: (-x[1]))
        if overlapping[0][1] == interval_end:
            break
        interval_end = overlapping[0][1]
    return interval_end


if __name__ == '__main__':
    main()
