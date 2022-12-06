import tqdm

def main():
    jump = 328
    spinlock = {0: 0}
    current = 0
    next_num = 1

    for i in range(2017):
        current = find_next(spinlock, current)
        temp = spinlock[current]
        spinlock[current] = next_num
        spinlock[next_num] = temp
        next_num += 1
        current = spinlock[current]
        # print(spinlock)
    
    print(spinlock[2017])



def find_next(spinlock, current, jump=328):
    for i in range(jump):
        current = spinlock[current]
    
    return current


if __name__ == '__main__':
    main()