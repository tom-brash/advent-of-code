import re
import heapq
from collections import deque, defaultdict

def main():
    print('\nElephant has agreed to help! Training elephant...')
    print('Elephant trained. Looking for optimal 26 minute route...')
    with open('input', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    v_exits = {}
    v_rates = {}
    valve_graph = {'AA': {}}
    max_time = 30
    heuristic_boundary = 0.75

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


    best_possible = (max_time - 4) * max_rate

    # format: best_possible, loc, travel_d, e_loc, e_travel_d, drained, flowing, t, opened
    start_state = (-best_possible, 'AA', 0, 'AA', 0, 0, 0, 4, frozenset())
    sq = [start_state]
    heapq.heapify(sq)

    best_states = {}
    best_found = 0
    best_time_state = defaultdict(int)  # to allow for heuristic search

    if heuristic_boundary > 0:
        print('\nWARNING: Using heuristic search: not guaranteed to find true optimal value')

    iter = 0 
    while sq:
        iter += 1
        if iter % 1000000 == 0:
            print(f'Tested {iter} different routes! Best found so far: {best_found}. Length of queue is {len(sq)}...')

        # get current state; best_possible is at the start of tuple to allow heapq priority sorting
        _, loc, travel_d, e_loc, e_travel_d, drained, flowing, t, opened = heapq.heappop(sq)

        # fastforward time to relevant decision
        if travel_d > 0 and e_travel_d > 0:
             time_skip = min(travel_d, e_travel_d, max_time-t)
             travel_d -= time_skip
             e_travel_d -= time_skip
             t += time_skip

        # fastforward until max_time if no more valves to open
        if flowing == max_rate:
            t = max_time

        # evaluate score against best found
        if t == max_time:
            if drained > best_found:
                best_found = drained
                # print(f'Best option found so far: {drained}')

        # check if current state has been reached faster
        current_state = (loc, travel_d, e_loc, e_travel_d, drained, flowing, opened)
        prev_best = best_states.get(current_state, 1000)
        if t >= prev_best:
            continue
        best_states[current_state] = t

        # add to loose heuristic dictionary based on only time and drained
        if drained > best_time_state[t]:
            best_time_state[t] = drained

        # add valid moves
        if t < max_time:
            # heuristic check: only add moves if t is low or drained is at least close to the best value at that time
            if t < 12 or drained > 0.75 * best_time_state[t]: 
                new_moves = get_valid_moves(*current_state, t, valve_graph, v_rates, max_rate, best_found, max_time)
                for move in new_moves:
                    heapq.heappush(sq, move)

    print(f"\n(16-2) Best possible route can release pressure of: {best_found}")

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

def get_valid_moves(loc, travel_d, e_loc, e_travel_d, drained, flowing, opened, t, valve_graph, v_rates, max_rate, best_found, max_time):
    options = []
    me_options = []
    elephant_options = []

    # add my own moves
    if travel_d == 0:
        # it will never be optimal to travel to a node and not open the valve...
        if loc not in opened and loc != "AA":
            me_options.append((loc, travel_d, set([loc])))

        # if valve already open, add next paths
        else:
            for new_loc in valve_graph[loc]:
                if new_loc in opened:
                    continue
                me_options.append((new_loc, valve_graph[loc][new_loc]-1,  set()))
    # if still travelling to a node...
    else:
        me_options.append((loc, travel_d - 1, set()))

    # add elephant moves
    if e_travel_d == 0:
        # do not open valve if other player is at the same location
        if e_loc not in opened and loc != "AA" and not (loc == e_loc and travel_d == 0):
            elephant_options.append((e_loc, e_travel_d, set([e_loc])))
        else:
            for new_loc in valve_graph[e_loc]:
                if new_loc in opened:
                    continue
                elephant_options.append((new_loc, valve_graph[e_loc][new_loc]-1,  set()))
    else:
        elephant_options.append((e_loc, e_travel_d - 1, set()))

    # for a cross-join of both players moves...
    for m in me_options:
        for e in elephant_options:
            # do not need to check if both players are heading to the same node
            if e[0] == m[0]:
                if e[1] > m[1]:
                    continue

            # check if new valves are being opened
            new_valves = m[2].union(e[2])
            flow_increase = 0
            if len(new_valves) > 0:
                for v in new_valves:
                    flow_increase += v_rates[v]
                new_opened = set(opened).union( new_valves)

                # check if this is still feasibly able to be the best solution
                best_possible = drained + (flow_increase * (max_time-t-1)) + (max_rate - flowing - flow_increase) * (max_time-t-1)
                if best_possible <= best_found:
                    continue

                # append new state, giving full credit to future flows
                options.append((-best_possible, m[0], m[1], e[0], e[1], drained + (flow_increase * (max_time-t-1)), flowing + flow_increase, t+1, frozenset(new_opened)))
            else:
                best_possible = (drained + (max_rate - flowing) * (max_time-t-1))
                if best_possible <= best_found:
                    continue
                options.append((-best_possible, m[0], m[1], e[0], e[1], drained, flowing, t+1, opened))
    return options


if __name__ == "__main__":
    main()
