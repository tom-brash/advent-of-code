from collections import defaultdict

def main():
    with open('day10/10.txt', 'r') as open_file:
        input_data = open_file.read()
    
    instructions = [int(i) for i in input_data.split(',')]
    s = {x:x for x in range(256)}
    
    current = 0
    skip = 0

    for i in instructions:
        marks = list(range(current, current + i))
        seq = [s[x % 256] for x in marks]
        for x, m in enumerate(marks):
            s[m % 256] = seq[-(x + 1)]
        
        current = (current + i + skip) % 256
        skip += 1
    
    print(s[0] * s[1])
        

if __name__ == '__main__':
    main()