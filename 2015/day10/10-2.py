def main():
    with open('day10/10.txt', 'r') as open_file:
        input_data = open_file.read()
    
    current_string = input_data
    for _ in range(50):
        new_string = ''
        c = current_string[0]
        x = 1
        for i in range(1, len(current_string)):
            if current_string[i] == c:
                x += 1
            else:
                new_string += str(x)
                new_string += c
                c = current_string[i]
                x = 1
        new_string += str(x)
        new_string += c
        current_string = new_string
    print(len(new_string))


if __name__ == '__main__':
    main()