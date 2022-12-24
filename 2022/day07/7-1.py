
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

    total = 0
    max_target_size = 100000
    known_sizes = {}
    for directory in data:
        size, _ = get_size(directory, data, known_sizes)
        if size <= 100000:
            total += size

    print("Total size of files < 100000 elf_bytes: ", total)

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
