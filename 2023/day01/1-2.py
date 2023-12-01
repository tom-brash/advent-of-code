import re

def alpha_to_num(s):
    mapping = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    if s.isnumeric():
        return s
    return mapping[s]


def main():
    print('==== Day 1 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    total = 0
    for line in lines:
        matches = re.finditer(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
        nums = [alpha_to_num(match.group(1)) for match in matches]
        num_str = nums[0] + nums[-1]
        total += int(num_str)

    print(f'\n(1-2) The total sum is: {total}')

if __name__ == "__main__":
	main()
