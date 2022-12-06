def main():
    with open('day1/1.txt', 'r') as open_file:
        input_data = open_file.read()

    n = 0
    for i, c in enumerate(input_data):
        if c == '(':
            n += 1
        else:
            n -=1
        if n == -1:
            print(i + 1)
            break
    
if __name__ == '__main__':
    main()