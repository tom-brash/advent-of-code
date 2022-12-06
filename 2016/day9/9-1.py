import re
def main():
    with open('day9/9.txt', 'r') as open_file:
        code = open_file.read()

    decompressed = ''
    n = 0
    while n < len(code):
        if code[n] == '(':
            current_marker = re.match(r'\((\d+)x(\d+)\)', code[n:])
            n += len(current_marker.group(0))
            for i in range(int(current_marker.group(2))):
                decompressed += code[n: n + int(current_marker.group(1))]
            n += int(current_marker.group(1))
        else:
            decompressed += code[n: n + 1]
            n += 1
    
    print(len(decompressed))



if __name__ == '__main__':
    main()