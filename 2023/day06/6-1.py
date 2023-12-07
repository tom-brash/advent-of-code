import re
import math

def get_distance(c, t):
    return (t-c) * c

def main():
    print('==== Day 6 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]

    races = []

    for i in range(len(times)):
        races.append((times[i], distances[i]))

    m_nums = []

    for race in races:
        ways = 0
        t = race[0]
        d = race[1]
        for i in range(t):
            if get_distance(i, t) > d:
                ways += 1
        m_nums.append(ways)

    print(math.prod(m_nums))

if __name__ == "__main__":
	main()
