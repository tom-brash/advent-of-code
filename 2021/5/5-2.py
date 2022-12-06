from collections import defaultdict

def main():
    with open('5/5.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    lines = []
    points = defaultdict(int)    
    for x in input_data:
        x1 = int(x.split(' -> ')[0].split(',')[0])
        y1 = int(x.split(' -> ')[0].split(',')[1])
        x2 = int(x.split(' -> ')[1].split(',')[0])
        y2 = int(x.split(' -> ')[1].split(',')[1])
        lines.append((x1, x2, y1, y2))

    print(lines)

    for l in lines:
        x1, x2, y1, y2 = l
        if x1 == x2:
            low = min(y1, y2)
            high = max(y1, y2)
            for y in range(low, high + 1):
                points[(x1, y)] += 1
        elif y1 == y2:
            low = min(x1, x2)
            high = max(x1, x2)
            for x in range(low, high + 1):
                points[(x, y1)] += 1
        else:
            lowx = min(x1, x2)
            highx = max(x1, x2)
            if (x1 < x2 and y1 < y2) or (x2 < x1 and y2 < y1):
                lowx = min(x1, x2)
                highx = max(x1, x2)
                lowy = min(y1, y2)
                highy = max(y1, y2)
                for i, x in enumerate(range(lowx, highx + 1)):
                    points[(x, lowy + i)] += 1

            else:
                lowx = min(x1, x2)
                highx = max(x1, x2)
                lowy = min(y1, y2)
                highy = max(y1, y2)
                for i, x in enumerate(range(lowx, highx + 1)):
                    points[(x, highy - i)] += 1

            lowx = min(x1, x2)
            highx = max(x1, x2)
            lowy = min(y1, y2)
            highy = max(y1, y2)
            
    
    x = 0
    for k in points.values():
        if k > 1:
            x += 1
    
    print(x)

class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()