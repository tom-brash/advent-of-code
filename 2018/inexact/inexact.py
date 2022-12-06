def main():
    with open('inexact/movies2.txt', 'r') as open_file:
        input_data = open_file.read()
    
    names = input_data.split('\n')
    s = ''
    for n in names:
        s += '('
        for c in set(n):
            if c != ' ':
                s += c.lower() + '|'
        s = s[:-1] + ')'
    
    print(s)


if __name__ == '__main__':
    main()