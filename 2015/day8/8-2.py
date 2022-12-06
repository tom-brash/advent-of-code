import re

def main():
    with open('day8/8.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    total_mem = 0
    total_l = 0
    for s in input_data:
        a = len(re.findall(r'\"', s))
        sl = len(re.findall(r'\\', s))
        total_l += len(s) + a + sl + 2
        total_mem += len(s)

    print(total_l - total_mem)


if __name__ == '__main__':
    main()