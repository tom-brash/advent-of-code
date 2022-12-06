import re
from collections import deque
import copy

def main():
    with open('day22/22.txt', 'r') as open_file:
        input_data = open_file.read()

    b_stats = [int(x) for x in re.findall(r'\d+', input_data)]
    player = CharacterState(50, 500, b_stats[0], b_stats[1])
    battlefield = Battlefield(player)
    battlefield.find_best_action()

class Battlefield:
    def __init__(self, player):
        self.player = player
        self.m_values = {0: 53, 1: 73, 2: 113, 3: 173, 4: 229}
    
    def find_best_action(self):
        sq = deque()
        sq.append((copy.deepcopy(self.player), 0)) # format (player,  mana spent)
        best = 1000000
        best_found = {}
        while sq:
            player, m = sq.popleft()
            if player.boss_alive == False:
                if m < best:
                    best = m
                    print(f'Boss defeated using {m} mana')
                continue
            if m > best:
                continue
            sr = str(player)
            best_achieved = best_found.get(sr, 1000000)
            if m >= best_achieved:
                continue
            best_found[sr] = m
            sq.extend(self.get_next_states(player, m))

    
    def get_next_states(self, player, m):
        next_moves = []
        for i in range(5):
            next_player_state = copy.deepcopy(player)
            next_player_state.take_turn(i)
            if next_player_state.player_alive == True:
                next_moves.append((next_player_state, m + self.m_values[i]))
        return next_moves

    

class CharacterState:
    def __init__(self, hp, mp, b_hp, b_dmg):
        self.hp = hp
        self.mp = mp
        self.b_hp = b_hp
        self.b_dmg = b_dmg
        self.shield = 0
        self.poison = 0
        self.recharge = 0
        self.m_values = {0: 53, 1: 73, 2: 113, 3: 173, 4: 229}
        self.min_cost = 53
        self.player_alive = True
        self.boss_alive = True
    
    def __str__(self):
        return '\,'.join([str(x) for x in [self.b_hp, self.shield, self.poison, self.recharge, self.hp, self.mp]])
    
    def take_turn(self, selection):
        # player turn
        self.hp -= 1
        
        if self.poison > 0:
            self.poison -= 1
            self.b_hp -= 3
            if self.b_hp <= 0:
                self.boss_alive = False
                return
        if self.recharge > 0:
            self.mp += 101
            self.recharge -= 1
        if self.shield > 0:
            self.shield -= 1
        if self.mp < self.min_cost:
            self.player_alive = False

        self.mp -= self.m_values[selection]
        
        if selection == 0:
            self.b_hp -= 4
        elif selection == 1:
            self.b_hp -= 2
            self.hp += 2
        elif selection == 2:
            self.shield += 6
            if self.shield > 6:
                self.player_alive = False
        elif selection == 3:
            self.poison += 6
            if self.poison > 6:
                self.player_alive = False
        elif selection == 4:
            self.recharge += 5
            if self.recharge > 5:
                self.player_alive = False
        
        if self.b_hp <= 0:
                self.boss_alive = False
                return

        # boss turn
        d = 0
        if self.shield > 0:
            d = 7
        if self.shield > 0:
            self.shield -= 1
        if self.poison > 0:
            self.poison -= 1
            self.b_hp -= 3
            if self.b_hp <= 0:
                self.boss_alive = False
                return

        if self.recharge > 0:
            self.mp += 101
            self.recharge -= 1
        
        
        self.hp -= max(self.b_dmg - d, 1)
        if self.hp <= 0:
            self.player_alive = False
        
        

if __name__ == '__main__':
    main()