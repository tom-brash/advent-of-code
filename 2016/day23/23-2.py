'''
As is common for this style of puzzle, the input instructions mimic some more traditional operations,
with some amount of disguising to make the output pattern non-obvious.

Here the pattern simply returns the factorial of the provided input (12), plus a constant which is 
effectively provided in the puzzle input by lines 20 and 21. After toggling the lines, both of these
are 'cpy' instructions, and the inc/dec/jnz instructions that follow simply transfer their product
to the output register.

This also works for part 1
'''

def main():
    with open('day23/23.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    easter_eggs = 12  # part of advent puzzle
    key_1 = int(input_data[19].split()[1])
    key_2 = int(input_data[20].split()[1])

    print(factorial(easter_eggs) + key_1 * key_2)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    main()