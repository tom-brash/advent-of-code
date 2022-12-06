import re
import pprint

def main():
    with open('day7/7.txt', 'r') as open_file:
        info = open_file.read().split('\n')

    supported_blocks = set()
    all_blocks = {}
    

    for i in info:
        blocks = re.findall(r'[\w]+', i)
        all_blocks[blocks[0]] = {'weight': int(blocks[1]), 'holding': [], 'layer': None, 'total_weight': int(blocks[1])}
        for s in range(2, len(blocks)):
            all_blocks[blocks[0]]['holding'].append(blocks[s])
    
    current_layer = 0
    next_queue = ['gmcrj']
    while len(next_queue) > 0:
        queue = next_queue.copy()
        next_queue = []
        for b in queue:
            all_blocks[b]['layer'] = current_layer
            next_queue.extend(all_blocks[b]['holding'])
        current_layer += 1
    
    w_layer = current_layer - 1
    print(w_layer)

    while w_layer > 1:
        w_layer -= 1
        for block in all_blocks:
            holding = all_blocks[block]['holding']
            if holding == []:
                continue
            if all_blocks[block]['layer'] == w_layer:
                for b in holding:
                    
                    all_blocks[block]['total_weight'] += all_blocks[b]['weight']
        
                

    
    

            

if __name__ == '__main__':
    main()