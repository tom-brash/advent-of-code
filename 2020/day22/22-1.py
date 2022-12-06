'''
DAY 22-1: Playing a game of Combat (War)

The first part is essentially just a game of War. The input is two player's decks,
and players continue playing the top card, with the high card winning and the winner
taking both cards. 

This is straightforward - each hand can be represented as a list, and the top two cards
can be popped off their respective decks and appended to the winner's.

Each card is unique and so there are no ties, and through observation there are no 
infinite loops (could be remedied by method like in part 2)
'''

def main():
    with open('day22/22-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    player_data = input_data.split('\n\n')
    hands = []
    hands = [x.split('\n')[1:] for x in player_data]

    while len(hands[0]) > 0 and len(hands[1]) > 0:
        hands = play_hand(hands)
    
    print(hands)
    hands.remove([])
    print(calculate_score(hands[0]))


def play_hand(hands):
    card_0 = hands[0].pop(0)
    card_1 = hands[1].pop(0)
    
    print('Player 1 plays ', str(card_0))
    print('Player 2 plays ', str(card_1))

    if int(card_0) > int(card_1):
        hands[0].append(card_0)
        hands[0].append(card_1)
    else:
        hands[1].append(card_1)
        hands[1].append(card_0)
    
    return hands


def calculate_score(hand):
    hand.reverse()
    total = 0
    for i, card in enumerate(hand):
        total += int(card) * (i + 1)
    return total


if __name__ == "__main__":
    main()