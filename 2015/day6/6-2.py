import re

def main():
    with open('day6/6.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    light_grid = {}
    for x in range(1000):
        for y in range(1000):
            light_grid[(x, y)] = 0
    
    for i in input_data:
        nums = [int(x) for x in re.findall(r'\d+', i)]
        if i[:6] == 'toggle':
            for x in range(nums[0], nums[2] + 1):
                for y in range(nums[1], nums[3] + 1):
                    light_grid[(x, y)] += 2
        elif i[:7] == 'turn on':
            for x in range(nums[0], nums[2] + 1):
                for y in range(nums[1], nums[3] + 1):
                    light_grid[(x, y)] += 1
        else:
            for x in range(nums[0], nums[2] + 1):
                for y in range(nums[1], nums[3] + 1):
                    if light_grid[(x, y)] > 0:
                        light_grid[(x, y)] -= 1
    
    total = 0
    for x in range(1000):
        for y in range(1000):
            total += light_grid[(x, y)] 
    
    print(total)



if __name__ == '__main__':
    main()