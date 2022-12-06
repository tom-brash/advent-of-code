from collections import defaultdict
from collections import deque
import copy


def main():
    with open('16/16.txt', 'r') as open_file:
        input_data = open_file.read()
    
    hex_string = int(input_data, base=16)
    h_size = len(input_data) * 4
    bin_string = bin(hex_string)[2:].zfill(h_size)
    
    print(bin_string)
    print(parse_packet(bin_string))


def parse_packet(bs):
    global total
    total_versions = int(bs[:3], base=2)
    
    t = int(bs[3:6], base=2)
    
    if t == 4:
        lit = ''
        i = 0
        n = bs[6 + i*5]
        while n == '1':
            lit += bs[7 + i*5: 11 + i*5]
            i += 1
            n = bs[6 + i*5]
        lit += bs[7 + i*5: 11 + i*5]
        l = int(lit, base=2)
        #print(f'Found literal {l}')
        return (total_versions, t, l, 11 + i*5)  # version, type, literal, length
    
    else:
        m = bs[6]
        if m == '0':
            package_length_found = 0
            sp_length = int(bs[7: 22], base=2)
            while package_length_found < sp_length:
                sv, st, sl, slen = parse_packet(bs[22 + package_length_found:])
                total_versions += sv
                package_length_found += slen
            return (total_versions, t, None, 22 + sp_length)
        elif m == '1':
            sp_num = int(bs[7: 18], base=2)
            package_length_found = 0
            packages_found = 0
            while packages_found < sp_num:
                sv, st, sl, slen = parse_packet(bs[18 + package_length_found:])
                total_versions += sv
                package_length_found += slen
                packages_found += 1
            return (total_versions, t, None, 18 + package_length_found)





class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()