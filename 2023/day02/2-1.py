import re

def main():
    print('==== Day 2 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    max_dict = {"red": 12, "green": 13, "blue": 14}
    total = 0

    for i, line in enumerate(lines):
        viable = True
        for color in ("red", "green", "blue"):
            r_string = '(\d+) ' + color
            balls_drawn = re.findall(r_string, line)
            balls_drawn = [int(x) for x in balls_drawn]
            if max(balls_drawn) > max_dict[color]:
                viable = False
        
        if viable:
            total += (i + 1)


    print(f'\n(2-1) The total sum is: {total}')

if __name__ == "__main__":
	main()
