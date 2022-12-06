'''
Day 23-1: Finding bots in range of widest radius bot

This one is vastly simpler than Part 2. We just find the bot that has the widest radius,
and then scan all the otehr bots to see which one have a 3D manahttan distance less than that 
radius.

Bots created as classes in anticipation of something nasty in part 2, which I completely underestimated
'''

import re

def main():
    with open('day23/23-1-input.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    max_range = 0
    bots = {}
    match_string = re.compile(r'pos\=\<(\-?[0-9]+)\,(\-?[0-9]+)\,(\-?[0-9]+)\>\,\ r\=(\-?[0-9]+)')
    for i, line in enumerate(input_data):
        m = re.match(match_string, line)
        x = int(m.group(1))
        y = int(m.group(2))
        z = int(m.group(3))
        radius = int(m.group(4))
        if radius > max_range:
            max_range = radius
            max_bot = i
        bots[i] = Nanobot(x, y, z, radius)
    
    best = bots[max_bot]
    
    total = 0
    for key, bot in bots.items():
        if best.check_in_range(bot):
            total += 1
    
    print(total)

class Nanobot:
    def __init__(self, x, y, z, radius):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
    
    def check_in_range(self, bot):
        manhattan = abs(bot.x - self.x) + abs(bot.y - self.y) + abs(bot.z - self.z)
        if manhattan <= self.radius:
            return True
        return False

if __name__ == '__main__':
    main()