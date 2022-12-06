def main():
    with open('day2/2.txt', 'r') as open_file:
        input_data = open_file.read()
    
    rows = input_data.split('\n')
    t = 0
    for r in rows:
        data = list(map(int, r.split('\t')))
        for i, x in enumerate(data):
            divisors = [d for j, d in enumerate(data) if j != i]
            for div in divisors:
                if x % div == 0:
                    t += x / div 

    print(t)
    
if __name__ == '__main__':
    main()