
import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    current_path = "home"
    data = {}

    for x in input:
        if x[0] == "$":
            if "$ ls" in x:
                continue
            elif "cd" in x:
                instruction = x.split(' ')[-1]
                if instruction == '/':
                    current_path = 'home'
                elif instruction == '..':
                    current_path = current_path.rsplit('/', 1)[0]
                else:
                    current_path += f'/{instruction}'
        else:
            t, n = x.split(' ')
            if current_path not in data:
                data[current_path] = []
            if t == "dir":
                data[current_path].append(current_path + '/' + n)
            else:
                data[current_path].append(int(t))

    known_sizes = {}

    drive_size = 70000000

    total_size, known_sizes = get_size("home", data, known_sizes)
    req_space = 30000000 - (70000000 - total_size)
    
    best_size = 999999999
    best_dir = None

    for d, s in known_sizes.items():
        if s >= req_space and s < best_size:
            best_dir = d
            best_size = s

    print(f'Total file space on drive: {drive_size} elf_bytes')
    print(f'Used space on drive: {total_size}')
    print(f'Requred additional space to download update: {req_space}')
    print(f'Recommended for deletion: {best_dir} of size {best_size}')

def get_size(d, data, known_sizes):
    size = 0
    contents = data[d]
    for f in contents:
        if isinstance(f, int):
            size += f
        else:
            if f in known_sizes:
                size += known_sizes[f]
            else:
                content_size, known_sizes = get_size(f, data, known_sizes)
                size += content_size
    known_sizes[d] = size
    return size, known_sizes

if __name__ == "__main__":
    main()
