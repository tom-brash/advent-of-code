import re

def main():
    with open('day12/12.txt', 'r') as open_file:
        input_data = open_file.read()

    obj = Object(input_data, 0)
    print(obj.total)

class Object:
    def __init__(self, data, tier):
        level = -1
        self.tier = tier
        self.children = []
        self.current = ''
        current_child = ''
        for c in data:
            if c == '{':
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    current_child += c
                    self.children.append(Object(current_child, tier + 1))
                    current_child = ''
                    continue
            if level == 0:
                self.current += c
            elif level >= 1:
                current_child += c

        self.total = sum([int(x) for x in re.findall(r'\-?\d+', self.current)])
        for c in self.children:
            self.total += c.total
        if ':\"red' in self.current:
            self.total = 0
        

if __name__ == '__main__':
    main()