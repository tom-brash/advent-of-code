import re

def main():
    print('==== Day 4 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    total = 0

    for card_no, card in enumerate(lines):
        points = 0
        card_no += 1
        card_details = card.split(':')[1]
        winning_nos = [int(n) for n in card_details.split('|')[0].split()]
        nos = [int(n) for n in card_details.split('|')[1].split()]

        for x in nos:
            if x in winning_nos:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        total += points
        
    print(total)


if __name__ == "__main__":
	main()
