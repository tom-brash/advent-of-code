import hashlib

def main():
    with open('day4/4.txt', 'r') as open_file:
        input_data = open_file.read()

    n = 0
    found = False
    while not found:
        n += 1
        attempt = input_data + str(n)
        result = hashlib.md5(attempt.encode()).hexdigest()
        if result[:5] == '00000':
            print(result)
            found = True
    print(n)


if __name__ == '__main__':
    main()