'''
DAY 9-2: Finding continugous numbers in the chain that sum to n

While not especially efficient, when given a target number we can just 
run through the list, summing all contiguous numbers until we surpass (or equal)
the target number exactly. If we match the target number, we return the range
that gave us the answer
'''

def main():
    with open('day9/9-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    numbers = input_data.split('\n')
    numbers = [float(x) for x in numbers]

    target = 14144619.0

    for i in range(len(numbers)):
        total = 0
        pointer = i
        used_numbers = []
        while total < target:
            total += numbers[pointer]
            used_numbers.append(numbers[pointer])
            pointer += 1            
        if total == target:
            used_numbers.sort()
            print(used_numbers[0] + used_numbers[-1])
            break


if __name__ == "__main__":
    main()