def main():
    target = 325489

    x_pos = 0
    y_pos = 0
    current = 1

    x_vec = 1
    y_vec = 0

    while current < target:
        x_pos += x_vec
        y_pos += y_vec
        current += 1
        #print((current, abs(x_pos) + abs(y_pos), x_pos, y_pos, x_vec, y_vec))
        if current == target:
            print(abs(x_pos) + abs(y_pos))
        if x_pos == y_pos or (x_pos < 0 and -x_pos == y_pos) or (x_pos > 0 and y_pos <= 0 and x_pos - 1 == -y_pos):
            temp = y_vec
            y_vec = x_vec
            x_vec = -temp
        

if __name__ == '__main__':
    main()