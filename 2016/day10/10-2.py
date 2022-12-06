import re
def main():
    with open('day10/10.txt', 'r') as open_file:
        instructions = open_file.read().split('\n')
    
    bot_floor = BotFloor(instructions)
    bot_floor.run()
    a = bot_floor.get_output(0)
    b = bot_floor.get_output(1)
    c = bot_floor.get_output(2)
    print(a * b * c)


class BotFloor:
    def __init__(self, instructions):
        self.instructions = instructions
        self.bot_list = {}
        self.output_list = {}
        for i in instructions:            
            nums = re.findall(r'\d+', i)
            if i[:5] == 'value':                                
                self.add_val(int(nums[1]), int(nums[0]))
            else:
                outs = re.findall(r'\w+\ \d+', i)
                self.add_instruct(int(nums[0]), outs[1].split(), outs[2].split())

    def add_val(self, n, v):
        if n not in self.bot_list:
            self.add_bot(n)
        self.bot_list[n].add_val(v)
    
    def add_output_val(self, n, v):
        if n not in self.output_list:
            self.output_list[n] = []
        self.output_list[n].append(v)

    def add_instruct(self, n, o1, o2):
        if n not in self.bot_list:
            self.add_bot(n)
        o1[1] = int(o1[1])
        o2[1] = int(o2[1])
        self.bot_list[n].low_out = o1
        self.bot_list[n].high_out = o2
        
    def add_bot(self, n):
        n_bot = Bot(n)
        self.bot_list[n] = n_bot

    def operation(self, n):
        current_bot = self.bot_list[n]
        current_bot.carrying.sort()
        low = current_bot.carrying[0]
        high = current_bot.carrying[1]
        if low == 17 and high == 61:
            print(n)
        if current_bot.low_out[0] == 'output':
            self.add_output_val(current_bot.low_out[1], low)
        else:
            self.add_val(current_bot.low_out[1], low)
        if current_bot.high_out[0] == 'output':
            self.add_output_val(current_bot.high_out[1], high)
        else:
            self.add_val(current_bot.high_out[1], high)
        
        current_bot.carrying = []
    
    def run(self):
        updated = True
        while updated:
            updated = False
            for key, bot in self.bot_list.items():
                if len(bot.carrying) == 2:
                    updated = True
                    self.operation(key)

    def printout(self):
        for bot in self.bot_list.values():
            bot.print_bot()
    
    def get_output(self, n):
        return self.output_list[n][0]


class Bot:
    def __init__(self, n):
        self.carrying = []
        self.n = n
        self.low_out = None
        self.high_out = None
    
    def add_val(self, v):
        self.carrying.append(v)
    
    def print_bot(self):
        print('Bot name: ', self.n)
        print('Carrying: ', self.carrying)
        print('Low goes to: ', self.low_out)
        print('High goes to: ', self.high_out)

    
if __name__ == '__main__':
    main()