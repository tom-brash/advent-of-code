'''
This final assembunny challenge of the year reduces to the following:

 - Take the input number and add a constant to it (in this input, that constant is 9 * 282 = 2538).
 - Integer divide that number by 2
 - Print the number mod 2
 - Once the number gets to zero, top it up to the original (input + constant)

As we are looking for permanently alternating odd and even values, we can reverse engineer the sequence of values:
1 (odd)
2 (even)
5 (odd)
10 (even)
etc.

Once this number exceeds the constant, we can subtract the constant to get the lowest viable integer value

'''


def main():
    with open('day25/25.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    k1 = int(input_data[1].split()[1])
    k2 = int(input_data[2].split()[1])
    floor_val = k1 * k2
    n = 1
    while n < floor_val:
        if n % 2 == 0:
            n = n * 2 + 1
        else:
            n = n * 2
    print(f'Lowest possible value: {n - k1*k2}')


if __name__ == '__main__':
    main()
