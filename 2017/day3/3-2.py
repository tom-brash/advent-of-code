def main():
    target = 325489

    x_pos = 0
    y_pos = 0
    current = 1

    x_vec = 1
    y_vec = 0

    spiral_data = {(0, 0): 1}

    while current < target:
        x_pos += x_vec
        y_pos += y_vec
        current = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                current += spiral_data.get((x_pos + i, y_pos + j), 0)
        spiral_data[(x_pos, y_pos)] = current
        if current > target:
            print(current)
        if x_pos == y_pos or (x_pos < 0 and -x_pos == y_pos) or (x_pos > 0 and y_pos <= 0 and x_pos - 1 == -y_pos):
            temp = y_vec
            y_vec = x_vec
            x_vec = -temp
        

if __name__ == '__main__':
    main()