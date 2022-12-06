import re

def main():
    with open('day2/2.txt', 'r') as open_file:
        input_data = open_file.read().split()
    
    total = 0
    for d in input_data:
        nums = sorted([int(x) for x in re.findall(r'\d+', d)])
        total += nums[0] * nums[1] * 2
        total += nums[1] * nums[2] * 2
        total += nums[0] * nums[2] * 2
        total += nums[0] * nums[1]
        
    
    print(total)
    



if __name__ == '__main__':
    main()