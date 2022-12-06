from collections import defaultdict
from collections import deque
import math
import re


def main():
    with open('18/18.txt', 'r') as open_file:
        input_data = open_file.read()
    
    a = '[[[0,[6,6]],[[7,2],[6,2]]],[[[9,4],[5,8]],6]]'
    
    for num in input_data.split('\n')[1:]:
        a = s_add(a, num)
        #print('problem start', a)
        a = [int(c) if c.isnumeric() else c for c in a]
        a = reduce(a)
        a = ''.join([str(v) for v in a])
    #print(a)
    a_fish = parse(a)
    print(a_fish.magnitude())
    

def reduce(s):
    stable = False
    while not stable:
        stable = True
        level = 0
        exploding_string = ''
        finished = False
        rightmost_i = None
        leftmost_i = None
        exploding_i = None
        exploding_end = None
        for i in range(len(s)):
            if s[i] == '[':
                if level != 5:
                    level += 1
            elif s[i] == ']':
                if level == 5 and not finished:
                    finished = True
                    exploding_end = i
                level -= 1
            elif level == 5 and not finished:
                if exploding_i == None:
                    exploding_i = i
            elif s[i] != ',':
                if level != 5 and not finished:
                    rightmost_i = i
                elif finished:
                    leftmost_i = i
                    break
            
        
        if exploding_i != None:
            stable = False
            exploding_bit = ''.join([str(v) for v in s[exploding_i: exploding_end]])
            #print(exploding_bit)
            exploding_nums = [int(x) for x in re.findall('\d+', exploding_bit)]
            if rightmost_i != None:
                s[rightmost_i] = s[rightmost_i] + exploding_nums[0]
            if leftmost_i != None:
                s[leftmost_i] = s[leftmost_i] + exploding_nums[1]
            s = s[:exploding_i - 1] + [0] + s[exploding_end + 1:]
            #continue
        
        if exploding_i == None:
            for i in range(len(s)):
                if s[i] not in ['[', ']', ',']:
                    if int(s[i]) > 9:
                        #print('too high!', int(s[i]))
                        l = math.floor(int(s[i]) / 2)
                        r = math.ceil(int(s[i]) / 2)
                        s = s[:i] + ['[', l, ',', r, ']'] + s[i + 1:]
                        stable = False
                        break
        
        #print(''.join([str(v) for v in s]))
    return s

        
def s_add(a, b):
    sn = '[' + a + ',' + b + ']'
    return sn
    
    
def parse(s, degree=0):
    level = 0
    p = 0
    while p < len(s):
        if level == 1:
            if s[p] == ',':
                break
        if s[p] == '[':
            level += 1
        elif s[p] == ']':
            level -= 1
        p += 1
    l = s[1:p]
    r = s[p + 1:-1]
    if '[' in l:
        l = parse(l, degree + 1)
    if '[' in r:
        r = parse(r, degree + 1)
    return Smallfish(l, r, degree)

class Smallfish:
    def __init__(self, l, r, degree):
        #self.parent = parent
        self.l = l
        self.r = r
        self.degree = degree

    def magnitude(self):
        if isinstance(self.l, str):
            lm = int(self.l)
        else:
            lm = self.l.magnitude()
        if isinstance(self.r, str):
            rm = int(self.r)
        else:
            rm = self.r.magnitude()
        return lm * 3 + rm * 2


if __name__ == '__main__':
    main()