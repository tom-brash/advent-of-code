def main():
    target = 325489
    target = 27

    last_odd = 1
    min_dist = 0
    while last_odd ** 2 < target:
        last_odd += 2
        min_dist += 1

    print(last_odd ** 2)
    print(min_dist)

if __name__ == '__main__':
    main()