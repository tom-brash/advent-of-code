def main():
    with open('day11/11.txt', 'r') as open_file:
        input_data = open_file.read()
    
    password = [ord(c) for c in input_data]
    while True:
        password = increment(password)
        if check_password(password):
            print(''.join([chr(x) for x in password]))
            break


def increment(password):
    n = len(password) - 1
    while True:
        password[n] = (((password[n] - 97) + 1) % 26) + 97
        if password[n] != 97:
            break
        n -= 1

    return password

def check_password(password):
    
    if 105 in password:
        return False
    if 111 in password:
        return False
    if 108 in password:
        return False
    
    c_b = False
    for i in range(0, len(password) - 2):
        if password[i] == password[i + 1] - 1 == password[i + 2] - 2:
            c_b = True
            break
    
    if not c_b:
        return False
    
    i = 0
    m = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            m += 1
            i += 2
            continue
        i += 1
    if m < 2:
        return False
    return True
    

if __name__ == '__main__':
    main()