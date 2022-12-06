'''
DAY 16-2: Flawed Frequency Transmission

Here the seqence is far too long to run the 'correct' math on all of the items in the list.
However, we observe that the back half of the list (which is where the offset makes us look) is 
a simpler pattern - the base pattern is multiplied sufficiently that the update is simply the
sum of itself and all subsequent numbers (modulo 10 as usual).

We can rapidly calculate this much more quickly, concerning ourselves only with the subsection of the
original input corresponding to the required sequence after offsetting.
''' 

import numpy as np
from itertools import cycle, islice
import tqdm

def main():
    with open('day16/16-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    signal = [int(c) for c in input_data] * 10000
    offset = int(''.join([str(x) for x in signal[:7]]))
    print('offset', offset)
    signal = signal[offset:]
    print(len(signal))
    
    for _ in tqdm.tqdm(range(100)):
        signal = execute_phase(signal)
    
    print(''.join([str(x) for x in signal[:8]]))

def execute_phase(signal):
    updated_signal = []
    total = sum(signal)
    for i in range(len(signal)):
        new_val = total % 10
        updated_signal.append(new_val)
        total -= signal[i]       
    return updated_signal


if __name__ == "__main__":
    main()