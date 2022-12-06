
import time

def main():

    start_time = time.time()
    with open('8/8.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    display = {frozenset(['a','b', 'c', 'e', 'f', 'g']): '0',
        frozenset(['c','f']): '1',
        frozenset(['a', 'c', 'd', 'e', 'g']): '2',
        frozenset(['a', 'c', 'd', 'f', 'g']): '3',
        frozenset(['b', 'c', 'd', 'f']): '4',
        frozenset(['a','b', 'd', 'f', 'g']): '5',
        frozenset(['a','b', 'd', 'e', 'f', 'g']): '6',
        frozenset(['a', 'c', 'f']): '7',
        frozenset(['a','b', 'c', 'd', 'e', 'f', 'g']): '8',
        frozenset(['a','b', 'c', 'd', 'f', 'g']): '9'}

    lengths = {2: set(['c', 'f']), 
        3: set(['a', 'c', 'f']), 
        4: set(['b', 'c', 'd', 'f'])}

    exclusions = {5: set(['a', 'd', 'g']),
        6: set(['a', 'b', 'f', 'g'])} 

    t = 0
    for i in input_data:
        # define possibility space
        possibilities = {}
        for signal in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            possibilities[signal] = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        
        signal_string = i.split(' | ')[0]
        output_string = i.split(' | ')[1]
        signals = signal_string.split()
        for signal in signals:
            # if length of signal corresponds to unique output number...
            if len(signal) in [2, 3, 4]:
                # limit the possibilities of signals to those unique outputs...
                for c in signal:
                    possibilities[c] = lengths[len(signal)].intersection(possibilities[c])
                # and remove those outputs from rest of possibilities
                for k in possibilities.keys():
                    if k not in signal:
                        possibilities[k] -= lengths[len(signal)]
            # if signal lengths is 5, nothing in the signal can be 'a', 'd', or 'g' (by observation of shared signals)
            elif len(signal) in [5, 6]:
                for c in signal:
                    for k in possibilities.keys():
                        if k not in signal:
                            possibilities[k] -= exclusions[len(signal)]
        
        # find unique values and remove them from all other signal option sets; iterate until each signal has unique output
        unique = False
        while not unique:
            for letter in possibilities.keys():
                if len(possibilities[letter]) == 1:
                    for k in possibilities.keys():
                        if k != letter:
                            possibilities[k] -= possibilities[letter]
            unique = True
            for x in possibilities.values():
                if len(x) != 1:
                    unique = False
        
        # display full number and convert to integer
        full_num = ''
        for out in output_string.split():
            possibility_lists = frozenset([next(iter(possibilities[x])) for x in out])
            full_num += display[possibility_lists]
        # print(full_num)
        t += int(full_num)
    
    # print total
    print(t)

    print(f'Part 2 time taken: {round((time.time() - start_time) * 1000, 3)} ms')
        
    
if __name__ == '__main__':
    main()
    