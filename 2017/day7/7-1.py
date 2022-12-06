import re

def main():
    with open('day7/7.txt', 'r') as open_file:
        info = open_file.read().split('\n')

    supported_blocks = set()
    all_blocks = []
    for i in info:
        blocks = re.findall(r'[A-Za-z]+', i)
        all_blocks.append(blocks[0])
        for s in range(1, len(blocks)):
            supported_blocks.add(blocks[s])
    
    for b in all_blocks:
        if b not in supported_blocks:
            print(b)
            break

            

if __name__ == '__main__':
    main()