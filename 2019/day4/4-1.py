def main():
    # hard coded input data
    input_data = [271973, 785961]

    valid_numbers = 0

    for number in range(input_data[0], input_data[1]):
        num_string = str(number)
        if valid_number(num_string):
            valid_numbers += 1

        # if number % 10000 == 0:
        #     print('Just checked...', number)

    print('Total valid numbers:', valid_numbers)


def valid_number(num_string):
    ascending_check = True
    adjacent_check = False
    for i in range(1,6):
        if int(num_string[i]) < int(num_string[i-1]):
            ascending_check = False
            break

    for i in range(1,6):
        if int(num_string[i]) == int(num_string[i-1]):
            adjacent_check = True
            break
    return ascending_check and adjacent_check


if __name__ == '__main__':
    main()