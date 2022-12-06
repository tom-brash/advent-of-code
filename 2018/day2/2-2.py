'''
Day 2-2: Processing boxes

Inefficient train of thought algorithm below, featuring significant amounts
of duplicated work (should just be checking the rest of the list, and print_string
is inelegantly created) but the list is so short it doesn't meaningfully impact the 
time
'''

def main():
    with open('day2/2-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    boxes = input_data.split('\n')
    
    box_1, box_2 = find_boxes(boxes)
    print_string = ''
    for i in range(len(box_1)):
        if box_1[i] == box_2[i]:
            print_string += box_1[i]
    
    print(print_string)
    
        

def find_boxes(boxes):
    for i, box in enumerate(boxes):
        for j, check in enumerate(boxes):
            if i != j:
                same = 0
                for i in range(len(box)):
                    if box[i] == check[i]:
                        same += 1
                if same == len(box) - 1:                    
                    print('Box 1:', box)
                    print('Box 2:', check)
                    return(box, check)

if __name__ == '__main__':
    main()