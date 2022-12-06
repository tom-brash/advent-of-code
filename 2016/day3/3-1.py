import re

def main():
    with open('day3/3.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    valid = 0

    for tri in input_data:
        nums = sorted(list(map(int, re.findall(r'\d+', tri))))
        if nums[1] + nums[0] > nums[2]:
            valid += 1
    
    print(valid)

if __name__ == '__main__':
    main()