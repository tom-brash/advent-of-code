def main():

    with open('1/1.txt', 'r') as open_file:
        input_data = open_file.read().split()

    input_data = [int(x) for x in input_data]
    
    x=0
    for i in range(3, len(input_data)):
        if input_data[i] + input_data[i-1] + input_data[i-2] > input_data[i-1] + input_data[i-2] + input_data[i-3]:
            x+= 1
    print(x)


if __name__ == '__main__':
    main()