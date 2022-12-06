from collections import Counter
import time

def main():
    start_time = time.time()
    
    with open('14/14.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    rules = {}
    s = 'OFSNKKHCBSNKBKFFCVNB'

    for x in input_data:
        a, b = x.split(' -> ')
        rules[a] = b
    
    pairs = Counter([a + b for a, b in zip(s, s[1:])])
    letters = Counter(s)
    
    new_pairs = pairs.copy()
    for _ in range(40):
        for p in pairs:
            count = pairs[p]
            a = p[0]
            b = p[1]
            c =  rules[p]
            new_pairs[a+c] += count
            new_pairs[c+b] += count
            new_pairs[a+b] -= count
            letters[c] += count
        pairs = new_pairs.copy()
    
    print(letters.most_common()[0][1] - letters.most_common()[-1][1])
    print(f'Part 2 time taken: {round((time.time() - start_time) * 1000, 3)} ms')

class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()