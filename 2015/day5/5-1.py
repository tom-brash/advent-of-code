import re

def main():
    with open('day5/5.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')


    total = 0
    for s in input_data:
        if len(re.findall(r'[aeiou]', s)) >= 3:
            if len(re.findall(r'(.)\1{1,}', s)) > 0:
                if len(re.findall(r'(ab|cd|pq|xy)', s)) == 0:
                    total += 1
    
    print(total)



if __name__ == '__main__':
    main()