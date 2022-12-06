from collections import defaultdict
import re

def main():
    with open('day7/7.txt', 'r') as open_file:
        input_data = open_file.read()
    
    wires = defaultdict(int)
    cs = set(re.findall(r'[a-z]+', input_data))

    input_data = input_data.split('\n')
    while True:
        for i in input_data:
            e = re.findall(r'[A-Z]+', i)
            target = re.search(r'\-\>\ (.+)', i).groups(1)[0]
            if target == 'b':
                wires['b'] = 16076      # manual override provided
                continue                # don't use original code
            d = i.split()
            if len(e) == 0:
                if d[0] in cs:
                    if d[0] not in wires:
                        continue
                    wires[target] = wires[d[0]]
                else:
                    wires[target] = int(d[0])
            elif 'NOT' in e:
                if d[1] not in wires:
                    continue
                wires[target] = ~wires[d[1]]
            else:
                if d[0] in cs:
                    if d[0] not in wires:
                        continue
                    a = wires[d[0]]
                else:
                    a = int(d[0])
                if d[2] in cs:
                    if d[2] not in wires:
                        continue
                    b = wires[d[2]]
                else:
                    b = int(d[2])
            
            if 'AND' in e:
                wires[target] = a & b
            elif 'OR' in e:
                wires[target] = a | b
            elif 'LSHIFT' in e:
                wires[target] = a << b
            elif 'RSHIFT' in e:
                wires[target] = a >> b
    
        if 'a' in wires:
            if wires['a'] != 0:
                break
    print(wires['a'])
                


if __name__ == '__main__':
    main()