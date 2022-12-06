import re

def main():
    with open('day7/7.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    total_valid = 0

    for address in input_data:
        found = False
        hyper_seqs = re.findall(r'\[(\w+)\]', address)        
        super_address = re.sub(r'\[(\w+)\]', '[]', address)
        seqs = re.findall(r'\w+', super_address)
        possible_bab = set()
        for seq in hyper_seqs:
            possible_bab |= (aba_check(seq))
        for bab in possible_bab:
            for seq in seqs:
                if bab in seq:
                    total_valid += 1
                    found = True
                    break
            if found:
                break

    print(f'Number of valid sequences: {total_valid}')        


def aba_check(s):
    potential = set()
    
    if len(s) < 3:
        return potential
    
    for i in range(2, len(s)):
        if s[i] == s[i - 2]:
            if s[i] != s[i - 1]:
                potential.add(''.join([s[i - 1], s[i], s[i - 1]]))
   
    return potential

if __name__ == '__main__':
    main()