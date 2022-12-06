import string
from collections import defaultdict
import pprint

def main():
    with open('inexact/movies2.txt', 'r') as open_file:
        input_data = open_file.read()
    
    rows = input_data.split('\n')
    s = ''
    freq = defaultdict(int)
    for r in rows:
        for c in r:
            if c != ' ':
                freq[c] += 1
    

    pprint.pprint(freq)


if __name__ == '__main__':
    main()