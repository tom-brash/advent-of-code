import re

def main():
    with open('day7/7.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')

    total_valid = 0

    for address in input_data:
        seqs = re.findall(r'\w+', address)
        hyper_seqs = re.findall(r'\[(\w+)\]', address)
        valid = True
        for seq in hyper_seqs:
            if abba_check(seq) == True:
                valid = False
                break
        if valid:
            for seq in seqs:
                if abba_check(seq) == True:
                    total_valid += 1
                    break

    print(total_valid)        


def abba_check(s):
    if len(s) < 4:
        return False
    
    for i in range(3, len(s)):
        if s[i] == s[i - 3]:
            if s[i - 1] == s[i - 2]:
                if s[i] != s[i - 1]:
                    return True
    
    return False

if __name__ == '__main__':
    main()