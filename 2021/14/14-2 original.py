from collections import Counter
import time

def main():
    with open('14/14.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    start_time = time.time()
    rules = {}
    rule_20 = {}

    for x in input_data:
        a, b = x.split(' -> ')
        rules[a] = b
    
    for p, rule in enumerate(rules.keys()):
        s = rule
        for _ in range(20):
            additions = ''
            for i in range(len(s) - 1):                
                additions += rules[s[i] + s[i + 1]]            
            new_string = s[0]
            for x in range(len(additions)):
                new_string += additions[x]
                new_string += s[x + 1]
            s = new_string
        rule_20[rule] = Counter(s)
    
    print('Rules created, parsing string')
    s = 'OFSNKKHCBSNKBKFFCVNB'
   
    for _ in range(20):
        additions = ''
        for i in range(len(s) - 1):
            
            additions += rules[s[i] + s[i + 1]]            
        new_string = s[0]
        for x in range(len(additions)):
            new_string += additions[x]
            new_string += s[x + 1]
        s = new_string
    
    print('String completed, creating counter')
    total = Counter()
    for i in range(len(s) - 1):
        total = total + rule_20[s[i] + s[i + 1]]
    
    total = total - Counter(s[1:-1])
    print(total.most_common()[0][1] - total.most_common()[-1][1])
    print(f'Part 2 time taken: {round((time.time() - start_time) * 1000, 3)} ms')

    



class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()