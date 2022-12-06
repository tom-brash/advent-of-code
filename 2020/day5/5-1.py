'''
DAY 5-1: Binary search through plane seats

We split each ticket into the binary instructions to process the row, and
the binary instructions to process the columns.

We then use a binary search helper function in order to uniquely determine
the seat.
'''

def main():

    with open('day5/5-1-input.txt', 'r') as input_data_file:
        input_data = input_data_file.read()

    tickets = input_data.split('\n')
    tickets.remove('')

    max = 0
    for ticket in tickets:
        val = process_ticket(ticket)
        if val > max:
            max = val
    
    print(max)


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