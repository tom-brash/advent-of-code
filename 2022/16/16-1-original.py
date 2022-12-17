import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    v_exits = {}
    v_rates = {}
    for x in input:
        vs = re.findall(r'[A-Z][A-Z]', x)
        fr = re.search(r'\d+', x)
        v_exits[vs[0]] = vs[1:]
        v_rates[vs[0]] = int(fr.group())

    print(v_rates)

    sq = deque([(0, 0, 0, 'AA', frozenset())])

    best = 0
    previous_bests = {}
    longest = 0

    while sq:
        drained, flowing, t, loc, opened = sq.popleft()
        if t > longest:
            print(f'Checking path of length {t}')
            longest = t
        if t == 30:
            if drained > best:
                best = drained
                print(f'One option found: {drained}')
        prev_best = previous_bests.get((loc, drained, opened), 1000)
        if t >= prev_best:
            continue
        previous_bests[(loc, drained, opened)] = t
        if t < 30:
            sq.extend(get_valid_moves(drained, flowing, t, loc, opened, v_rates, v_exits))
    print(f'Final answer: {best}')

def get_valid_moves(drained, flowing, t, loc, opened, v_rates, v_exits):
    options = []
    if v_rates[loc] > 0 and loc not in opened:
        new_opened = set(opened)
        new_opened.add(loc)
        options.append((drained + flowing, flowing + v_rates[loc], t + 1, loc, frozenset(new_opened)))
    for next_loc in v_exits[loc]:
        options.append((drained + flowing, flowing, t + 1, next_loc, opened))
    return options


if __name__ == "__main__":
    main()
