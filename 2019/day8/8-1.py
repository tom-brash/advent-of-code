with open('day8/8-1-input.txt', 'r') as input_file:
    input_data = input_file.read()

picture_data = str(input_data[:-1])
image_w = 25
image_h = 6
layer_size = image_h * image_w
image_l = len(picture_data) / layer_size


layers = []
for i in range(int(image_l)):
    layers.append(picture_data[i*layer_size: i*layer_size + layer_size])

min_zero = image_w * image_h + 1
current_answer = 0

for layer in layers:
    zeroes = layer.count('0')
    if zeroes < min_zero:
        min_zero = zeroes
        current_answer = layer.count('1') * layer.count('2')
        identified_layer = layer

print('Final answer:', current_answer)