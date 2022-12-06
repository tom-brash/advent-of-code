from collections import deque

def main():
    with open('day24/24.txt', 'r') as open_file:
        adapters = open_file.read().split('\n')
    
    adapters = [(int(x.split('/')[0]), int(x.split('/')[1])) for x in adapters]

    opening_bridge = [[(0, 0)], 0]
    queue = deque([opening_bridge])
    strongest_bridge = 0
    full_bridge = None
    while len(queue) > 0:
        current_bridge = queue.popleft()
        additions = [x for x in adapters if x not in current_bridge[0] and (x[0] == current_bridge[-1] or x[1] == current_bridge[-1])]
        if len(additions) == 0:
            bridge_power = sum(map(sum, current_bridge[0]))
            if bridge_power > strongest_bridge:
                strongest_bridge = bridge_power
                full_bridge = current_bridge

        for a in additions:
            if a[0] == current_bridge[-1]:
                extension = a[1]
            else:
                extension = a[0]
            new_bridge = [current_bridge[0] + [a], extension]
            queue.append(new_bridge)
    
    print(strongest_bridge)
    print(full_bridge)



if __name__ == '__main__':
    main()