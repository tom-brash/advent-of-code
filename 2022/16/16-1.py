import re
import heapq
from collections import deque, defaultdict

def main():
    with open('test', 'r') as open_file:
        input = open_file.read().strip().split('\n')

    v_exits = {}
    v_rates = {}
    valve_graph = {'AA': {}}
    max_time = 30
    heuristic_boundary = 0.7

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


    best_possible = (max_time-1) * max_rate

    # format: best_possible, loc, drained, flowing, t, opened
    start_state = (-best_possible, 'AA', 0, 0, 0, frozenset())
    sq = [start_state]
    heapq.heapify(sq)

    best_states = {}
    best_found = 0
    best_time_state = defaultdict(int)  # to allow for heuristic search

    print('Starting search for optimal routes...')
    if heuristic_boundary > 0:
        print('WARNING: Using heuristic search: not guaranteed to find true optimal value')
        print()

    iter = 0 
    while sq:
        iter += 1
        if iter % 1000000 == 0:
            print(f'Tested {iter} different routes! Length of queue is {len(sq)}...')

        # get current state; best_possible is at the start of tuple to allow heapq priority sorting
        _, loc, drained, flowing, t, opened = heapq.heappop(sq)

        # fastforward until max_time if no more valves to open
        if flowing == max_rate:
            t = max_time

        # evaluate score against best found
        if t == max_time:
            if drained > best_found:
                best_found = drained
                print(f'Best option found so far: {drained}')

        # check if current state has been reached faster
        current_state = (loc, drained, opened)
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
            if t < 12 or drained > heuristic_boundary * best_time_state[t]: 
                new_moves = get_valid_moves(loc, drained, flowing, opened, t, valve_graph, v_rates, max_rate, best_found, max_time)
                for move in new_moves:
                    heapq.heappush(sq, move)

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

def get_valid_moves(loc, drained, flowing, opened, t, valve_graph, v_rates, max_rate, best_found, max_time):
    options = []
    
    for new_loc in valve_graph[loc]:
        if new_loc in opened and new_loc != 'AA':
            continue

        flow_increase = v_rates[new_loc]
        time_taken = valve_graph[loc][new_loc] + 1
        new_opened = set(opened)
        new_opened.add(new_loc)

        best_possible = drained + (max_time - t - time_taken) * flow_increase + (max_time - t - time_taken) * max_rate
        if best_possible <= best_found:
            continue
        options.append((best_possible, new_loc, drained + (max_time - t - time_taken) * flow_increase, flowing + flow_increase, t + time_taken, frozenset(new_opened)))
    return options


if __name__ == "__main__":
    main()
