import re

def main():
    print('==== Day 8 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    instructions = [0 if x == 'L' else 1 for x in lines[0]]
    s_mapping = lines[2:]
    
    mapping = {}

    for m in s_mapping:
        letters = re.findall(r'[A-Z]+', m)
        mapping[letters[0]] = (letters[1], letters[2])

    i = 0
    loc = 'AAA'
    length = len(instructions)
    while loc != 'ZZZ':
        loc = mapping[loc][instructions[i % length]]
        i += 1
        print(loc)

    print(i)


    




if __name__ == "__main__":
	main()
