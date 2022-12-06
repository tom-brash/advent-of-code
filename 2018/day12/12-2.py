'''
Day 12-2: Tracking life in pots after 50,000,000,000 epochs

Here there isn't really a way to process the epochs 50b times in the same way as the 20 epochs.

By observation, however, the pattern stabilizes after ~100 epochs, and then just starts moving 
to the right (kind of like a Conway glider). This means that our answer (value of the pots containing
life) just goes up by a fixed number (in this case 40) every epoch. 

We could do this slightly more programatically by keeping track of the differences, but given that this
was largely solved by observation the value 40 is hardcoded.
'''

def main():
    with open('day12/12-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    input_data = input_data.split('\n\n')
    initial_state = input_data[0].split(': ')[1]
    rule_data = input_data[1].split('\n')

    state = {}
    rules = {}

    for rule in rule_data:
        rule = rule.split(' => ')
        rules[rule[0]] = rule[1]
    
    for i, c in enumerate(initial_state):
        state[i] = c
    
    for i in range(100):  # stabilize the system (get out of the early chaos)
        state = step(state, rules)
    
    s = sum([k for k, v in state.items() if v == '#'])  # get the sum after 100 epochs (observed to be stable)
    print((50000000000 - 100) * 40 + s)  # every epoch the value goes up by 40 after stabilizing (by observation)


def step(state, rules):
    l_bound = min(state.keys()) - 2
    r_bound = max(state.keys()) + 2
    next_state = {}
    for i in range(l_bound, r_bound + 1):
        x = ''
        for j in range(-2, 3):
            x += state.get(i + j, '.')
        next_state[i] = rules[x]
    
    return next_state


if __name__ == '__main__':
    main()