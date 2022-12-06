'''
Day 21-2: Slowest non-infinite runtime

We can infer that if there is a finite set of possible runtimes, then the equality check must eventually loop. As
a result, the check prior to the loop ending will be the slowest possible finite runtime. Unfortunately, the 
loop is long enough that running naively is too slow - we need to translate what the program is doing to regular
Python.
'''

def main():
    with open('day21/21-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    reg_4 = 65536
    reg_5 = 3935295
    outputs = set()
    
    running = True

    while True:
        condition = True
        while condition == True:
            reg_5 += reg_4 & 255
            reg_5 = reg_5 & 0xFFFFFF
            reg_5 *= 65899
            reg_5 = reg_5 & 0xFFFFFF
            condition = reg_4 >= 256
            if condition:
                reg_4 = reg_4 >> 8
            
        if reg_5 in outputs:
            print(last_output)
            break
        else:
            outputs.add(reg_5)
            last_output = reg_5
        
        reg_4 = reg_5 | 65536
        reg_5 = 3935295


if __name__ == '__main__':
    main()