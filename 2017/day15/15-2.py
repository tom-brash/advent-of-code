from tqdm import tqdm

def main():
    gen_a = 699  # input
    gen_b = 124  # input

    total = 0
    for i in tqdm(range(5000000)):
        gen_a = gen_a * 16807 % 2147483647
        while gen_a % 4 != 0:
            gen_a = gen_a * 16807 % 2147483647
        gen_b = gen_b * 48271 % 2147483647
        while gen_b % 8 != 0:
            gen_b = gen_b * 48271 % 2147483647
        if (gen_a & 0b1111111111111111) == (gen_b & 0b1111111111111111):
            total += 1
    print(total)


if __name__ == '__main__':
    main()