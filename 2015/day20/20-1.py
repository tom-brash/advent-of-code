from functools import reduce

def main():
    with open('day20/20.txt', 'r') as open_file:
        input_data = int(open_file.read())
    
    n = 1
    while True:
        f = get_factors(n)
        if f >= input_data:
            print(n)
            break
        #print(n, f)
        if n % 10000 == 0:
            print(n, f)
        n += 1

def get_factors(n):
    f =  list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    return sum([10 * x for x in f])
    


if __name__ == '__main__':
    main()