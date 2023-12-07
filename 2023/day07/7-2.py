import re
from collections import Counter


class Hand:
    def __init__(self, cards, wager):
        self.cards = cards
        self.wager = wager
        self.get_jokers()
        self.score_hand()

    def get_jokers(self):
        self.jokers = self.cards.count('J')
        self.reg_cards = self.cards.replace('J','')

    def score_hand(self):
        ranks = {'2': 20, '3': 30, '4': 40, '5': 50, '6': 60, '7': 70, '8': 80, '9': 90, 'T': 91, 'J': 10, 'Q': 93, 'K': 94, 'A': 95}
        hc = sorted(Counter(self.reg_cards).values())
        if len(hc) == 0:
            hc = [5]
        else: hc[-1] = hc[-1] + self.jokers

        if hc == [5]:
            score = 7
        elif hc == [1, 4]:
            score = 6
        elif hc == [2, 3]:
            score = 5
        elif max(hc) == 3:
            score = 4
        elif hc == [1, 2, 2]:
            score = 3
        elif max(hc) == 2:
            score = 2
        else:
            score = 1

        for i in range(5):
            score += ranks[self.cards[i]] * 10**((i + 1) * -2)

        self.score = score
     

def main():
    print('==== Day 7 ====')
    with open('input', 'r') as open_file:
	    lines = open_file.read().strip().split('\n')

    hands = []
    for line in lines:
        hands.append(Hand(line.split()[0], int(line.split()[1])))

    hands = sorted(hands, key=lambda x: x.score)

    total = 0

    for i, hand in enumerate(hands, 1):
        # print(hand.cards, hand.score)
        total += i * hand.wager

    print(total)

if __name__ == "__main__":
    main()
