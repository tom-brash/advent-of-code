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

slices = []
for pixel in range(layer_size):
    slice_v = ''
    for layer in layers:
        slice_v += layer[pixel]
    slices.append(slice_v)

outputs = []
for i, slice_v in enumerate(slices):
    current_visible = 3
    for j in range(len(slice_v)):
        if slice_v[j] == '2':
            continue
        if slice_v[j] == '1':
            current_visible = '#'
            break
        if slice_v[j] == '0':
            current_visible = ' '
            break
    outputs.append(current_visible)

for i in range(image_h):
    print(''.join(outputs[i*image_w: i*image_w+image_w]))

