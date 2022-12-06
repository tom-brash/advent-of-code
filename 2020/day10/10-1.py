'''
DAY 10-1: Determine voltage differences in adapter chain

To use all of the adapters, they have to be in order. We can find the differences
by just sorting all of the voltages first, and then looping through and keeping
track of the differences. 
'''

def main():
    with open('day10/10-1-test.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    voltages = input_data.split('\n')
    voltages = [int(x) for x in voltages]
    voltages.append(0)
    voltages.sort()
    voltages.append(voltages[-1] + 3)

    diffs = {1: 0, 2: 0, 3: 0}
    for i, volt in enumerate(voltages):
        if i != 0:
            diff = volt - voltages[i-1]
            diffs[diff] += 1
    
    print(diffs)
    print(diffs[1] * diffs[3])


if __name__ == "__main__":
    main()