import re

def main():
    with open('day25/25.txt', 'r') as open_file:
        input_data = open_file.read()

    target_nums = [int(x) for x in re.findall(r'\d+', input_data)]
    r = target_nums[0]
    c = target_nums[1]

    # find which number keycode we are looking for
    n = find_sequence(r,c)
    print('n: ', n)
    
    # find the nth keycode generated
    gen = generate_keycode()
    for _ in range(n):
        x = next(gen)
    print(x)

def find_sequence(r, c):
    i = 1
    x = 1
    for _ in range(r - 1):
        i += x
        x += 1
    x += 1
    for _ in range(c - 1):
        i += x
        x += 1
    return i

def generate_keycode():
    x = 20151125
    while True:
        yield x
        x *= 252533
        x = x % 33554393

if __name__ == '__main__':
    main()