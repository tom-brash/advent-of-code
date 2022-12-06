'''
Day 24-2: Evaluating a handicapped battle

The part 1 scaffolding is enough to get this done. We do need to put in place stalemate protection
(since hp damage less than a full unit is ignored and immunities exist, some states will end in a 
draw) - but otherwise we can just run the previous code for every possible boost value (incrementing by 1)
until we get to the answer. Better search strategies (even a binary search would help) would speed things
up, but the answer is low enough that it is interesting to watch how the scores change with the boost level
'''

import re

def main():
    with open('day24/24-1-input.txt', 'r') as open_file:
        input_data = open_file.read().split('\n\n')
    
    immune_data = input_data[0].split('\n')[1:]
    infection_data = input_data[1].split('\n')[1:]

    
    immune_win = False
    boost = 0
    
    while immune_win == False:
        battle = Battlefield(immune_data, infection_data, boost)
        while battle.state == 'active':
            battle.run_round()
        if battle.winner == 'immune':
            immune_win = True
        else:
            boost += 1

class Battlefield:
    def __init__(self, immune_data, infection_data, boost=0):
        self.armies = []
        self.state = 'active'
        self.boost = boost
        self.steps = 0
        self.last_hp_total = 0
        for i, d in enumerate(immune_data):
            self.armies.append(BattleGroup('immune', d, i + 1, boost))
        for i, d in enumerate(infection_data):
            self.armies.append(BattleGroup('infection', d, i + 1))

    def run_round(self):
        # if self.steps > 5000:
        #     print('hi')
        self.select_targets()
        self.attack_targets()
        self.steps += 1
        self.cleanup_step()

    def select_targets(self):
        self.armies.sort(key=lambda a: (a.power, a.initiative), reverse=True)
        for army in self.armies:
            possible_targets = [a for a in self.armies if a.team != army.team and a.attacker == None]
            best_dmg = 1
            best_effective_power = -1
            best_init = -1
            for t in possible_targets:
                pos_dmg = t.determine_damage(army.power, army.attack_type)
                if pos_dmg > best_dmg:
                    best_dmg = pos_dmg
                    best_effective_power = t.power
                    best_init = t.initiative
                    army.target = t                
                elif pos_dmg == best_dmg:
                    if t.power > best_effective_power:
                        army.target = t
                        best_effective_power = t.power
                        best_init = t.initiative
                    elif t.power == best_effective_power:
                        if t.initiative > best_init:
                            best_init = t.initiative
                            army.target = t
            if army.target != None:
                army.target.attacker = army
    
    def attack_targets(self):
        self.armies.sort(key=lambda a: a.initiative, reverse=True)
        for army in self.armies:
            if army.target != None and army.status == 'active':                
                target = army.target
                army.power = army.damage * army.units
                target.receive_damage(army.power, army.attack_type, army)
                
    
    def cleanup_step(self):
        self.armies = [a for a in self.armies if a.status == 'active' ]
        for army in self.armies:
            army.attacker = None
            army.target = None
            army.power = army.damage * army.units
        immune_armies = [a for a in self.armies if a.team == 'immune' ]
        infection_armies = [a for a in self.armies if a.team == 'infection' ]
        hp_remaining = sum([a.hp * a.units for a in self.armies if a.status == 'active'])
        if hp_remaining == self.last_hp_total:
            self.state = 'finished'
            self.winner = 'stalemate'
            print(f'No winner of the round with a boost of {self.boost}. Stalemate reached after {self.steps} steps')
        elif len(immune_armies) == 0:
            self.state = 'finished'
            self.winner = 'infection'
            self.trigger_scoring()
        elif len(infection_armies) == 0:
            self.state = 'finished'
            self.winner = 'immune'
            self.trigger_scoring()
        self.last_hp_total = hp_remaining
    
    def trigger_scoring(self):
        score = sum([a.units for a in self.armies if a.status == 'active' ])
        print(f'Winner of the round with boost of {self.boost} is team {self.winner} with a score of: {score}. Battle took {self.steps} steps')
        #print('Winning score:', score)


class BattleGroup:
    def __init__(self, team, data, i, boost=0):
        self.number = i
        self.team = team
        self.status = 'active'
        self.attacker = None
        self.target = None
        vals = list(map(int, re.findall(r'\-?\d+', data)))
        self.units = vals[0]
        self.hp = vals[1]
        self.damage = vals[2] + boost
        self.initiative = vals[3]
        self.power = self.damage * self.units
        self.attack_type = re.search(r'([a-z]+)\ damage', data).group(1)
        self.immunities = []
        self.weaknesses = []

        if 'immune' in data:
            re_i = re.search(r'immune to ([a-z]+)(?:\, ([a-z]+))?', data)
            self.immunities.append(re_i.group(1))
            if re_i.group(2) != None:
                self.immunities.append(re_i.group(2))
        if 'weak' in data:
            re_w = re.search(r'weak to ([a-z]+)(?:\, ([a-z]+))?', data)
            self.weaknesses.append(re_w.group(1))
            if re_w.group(2) != None:
                self.weaknesses.append(re_w.group(2))
    
    def determine_damage(self, damage, d_type):
        if d_type in self.immunities:
            return 0
        if d_type in self.weaknesses:
            return damage * 2
        return damage
    
    def receive_damage(self, damage, d_type, attacker):
        if d_type in self.immunities:
            damage = 0
        if d_type in self.weaknesses:
            damage *= 2
        self.units -= damage // self.hp
        if self.units <= 0:
            self.status = 'defeated'
        
        #print(f'{attacker.team} group {attacker.number} attacks {self.team} group {self.number} for {damage} damage, killing {damage // self.hp} units')
        

if __name__ == '__main__':
    main()
