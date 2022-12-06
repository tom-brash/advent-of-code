import time

def main():
    with open('19/19.txt', 'r') as open_file:
        input_data = open_file.read().split('\n\n')
    
    start_time = time.time()
    
    galaxy = set()
    unattached = []
    jigsaw = []
    tested = set()
    for i, scan in enumerate(input_data):
        unattached.append(Scanner(i, scan.split('\n')[1:]))
    
    # lock in first scanner
    print('Starting... First scanner locked in at (0, 0, 0)')
    first_scanner = unattached.pop(0)
    first_scanner.beacons = first_scanner.beacons[0]
    first_scanner.b_graphs = first_scanner.b_graphs[0]
    first_scanner.locked = True
    first_scanner.loc = (0, 0, 0)
    for b in first_scanner.beacons:
        galaxy.add(tuple(b))
    jigsaw.append(first_scanner)

    # find other scanners
    while len(unattached) > 0:
        for s in jigsaw:
            for n in unattached:
                if frozenset([s.n, n.n]) in tested:
                        continue
                tested.add(frozenset([s.n, n.n]))
                print(f'Testing scanner {s.n} against scanner {n.n}')
                for i in range(24):
                    
                    res = beacon_match(s.b_graphs, n.b_graphs[i])
                    if res != False:
                        n.beacons = n.beacons[i]
                        n.b_graphs = n.b_graphs[i]
                        n.locked = True
                        ref_point_a, ref_point_b = res[1][0]
                        n.loc = tuple([x1 - x2 for x1, x2 in zip(ref_point_a, ref_point_b)])
                        print(f'Location of scanner {n.n} found at location {n.loc}')
                        n.update_to_absolute()
                        unattached.remove(n)
                        jigsaw.append(n)
                        for b in n.beacons:
                            galaxy.add(tuple(b))
                        print(f'Remaining scanners... {len(unattached)}')
                        break
    
    
    print(len(galaxy))
    
    # find largest distance between scanners
    biggest = 0
    scanner_locs = []
    for s in jigsaw:
        scanner_locs.append(s.loc)
    for i, b in enumerate(scanner_locs):
        for j, c in enumerate(scanner_locs):
            if i != j:
                d = manhattan(b, c)
                if d > biggest:
                    biggest = d

    print('Largest distance: ', biggest)
    print(f'Finished in {time.time() - start_time}s')

def beacon_match(g1, g2):
    matching = []
    total = 0
    for b in g1:
        for c in g2:
            if len(set(b[1]).intersection(set(c[1]))) >= 11:
                total += 1
                matching.append((b[0], c[0]))
        if total >= 12:
            return total, matching
    return False

def manhattan(p1, p2):
    t = 0
    for i in range(3):
        t += abs(p1[i] - p2[i])
    return t

class Scanner:
    def __init__(self, n, beacons):
        self.loc = None
        self.n = n
        beacons = [[int(b) for b in x.split(',')] for x in beacons]
        self.beacons = []
        self.locked = False
        for i in range(24):
            self.beacons.append([])
        
        for beacon in beacons:
            beacon = list(self.sequence(beacon))
            for i in range(24):
                self.beacons[i].append(beacon[i])

        self.b_graphs = []
        for b_orientation in self.beacons:
            b_graph = []
            for i, b in enumerate(b_orientation):
                b_edges = []
                for j, c in enumerate(b_orientation):
                    if i != j:
                        edge = tuple([x2 - x1 for x1, x2 in zip(b, c)])
                        b_edges.append(edge)
                b_graph.append([b, b_edges])
            self.b_graphs.append(b_graph)
    
    def update_to_absolute(self):
        if not self.locked:
            print('Can\'t update this yet!! This scanner does not have a location or orientation')
        self.beacons = [[a + b for a, b in zip(self.loc, beacon)] for beacon in self.beacons]
        for i, _ in enumerate(self.b_graphs):
            actual_loc = [a + b for a, b in zip(self.loc, self.b_graphs[i][0])]
            self.b_graphs[i][0] = actual_loc
    
    def roll(self, v): 
        return (v[0],v[2],-v[1])

    def turn(self, v): 
        return (-v[1],v[0],v[2])

    def sequence (self, v):
        for cycle in range(2):
            for step in range(3):  # Yield RTTT 3 times
                v = self.roll(v)
                yield(v)           #    Yield R
                for i in range(3): #    Yield TTT
                    v = self.turn(v)
                    yield(v)
            v = self.roll(self.turn(self.roll(v)))  # Do RTR

                        

if __name__ == '__main__':
    main()