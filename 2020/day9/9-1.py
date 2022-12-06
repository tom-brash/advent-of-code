'''
DAY 9-1: Finding first invalid value

A number is valid if it can be created by summing two of the previous n numbers,
where n is the length of the 'preamble'. We can essentially reuse code from Day 1-1
to check where a number can be made by previous ones, and then just pass in the 
preceding 25 numbers to the function each time.
'''


def main():
    with open('day9/9-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    numbers = input_data.split('\n')
    numbers = [float(x) for x in numbers]

    preamble = 25
    for i in range(preamble, len(numbers)):
        if check_validity(numbers[i], numbers[i-25:i]) == False:
            print(numbers[i])
            break 


def check_validity(target, preamble):
    for i, number in enumerate(preamble):
        remaining_numbers = preamble[:i] + preamble[i:]
        if (target - number) in remaining_numbers:
            return True 
    return False

if __name__ == "__main__":
    main()