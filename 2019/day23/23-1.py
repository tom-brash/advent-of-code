'''
DAY 23-1: (Intcode) Sending packets around Intcode machines 

This is another intcode processing machine, and requires a lot of machines working 'at once'.
As I already set up the intcode machine to pause on input requirement, we can handle this fairly
simply using a loop, without requiring async processes.

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
    
    # print out the network
    def print_network(self):
        pprint.pprint(self.nodes)

    # turn on the network
    def run(self):
        while True:
            for i, node in enumerate(self.nodes):
                machine = node['machine']
                messages = node['message_queue']

                # get the latest input if available (as a x, y pair) otherwise -1
                if len(messages) > 0:
                    machine.add_to_input_queue(messages.popleft(), add_list=True)
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
                                print('First packet to 255 has y value: ', y)
                                return 1
                            self.post(target, x, y)

                        machine.clear_output_queue()
    
    # send message to another queue
    def post(self, target, x, y):
        self.nodes[target]['message_queue'].append([x, y])
            

if __name__ == "__main__":
    main()