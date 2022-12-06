from collections import defaultdict
from collections import deque
from math import prod
import copy


def main():
    with open('16/16.txt', 'r') as open_file:
        input_data = open_file.read()
    
    hex_string = int(input_data, base=16)
    h_size = len(input_data) * 4
    bin_string = bin(hex_string)[2:].zfill(h_size)
    
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
        package_values = []
        if m == '0':
            offset = 22
            package_length_found = 0
            sp_length = int(bs[7: 22], base=2)
            while package_length_found < sp_length:
                sv, st, sl, slen = parse_packet(bs[22 + package_length_found:])
                total_versions += sv
                package_length_found += slen
                package_values.append(sl)
        elif m == '1':
            offset = 18
            sp_num = int(bs[7: 18], base=2)
            package_length_found = 0
            packages_found = 0
            while packages_found < sp_num:
                sv, st, sl, slen = parse_packet(bs[18 + package_length_found:])
                total_versions += sv
                package_length_found += slen
                packages_found += 1
                package_values.append(sl)
        
        eval_dict = {
            0: sum,
            1: prod,
            2: min,
            3: max,
            5: lambda vals: int(vals[0] > vals[1]),
            6: lambda vals: int(vals[0] < vals[1]),
            7: lambda vals: int(vals[0] == vals[1])
        }
        out = eval_dict[t](package_values) 
        return (total_versions, t, out, offset + package_length_found)




class Thing:
    def __init__(self, data):
        pass

if __name__ == '__main__':
    main()