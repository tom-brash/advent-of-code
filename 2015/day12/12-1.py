import re

def main():
    with open('day12/12.txt', 'r') as open_file:
        input_data = open_file.read()
    
    nums = [int(x) for x in re.findall(r'\-?\d+', input_data)]
    print(sum(nums))


if __name__ == '__main__':
    main()