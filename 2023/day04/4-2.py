import re
from collections import defaultdict

def main():
    print('==== Day 4 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    card_count = {}
    for i in range(len(lines)):
        card_count[i+1] = 1


    for card_no, card in enumerate(lines):
        matches = 0
        card_no += 1

        num_cards = card_count[card_no]
        card_details = card.split(':')[1]
        winning_nos = [int(n) for n in card_details.split('|')[0].split()]
        nos = [int(n) for n in card_details.split('|')[1].split()]

        for x in nos:
            if x in winning_nos:
                matches += 1

        for i in range(matches):
            target = card_no + i + 1
            if target in card_count:
                card_count[target] += num_cards

    print(sum(card_count.values()))

if __name__ == "__main__":
	main()
