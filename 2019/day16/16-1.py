'''
DAY 16-1: Flawed Frequency Transmission

Here the seqence is short enough that we can 'accurately' update the entire
system, by using numpy dot products. The most interesting thing coding wise
here is the use of itertools to create the right numpy matrix to multiply by,
creating a sequence of the base pattern of the required length and offset
''' 

import numpy as np
from itertools import cycle, islice

def main():
    with open('day16/16-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    signal = [int(c) for c in input_data]
    for _ in range(100):
        signal = execute_phase(signal)
        #print(''.join([str(i) for i in signal]))
    signal = [str(i) for i in signal]
    print(''.join(signal[:8]))

def execute_phase(signal):
    base_pattern = [0, 1, 0, -1]
    updated_signal = []
    for i in range(len(signal)):
        pattern = [val for val in base_pattern for _ in range(i + 1)]
        a = np.array(signal)
        b = np.array(list(islice(cycle(pattern), len(signal) + 1))[1:])
        new_val = abs(np.dot(a, b)) % 10
        updated_signal.append(new_val)
    return updated_signal


if __name__ == "__main__":
    main()