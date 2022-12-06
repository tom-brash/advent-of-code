from itertools import combinations
import re

def main():
    with open('day21/21.txt', 'r') as open_file:
        input_data = open_file.read()
    
    with open('day21/appendix.txt', 'r') as open_file:
        item_shop = open_file.read().split('\n\n')
    
    b_stats = tuple([int(x) for x in re.findall(r'\d+', input_data)])

    # Set up the items store
    weapons = [[int(y) for y in re.findall(r'\d+', x)] for x in item_shop[0].split('\n')[1:]]
    armor = [[int(y) for y in re.findall(r'\d+', x)] for x in item_shop[1].split('\n')[1:]]
    armor.append([0, 0, 0])
    rings = [[int(y) for y in re.findall(r'\d+', x)[1:]] for x in item_shop[2].split('\n')[1:]]
    rings.append([0, 0, 0])
    rings.append([0, 0, 0])

    best = 10000
    for w in range(5):
        for a in range(6):
            for c in list(combinations(range(8), 2)):
                r1 = c[0]
                r2 = c[1]
                cost = weapons[w][0] + armor[a][0] + rings[r1][0] + rings[r2][0]
                hp = 100
                dmg = weapons[w][1] + armor[a][1] + rings[r1][1] + rings[r2][1]
                df = weapons[w][2] + armor[a][2] + rings[r1][2] + rings[r2][2]
                player = Character(hp, dmg, df)
                boss = Character(*b_stats)
                if fight(player, boss) == 'Player':
                    if cost < best:
                        best = cost
    
    print(best)

                

    

def fight(player, boss):
    n = 0
    while True:
        boss.hp -= max(player.dmg - boss.armor, 1)
        if boss.hp <= 0:
            return 'Player'
        player.hp -= max(boss.dmg - player.armor, 1)
        if player.hp <= 0:
            return 'Boss'

class Character:
    def __init__(self, hp, dmg, armor):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
    



if __name__ == '__main__':
    main()