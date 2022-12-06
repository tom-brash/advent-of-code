import re

def main():
    with open('day3/3.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    valid = 0

    col_1 = []
    col_2 = []
    col_3 = []

    for tri in input_data:
        nums = list(map(int, re.findall(r'\d+', tri)))
        col_1.append(nums[0])
        col_2.append(nums[1])
        col_3.append(nums[2])
        if len(col_1) % 3 == 0:
            for c in [col_1, col_2, col_3]:
                tri_test = sorted(c[-3:])
                if tri_test[0] + tri_test[1] > tri_test[2]:
                    valid += 1
    
    print(valid)

if __name__ == '__main__':
    main()