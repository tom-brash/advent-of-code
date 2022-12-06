'''
Day 2-1: Processing boxes

Trivial problem looking at strings with exactly 2 or 3 instances of each character.
Using sets for speed, but nothing much to see here
'''

def main():
    with open('day2/2-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    boxes = input_data.split('\n')
    
    two_boxes = 0
    three_boxes = 0
    
    for box in boxes:
        f_two = False
        f_three = False
        bc = set([c for c in box])
        for c in bc:
            count = box.count(c)
            if count == 2:
                f_two = True
            if count == 3:
                f_three = True
        
        if f_two:
            two_boxes += 1
        if f_three:
            three_boxes += 1
    
    print('Final answer:', two_boxes * three_boxes)

if __name__ == '__main__':
    main()