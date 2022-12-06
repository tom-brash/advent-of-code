'''
Day 12-1: Tracking life in pots after 20 epochs

Here the rules are fairly straightforward to apply - we have a comprehensive set which
we can store as a dictionary.

There is a minor inefficiency here in that we do not 'compress' the state that we care about,
always extending it by 2 pots at every epoch. For 20 epochs though, this makes a trivial impact.
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
    
    for i in range(20):
        state = step(state, rules)
    
    s = sum([k for k, v in state.items() if v == '#'])
    print('Sum of pots with life after 20 epochs:', s)


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