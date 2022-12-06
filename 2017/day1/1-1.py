with open('day1/1.txt', 'r') as open_file:
    input_data = open_file.read()

digits = {}
t = 0
for i, c in enumerate(input_data):
    digits[i] = c
    if c == digits.get(i - 1):
        t += int(c)

if digits[0] == digits[len(input_data) - 1]:
    t += int(digits[0])

print(t)
