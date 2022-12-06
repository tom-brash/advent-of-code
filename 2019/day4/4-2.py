def main():
    # hard coded input data
    input_data = [271973, 785961]

    valid_numbers = 0

    for number in range(input_data[0], input_data[1]):
        num_string = str(number)
        if valid_number(num_string):
            valid_numbers += 1

    print('Total valid numbers:', valid_numbers)


def valid_number(num_string):
    ascending_check = True
    adjacent_check = False
    open_for_double = [1,1,1,1,1,1]  # doubles can be in any part of the sequence
    for i in range(1,6):
        if int(num_string[i]) < int(num_string[i-1]):
            ascending_check = False
            break

    #check for triples (invalidating doubles)
    for i in range(2,6):
        if int(num_string[i]) == int(num_string[i-1]) == int(num_string[i-2]):
            open_for_double[i] = 0
            open_for_double[i-1] = 0
            open_for_double[i-2] = 0

    # check for valid doubles
    for i in range(1,6):
        if int(num_string[i]) == int(num_string[i-1]):
            if open_for_double[i] == 1 and open_for_double[i-1] == 1:
                adjacent_check = True
                break
    return ascending_check and adjacent_check


if __name__ == '__main__':
    main()