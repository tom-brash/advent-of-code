from collections import Counter

def main():
    with open('21/21.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    p1_start = int(input_data[0][-1])
    p2_start = int(input_data[1][-1])
    universes = Counter(((p1_start, p2_start, 0, 0),))
    ongoing = set()
    ongoing.add((p1_start, p2_start, 0, 0))
    outcomes_dict = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

    turn_count = 0
    q_die_rolls = 0
    while len(ongoing) > 0:
        # move player 1
        new_universes = Counter()
        for u in ongoing:
            f = universes[u]
            q_die_rolls += 1 * f
            universes[u] = 0            
            x, y, xt, yt = u
            if turn_count % 2 == 0:  
                for i, j in outcomes_dict.items():
                    nx = (x - 1 + i) % 10 + 1
                    new_universes[(nx, y, xt + nx, yt)] += j * f
                    
            else:
                for i, j in outcomes_dict.items():
                    ny = (y - 1 + i) % 10 + 1
                    new_universes[(x, ny, xt, yt + ny)] += j * f
        universes += new_universes
        ongoing = {z for z in universes.keys() if z[2] < 21 and z[3] < 21}
        turn_count += 1
        
    p1_total = 0
    p2_total = 0
    for x, y in universes.items():
        if x[2] >= 21:
            p1_total += y
        else:
            p2_total += y
    
    winner = ''
    if p1_total > p2_total: winner = 'Player 1'
    else: winner = 'Player 2'

    print(f'Winner is {winner} with {max(p1_total, p2_total)} wins in {p1_total + p2_total} universes')
    print(f'There were {len(universes.keys())} unique game states considered')
    print(f'The quantum die was rolled {q_die_rolls} times, creating {q_die_rolls * 27} different universes')       



if __name__ == '__main__':
    main()