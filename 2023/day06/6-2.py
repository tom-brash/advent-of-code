import re
import math

def get_distance(c, t):
    return (t-c) * c

def main():
    print('==== Day 6 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]

    time = int(''.join(times))
    distance = int(''.join(distances))
    
    found_end = False
    found_start = False
    
    ways = 0

    for i in range(time):
        if get_distance(i, time) > distance:
            ways += 1

    print(ways)
        


if __name__ == "__main__":
	main()
