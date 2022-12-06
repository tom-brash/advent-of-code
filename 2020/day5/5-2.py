'''
DAY 5-2: Find the empty seat

We can reuse the code from 5-1 to find all the seat IDs. Then it's just a
question of sorting the list and going through it until we find a gap.
'''

def main():

    with open('day5/5-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    tickets = input_data.split('\n')
    tickets.remove('')

    ticket_ids = []
    for ticket in tickets:
        ticket_ids.append(process_ticket(ticket))
    
    ticket_ids.sort()
    
    i = ticket_ids[0]

    found = False
    while not found:
        i += 1
        if i not in ticket_ids:
            found = True
            print(i)
        

def process_ticket(ticket):
    row_data = ticket[:7]
    seat_rows = range(128)
    for direction in row_data:
        seat_rows = binary_split(seat_rows, direction)
    
    col_data = ticket[7:]
    seat_cols = range(8)
    for direction in col_data:
        seat_cols = binary_split(seat_cols, direction)
    
    row = seat_rows[0]
    col = seat_cols[0]

    return row * 8 + col



def binary_split(a_list, direction):
    half = len(a_list)//2
    if direction == "F" or direction == "L":
        return a_list[:half]
    else:
        return a_list[half:]


if __name__ == '__main__':
    main()   