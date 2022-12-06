import re

def main():
    with open('day12/12.txt', 'r') as open_file:
        input_data = open_file.read().split('\n')
    
    progs = {}
    for i in input_data:
        d_list = re.findall(r'\d+', i)
        progs[d_list[0]] = []
        for j in range(1, len(d_list)):
            progs[d_list[0]].append(d_list[j])
        
    queue = ['0']
    visible = set()

    groups = 0
    while len(progs) > 0:
        queue = [next(iter(progs))]
        while len(queue) > 0:
            x = queue.pop(0)   
            visible.add(x)
            new_items = [y for y in progs[x] if y not in visible]
            queue.extend(new_items)
        groups += 1
        progs = {k:v for k, v in progs.items() if k not in visible}
    
    print(groups)
        
        

        

if __name__ == '__main__':
    main()