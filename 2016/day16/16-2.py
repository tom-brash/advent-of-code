def main():
    seed_string = '01110110101001000'
    dragon = dragon_curve(seed_string, 35651584)
    print(f'Checksum for initial seed is {checksum(dragon)}')

def dragon_curve(seed, n):
    dragon_string = seed
    while len(dragon_string) < n:
        segment = process_string(dragon_string)
        dragon_string += '0'
        dragon_string += segment
    return dragon_string[:n]

def process_string(s):
    r = s[::-1]
    d = {'0': '1', '1': '0'}
    return ''.join([d[c] for c in r])

def checksum(s):
    d = {'00': '1', '11': '1'}
    while len(s) % 2 == 0:
        s = ''.join([d.get(s[i * 2] + s[i * 2 + 1], '0') for i in range(len(s) // 2)])
    return s

if __name__ == '__main__':
    main()
