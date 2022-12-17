import re
from collections import deque, defaultdict

def main():
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    v_exits = {}
    v_rates = {}
    valve_graph = {'AA': {}}

    for x in input:
        vs = re.findall(r'[A-Z][A-Z]', x)
        fr = int(re.search(r'\d+', x).group())
        v_exits[vs[0]] = vs[1:]
        if fr > 0:
            v_rates[vs[0]] = fr
            valve_graph[vs[0]] = {}

    max_rate = sum(v_rates.values())

    for v in valve_graph:
        for target_v in valve_graph:
            if target_v == v:
                continue
            if target_v == "AA":
                continue
            valve_graph[v][target_v] = bfs(v, target_v, v_exits)


    # format: loc, travel_loc, travel_d, e_loc, e_travel_loc, e_travel_d, drained, flowing, t, opened

    start_state = ('AA', 0, 'AA', 0, 0, 0, 0, frozenset())
    sq = deque([start_state])
    best_states = {}
    # ans = 2292
    processed = 0

    iter = 0 

    while sq:
        iter += 1
        if iter % 1000000 == 0:
            print(f'Tested {iter} combinations; length of queue remains {len(sq)}')
        loc, travel_d, e_loc, e_travel_d, drained, flowing, t, opened = sq.popleft()
        if drained + (26 - t) * max_rate <= best_found:
            continue
        if travel_d > 0 and e_travel_d > 0:
             time_skip = min(travel_d, e_travel_d, 26-t)
             travel_d -= time_skip
             e_travel_d -= time_skip
             drained += flowing * time_skip
             t += time_skip
        if flowing == max_rate:
             drained += (26-t) * flowing
             t = 26
        if t == 26:
            if drained > best_found:
                best_found = drained
                print(f'One option found: {drained}')
        current_state = (loc, travel_d, e_loc, e_travel_d, drained, flowing, opened)
        prev_best = best_states.get(current_state, 1000)
        if t >= prev_best:
            continue
        best_states[current_state] = t
        if t < 26:
            sq.extend(get_valid_moves(*current_state, t, valve_graph, v_rates))

    print(f"Final answer: {best_found}")

def bfs(start, target, v_exits):
    sq = deque([(start, 0)])
    best_states = {}

    while sq:
        loc, d = sq.popleft()
        if loc == target:
            return d
        prev_best = best_states.get(loc, 1000)
        if d >= prev_best:
            continue
        best_states[loc] = d

        next_states = [(next_loc, d + 1) for next_loc in v_exits[loc]]
        sq.extend(next_states)


def get_valid_moves(loc, travel_d, e_loc, e_travel_d, drained, flowing, opened, t, valve_graph, v_rates):
    options = []
    me_options = []
    elephant_options = []
    if travel_d == 0:
        if loc not in opened and loc != "AA":
            me_options.append((loc, travel_d, set([loc])))
        else:
            for new_loc in valve_graph[loc]:
                if new_loc in opened:
                    continue
                me_options.append((new_loc, valve_graph[loc][new_loc]-1,  set()))
    else:
        me_options.append((loc, travel_d - 1, set()))

    if e_travel_d == 0:
        if e_loc not in opened and loc != "AA" and not (loc == e_loc and travel_d == 0):
            elephant_options.append((e_loc, e_travel_d, set([e_loc])))
        else:
            for new_loc in valve_graph[e_loc]:
                if new_loc in opened:
                    continue
                elephant_options.append((new_loc, valve_graph[e_loc][new_loc]-1,  set()))
    else:
        elephant_options.append((e_loc, e_travel_d - 1, set()))

    drained = drained + flowing
    for m in me_options:
        for e in elephant_options:
            if e[0] == m[0]:
                if e[1] > m[1]:
                    continue
            new_valves = m[2].union(e[2])
            flow_increase = 0
            if len(new_valves) > 0:
                for v in new_valves:
                    flow_increase += v_rates[v]
                new_opened = set(opened).union( new_valves)
                options.append((m[0], m[1], e[0], e[1], drained, flowing + flow_increase, t+1, frozenset(new_opened)))
            else:
                options.append((m[0], m[1], e[0], e[1], drained, flowing, t+1, opened))
    return options



if __name__ == "__main__":
    main()
