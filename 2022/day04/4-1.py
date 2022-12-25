def main():
    print("====Day 4====")
    print("Cleaning up camp...")
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    total = 0
    for x in input:
        a, b = x.split(',')
        a_min, a_max = [int(i) for i in a.split('-')]
        b_min, b_max = [int(i) for i in b.split('-')]
        if (a_min >= b_min and a_max <= b_max) or (b_min >= a_min and b_max <= a_max):
            total += 1
    print(f"\n(4-1)Number of elf cleaning assignments that fully overlap: {total}")
        

if __name__ == "__main__":
    main()
