from tqdm import tqdm
from collections import deque

def main():
    jump = 328
    spinlock = deque([0])
    for i in tqdm(range(1, 50000001)):
        spinlock.rotate(-jump)
        spinlock.append(i)
    
    zero_index = spinlock.index(0)
    print(spinlock[zero_index + 1])


if __name__ == '__main__':
    main()