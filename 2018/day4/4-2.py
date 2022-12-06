'''
Day 4-2: Guard sleeping patterns (2)

The solution to this one fits more or less neatly into the logic used for #1 (suggesting
the method for #1 was gratuitiously overkill). We just keep track of each minute for 
each guard, incrementing the count by one every time we find the guard asleep on that minute
'''

import re
from collections import defaultdict
from pprint import pprint

def main():
    with open('day4/4-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    events = input_data.split('\n')
    events.sort()  # important step of sorting the data, necessary for the method used
    guards = defaultdict(dict)

    # run through events in order
    for event in events:
        
        # parse out details of string
        date_time = re.search(r'\[1518\-(.*?)\]', event)[1]
        month = int(date_time.split('-')[0])
        day = int(date_time.split('-')[1][:2])
        time = int(date_time.split(':')[1])       
        
        today = (month, day)

        # set the current guard
        if 'Guard' in event:
            current_guard = re.search(r'\#([0-9]+)', event)[1]
            if current_guard not in guards:
                guards[current_guard] = {'min_idle': defaultdict(int)}
        
        # set the most recent 'fell asleep' time
        elif 'falls' in event:
            fell_asleep = time
        
        # add the minutes asleep to the details in the guards dictionary
        else:
            for t in range(fell_asleep, time):
                guards[current_guard]['min_idle'][t] += 1


    max_times_idle = 0
    for guard in guards.keys():
        for minute in guards[guard]['min_idle'].keys():
            if guards[guard]['min_idle'][minute] > max_times_idle:
                max_times_idle = guards[guard]['min_idle'][minute]
                g = guard
                m = minute
    
    print('Guard:', g)
    print('Minute with the most sleep:', m)
    print('Final answer:', int(g) * m)
        

if __name__ =='__main__':
    main()