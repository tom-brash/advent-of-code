'''
DAY 25-1: Identifying cryptographic handshake

The final day requires identifying a matching 'cryptographic handshake' between a door and key.

Given the 'public key' of both the door and the key, we can work backwards to find the number
of 'cycles' that the door or key runs a particular rule: multiplying a subject number (7) by the 
current value and then taking the remainder when dividing by 20201227.

After getting the cycle numbers, there is redundant information. The answer can be obtained by
either by applying the door cycle number using the card public key as the subject number, or else
using the card cycle number using the door public key as the subject number.

Either approach gives the answer. 

Uniquely, there is no second part, so this is the only file for today.
'''

def main():
    with open('day25/25-1-input.txt', 'r') as input_file:
        input_data = input_file.read()
    
    card_public_key = int(input_data.split('\n')[0])
    door_public_key = int(input_data.split('\n')[1])

    # get cycle numbers for card and door
    card_cycle = find_cycle_from_public_key(card_public_key)
    door_cycle = find_cycle_from_public_key(door_public_key)

    # find answer using door_cycle and card_public_key
    value = 1
    for _ in range(door_cycle):
        value = run_cycle(card_public_key, value)

    answer_1 = value
    print('Value using door cycle and card public key: ', value)

    # cross check answer using card_cycle and door_public_key
    value = 1
    for _ in range(card_cycle):
        value = run_cycle(door_public_key, value)
    
    answer_2 = value
    print('Cross check: ', value)

    # confirm that answers are matched
    if answer_1 == answer_2:
        print('Answers match!')
    else:
        print('No matching answers found')


# given a public key, work backwards to the number of cycles used
def find_cycle_from_public_key(public_key):
    value = 1
    cycle = 0
    while value != public_key:
        value = run_cycle(7, value)
        cycle += 1
    return cycle


# run a single cycle using a subject number and current value
def run_cycle(subject_number, value):
    value = value * subject_number
    value = value % 20201227
    return value



if __name__ == "__main__":
    main()