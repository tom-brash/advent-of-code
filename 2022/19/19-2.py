import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    blueprints = []
    for x in input[:3]:
        nums = [int(x) for x in re.findall(r'\d+', x)]
        blueprints.append(Blueprint(nums[1:]))

    total = 1
    
    for i, b in enumerate(blueprints):
        print()
        print(f"Trying blueprint {i}")
        n = find_max_geodes(b)
        total *= n
        
    print(f'Final answer: {total}')

def find_max_geodes(blueprint):
    start = (1, 0, 0, 0, 1, 0, 0, 0, 1)
    sq = deque([start])
    best_found = 0
    best_states = {}
    best_g_at_t = defaultdict(int)
    while sq:
        a, b, c, d, ar, br, cr, dr, t = sq.popleft()
        if d > best_found:
            best_found = d
            print(f'A solution found: {d}')
        current_state = (a, b, c, d, ar, br, cr, dr)
        best_previous = best_states.get(current_state, 35)
        
        best_at_t = best_g_at_t[t]
        if t >= 28 and d <= 0.6 * best_at_t:
            continue
        
        if d > best_at_t:
            best_g_at_t[t] = d

        if t >= best_previous:
            continue
        best_states[current_state] = t
        sq.extend(get_valid_moves(blueprint, *current_state, t))
    print("Best found for blueprint: ", best_found)
    return best_found

def get_valid_moves(blueprint, a, b, c, d, ar, br, cr, dr, t):
    options = []
    current_state = (a, b, c, d, ar, br, cr, dr)
    # buy geode
    if cr > 0:
        options.append(save_up(*current_state, t, blueprint.geode[0], 0, blueprint.geode[1], "geode"))
    # buy obsidian
    if br > 0:
        options.append(save_up(*current_state, t, blueprint.obsidian[0], blueprint.obsidian[1], 0, "obsidian"))
    options.append(save_up(*current_state, t, blueprint.ore, 0, 0, "ore"))
    options.append(save_up(*current_state, t, blueprint.clay, 0, 0, "clay"))
    
    options = [o for o in options if o[-1] <=31]

    return options

def save_up(a, b, c, d, ar, br, cr, dr, t, o_cost, c_cost, ob_cost, purchase):
    while a < o_cost or b < c_cost or c < ob_cost:
        a += ar
        b += br
        c += cr
        t += 1

    # execute build turn
    a -= o_cost
    b -= c_cost
    c -= ob_cost
    a += ar
    b += br
    c += cr
    if purchase == "geode":
        dr += 1
        d += 31 - t
    elif purchase == "obsidian":
        cr += 1
    elif purchase == "clay":
        br += 1
    elif purchase == "ore":
        ar += 1
    
    t += 1
    
    return (a, b, c, d, ar, br, cr, dr, t)

class Blueprint:
    def __init__(self, nums):
        self.ore = nums[0]
        self.clay = nums[1]
        self.obsidian = (nums[2], nums[3])
        self.geode = (nums[4], nums[5])

if __name__ == "__main__":
    main()
