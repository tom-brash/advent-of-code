from collections import defaultdict
from collections import deque
from collections import Counter
import copy

def main():
    with open('14/14.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    s = 'NNCB'
    rules = {}

    for x in input_data:
        a, b = x.split(' -> ')
        rules[a] = b
    
    for _ in range(10):
        additions = ''
        for i in range(len(s) - 1):
            
            additions += rules[s[i] + s[i + 1]]            
        new_string = s[0]
        for x in range(len(additions)):
            new_string += additions[x]
            new_string += s[x + 1]
        s = new_string
    
    print(Counter(s).most_common())
    
    test = 'abcdr'
    



class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()