def main():
    with open('day1/1.txt', 'r') as open_file:
        input_data = open_file.read()


    n = 0
    for c in input_data:
        if c == '(':
            n += 1
        else:
            n -=1
    
    print(n)

if __name__ == '__main__':
    main()