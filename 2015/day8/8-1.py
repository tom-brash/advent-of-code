import re

def main():
    with open('day8/8.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    total_mem = 0
    total_l = 0
    for s in input_data:
        x = eval(s)
        total_l += len(x)
        total_mem += len(s)

    print(total_mem - total_l)


if __name__ == '__main__':
    main()