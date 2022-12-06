import re

def main():
    with open('day22/22.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')[2:]

    nodes = {}
    for i in input_data:
        nums = [int(x) for x in re.findall(r'\d+', i)]
        nodes[(nums[0], nums[1])] = (nums[3], nums[4])
    
    cluster = MemoryCluster(nodes)
    cluster.get_viable_pairs()

class MemoryCluster:
    def __init__(self, node_data):
        self.nodes = node_data
        self.viable_pairs = set()

    def get_viable_pairs(self):
        for loc, node in self.nodes.items():
            data_size = node[0]
            if data_size > 0:
                possible = [x for x in self.nodes.keys() if x != loc]
                for a in possible:
                    if self.nodes[a][1] >= data_size:
                        self.viable_pairs.add((loc, a))
        print(f'Total number of viable pairs: {len(self.viable_pairs)}')


if __name__ == '__main__':
    main()
