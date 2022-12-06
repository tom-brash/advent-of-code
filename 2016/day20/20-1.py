def main():
    with open('day20/20.txt', 'r') as open_file:
        blacklist_info = open_file.read()

    blacklist_info = [x.split('-') for x in blacklist_info.split('\n')]
    blacklist = [(int(x[0]), int(x[1])) for x in blacklist_info]
    blacklist.sort(key=lambda x: (x[0], x[1]))
    interval_end = blacklist[0][1]
    while True:
        overlapping = [x for x in blacklist if x[0] <= interval_end + 1]
        overlapping.sort(key=lambda x: (-x[1]))
        if overlapping[0][1] == interval_end:
            break
        interval_end = overlapping[0][1]
    
    print(f'First non-blacklisted IP address: {interval_end + 1}')


if __name__ == '__main__':
    main()