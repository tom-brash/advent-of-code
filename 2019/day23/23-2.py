'''
DAY 23-2: (Intcode) Managing idle Intcode machines

Given the way 23-1 is set up, this is one of the easiest extensions. For each loop
of the machines, we just keep track of whether at least one is doing something, and if
not pass the latest value in the NAC to address 0 and keep the loop going

''' 
import sys
import os
import pprint
from collections import deque
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day23/23-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    starting_memory = [int(x) for x in input_data.split(',')]

    net = Network(50, starting_memory)
    net.run()
    

# network of intcode machines
class Network:
    def __init__(self, n, mem):
        self.nodes = []
        # run each intcode machine with its number as the starting code
        for i in range(n):
            machine = Intcode_computer(mem, input_queue=[i], suppress_notifications=True)
            machine.run()
            self.nodes.append({'machine': machine, 'message_queue': deque()})
        self.nac = None  # current value in the nac
        self.last_nac_y = None  # last nac value sent
    

    def print_network(self):
        pprint.pprint(self.nodes)

    # turn on the network
    def run(self):
        first_y_found = False
        while True:
            network_idle = True  # unless anything is done this round
            for i, node in enumerate(self.nodes):
                machine = node['machine']
                messages = node['message_queue']

                # get the latest input if available (as a x, y pair) otherwise -1
                if len(messages) > 0:
                    machine.add_to_input_queue(messages.popleft(), add_list=True)
                    network_idle = False
                else:
                    machine.add_to_input_queue(-1)
                
                machine.run()
                outputs = machine.output_queue
                if len(outputs) > 0:
                    if outputs[-1] != 'halt':
                        for i in range(len(outputs) // 3):                           
                            target = outputs[i * 3]
                            x = outputs[i * 3 + 1]
                            y = outputs[i * 3 + 2]
                            if target == 255:
                                if not first_y_found:  # print out the answer to part 1 - might as well
                                    print('First value sent to nac: ', y)
                                    first_y_found = True
                                self.nac = [x, y]
                            else:
                                self.post(target, x, y)
                            network_idle = False

                        machine.clear_output_queue()
            
            if network_idle:  # post the nac value to address 0 if network is idle
                self.post(0, self.nac[0], self.nac[1])
                if self.nac[1] == self.last_nac_y:
                    print('First repeated nac y value: ', self.nac[1])
                    return 1
                self.last_nac_y = self.nac[1]
    
    def post(self, target, x, y):
        self.nodes[target]['message_queue'].append([x, y])
            

if __name__ == "__main__":
    main()