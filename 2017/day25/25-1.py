import re
from tqdm import tqdm

def main():
    with open('day25/25.txt', 'r') as open_file:
        input_data = open_file.read().split('\n\n')
    
    turing_machine = Turing(input_data)
    turing_machine.run()
    turing_machine.diagnostic_checksum()

class Turing():
    def __init__(self, input_data):
        self.state = re.search(r'state (\w)', input_data[0]).group(1)
        self.target = int(re.search(r'\d+', input_data[0]).group(0))
        self.ruleset = {}
        for i in range(1, len(input_data)):
            key = re.search(r'In state (\w)', input_data[i]).group(1)
            vals = re.search(r'Write.+?(\d).+?to the (\w+).+?state (\w).+?Write.+?(\d).+?to the (\w+).+?state (\w)', input_data[i], flags= re.DOTALL)
            rule = {0: {'write': int(vals.group(1)), 'move': vals.group(2), 'shift': vals.group(3)},
                        1: {'write': int(vals.group(4)), 'move': vals.group(5), 'shift': vals.group(6)}}
            self.ruleset[key] = rule
        self.tape = {}
        self.current = 0
    
    def run(self):
        for i in tqdm(range(self.target)):
            c = self.tape.get(self.current, 0)
            rules = self.ruleset[self.state][c]
            self.tape[self.current] = rules['write']
            if rules['move'] == 'right':
                self.current += 1
            else:
                self.current -= 1
            self.state = rules['shift']
    
    def diagnostic_checksum(self):
        print(f'Result of diagnostic checksum: {sum([v for v in self.tape.values()])}')


if __name__ == '__main__':
    main()