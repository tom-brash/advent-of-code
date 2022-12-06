'''
Day 4-1: Guard sleeping patterns

Here we try and find the guard who sleeps the most, and then the minute that 
guard is most regularly asleep. This isn't a difficult problem, but the amount of
sorting and parsing of the string makes it a little awkward (as the mess of code
below suggests)
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
                guards[current_guard] = {'total': 0}
        
        # set the most recent 'fell asleep' time
        elif 'falls' in event:
            fell_asleep = time
        
        # add the minutes asleep to the details in the guards dictionary
        else:
            if today not in guards[current_guard]:
                guards[current_guard][today] = []
            for t in range(fell_asleep, time):
                guards[current_guard][today].append(t)
            guards[current_guard]['total'] += time - fell_asleep


    # find the sleepiest guard
    max_sleep_mins = 0  
    for key, val in guards.items():
        if val['total'] > max_sleep_mins:
            max_sleep_mins = val['total']
            sleepiest_guard = key
    
    print('Guard #%s is the sleepiest_guard' %sleepiest_guard)
    
    # find which minute was most slept on for that guard
    min_idle = defaultdict(int)

    for key, val in guards[sleepiest_guard].items():
        if key != 'total':
            for min in val:
                min_idle[min] += 1

    max_idle = max(min_idle.values())
    minute_with_max_idle = [k for k, v in min_idle.items() if v == max_idle][0]

    print('Minute with the most sleep:', minute_with_max_idle)
    print('Final answer:', int(sleepiest_guard) * minute_with_max_idle)
        

if __name__ =='__main__':
    main()