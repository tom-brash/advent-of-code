'''
DAY 22-2: Playing a game of Recursive Combat

Here we play a modified version of the game using recursive rules.
If after playing a card each player has at least n cards in their deck,
where n is the value of the card they just played, instead of using the 
high card to determine the winner, they play another game of Recursive
Combat using the top n cards of their decks.

Infinite loop detection is put in place here by just keeping a list of 
previous game states and testing whether it is identical before playing
out the hand.

Otherwise it is a relatively straightforward recursive relationship. An
extra variable is kept track of for the total number of games for the sake
of interest.

Various print blocks have been commented out but can be used for detail and 
debugging. However, close to 20k individual games end up being played and 
it is not recommended to leave them uncommented. 

Note this code takes ~1min to run.
'''

import copy

def main():
    with open('day22/22-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    player_data = input_data.split('\n\n')
    hands = []
    hands = [x.split('\n')[1:] for x in player_data]

    winner, hands, total_games = play_recursive_combat(hands, 1, 0)

    print('Winner hand score: ', str(calculate_score(hands[winner])))
    print('Total games required: ', str(total_games))
    

def play_recursive_combat(hands, depth, total_games):
    #print('Starting game at depth ', depth)
    #print()
    previous_hands = []
    while len(hands[0]) > 0 and len(hands[1]) > 0:
        if hands in previous_hands:
            #print('Infinite loop detected... winner is player 0')
            return 0, hands, total_games + 1
        previous_hands.append(copy.deepcopy(hands))

        card_0 = hands[0].pop(0)
        card_1 = hands[1].pop(0)
        
        #print('Player 1 plays ', str(card_0))
        #print('Player 2 plays ', str(card_1))

        if len(hands[0]) >= int(card_0) and len(hands[1]) >= int(card_1):
            #print('Recursive game required...')
            next_game_hands = [hands[0][:int(card_0)], hands[1][:int(card_1)]]
            hand_winner, _, total_games = play_recursive_combat(next_game_hands, depth + 1, total_games)
            #print('Back to game at depth ' + str(depth))
            #print()
        
        else:
            if int(card_0) > int(card_1):
                hand_winner = 0
            else:
                hand_winner = 1
        
        #print('Winner of the round is player ', str(hand_winner + 1))

        if hand_winner == 0:
            hands[0].append(card_0)
            hands[0].append(card_1)
        else:
            hands[1].append(card_1)
            hands[1].append(card_0)

    if len(hands[1]) == 0:
        return 0, hands, total_games + 1
    else:
        return 1, hands, total_games + 1        


def calculate_score(hand):
    hand.reverse()
    total = 0
    for i, card in enumerate(hand):
        total += int(card) * (i + 1)
    return total


if __name__ == "__main__":
    main()