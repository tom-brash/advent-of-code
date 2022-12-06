with open('times.txt', 'r') as open_file:
    times = open_file.read().split('\n')

total = 0
for t in times:
    time = t.split()[3]
    m = float(time.split('\.')[0])
    s = float(time.split('\.')[0])

    m += s / 60
    total += m

remaining = 25 - len(times)
hours = int(total // 60)
mins = int((total % 60) // 1)
s = int((total % 60) % 1 * 60)
total = round(total / 60, 2)

print(f'Completed {len(times)} days with a total time of {hours} hours, {mins} minutes, and {s} seconds')
if remaining != 0:  
    print(f'\n{remaining} days remaining, with average time of {round((24 - total) / remaining, 2)}h per problem')
print(f'\nAverage time so far: {round(total / len(times), 2)}h')