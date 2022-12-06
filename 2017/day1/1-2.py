with open('day1/1.txt', 'r') as open_file:
    input_data = open_file.read()

digits = {}
t = 0
for i, c in enumerate(input_data):
    digits[i] = int(c)

x = len(input_data) / 2
y = len(input_data)
for i in range(len(input_data)):
    if digits[(i + x) % y] == digits[i]:
        t += digits[i]


print(t)
