import copy

class Intcode_computer:
    def __init__(self, memory, instruction_pointer=0, relative_base=0, input_queue=None, suppress_notifications=False):
        self.memory = copy.deepcopy(memory)
        self.memory.extend([0] * 5000)
        self.instruction_pointer = instruction_pointer
        self.relative_base = relative_base
        self.input_queue = input_queue
        self.output_queue = []
        self.suppress_notifications=suppress_notifications
        self.status = 'Running'
    

    def add_to_input_queue(self, add_val, add_list=False):
        if add_list == False:
            self.input_queue.append(add_val)
        else:
            for x in add_val:
                self.input_queue.append(x)
    
    def get_last_output(self, exclude_last=False):
        if len(self.output_queue) == 0:
            return ''
        if exclude_last == True:
            return self.output_queue[-2]
        return self.output_queue[-1]

    def pprint(self):
        print_mem = self.memory.copy()
        while print_mem[-1] == 0:
            del print_mem[-1]
        print(print_mem)

    def clear_output_queue(self):
        self.output_queue = []

    def run(self, pause_at_output=False):
        param_dict = {'01': 'rrw', '02': 'rrw', '03': 'w', '04': 'r', '05': 'rr', '06': 'rr', '07': 'rrw', '08': 'rrw', '09': 'r', '99': ''}

        while True:            
            moved = False
            current_opcode, params = self.parse_current()

            # RUN INSTRUCTIONS
            # Param dictionary is used to return values based on parameter mode
            # exceptions are made for instructions that store values, which have different access rules and are done direct
            
            # CHECK VALIDITY
            if current_opcode not in param_dict:
                print('Invalid opcode found:', current_opcode)
                return 1

            # HALT
            elif current_opcode == '99':
                self.output_queue.append('halt')
                self.instruction_pointer += len(param_dict[current_opcode]) + 1
                self.status = 'halt'
                return 0

            # ADD
            elif current_opcode == '01':
                # add numbers located at indices shown by params 0 and 1, and store them in param 3 index
                # param 2 is storage param
                self.memory[params[2]] = params[0] + params[1]
            
            # MULTIPLY
            elif current_opcode == '02':
                # multiply numbers located at indices shown by params 0 and 1, and store them in param 2 index
                # param 2 is storage param
                self.memory[params[2]] = params[0] * params[1]
            
            # INPUT
            elif current_opcode == '03':
                # param 0 is storage param
                if self.input_queue is None:
                    self.memory[params[0]] = int(input('Input: '))
                elif self.input_queue == []:
                    if self.suppress_notifications == False:
                        print('awaiting input')
                    return 0
                else:
                    self.memory[params[0]] = self.input_queue.pop(0)
            
            # OUTPUT
            elif current_opcode == '04':
                self.output_queue.append(params[0])
                # print('Output: ', params[0])
                if pause_at_output == True:
                    self.instruction_pointer += len(param_dict[current_opcode]) + 1
                    return 0
            
            # JUMP IF TRUE
            elif current_opcode == '05':
                if params[0] != 0:
                    self.instruction_pointer = params[1]
                    moved = True
            
            # JUMP IF FALSE
            elif current_opcode == '06':
                if params[0] == 0:
                    self.instruction_pointer = params[1]
                    moved = True
            
            # LESS THAN
            elif current_opcode == '07':
                if params[0] < params[1]:
                    self.memory[params[2]] = 1
                else:
                    self.memory[params[2]] = 0
            
            # EQUALITY
            elif current_opcode == '08':
                if params[0] == params[1]:
                    self.memory[params[2]] = 1
                else:
                    self.memory[params[2]] = 0
            
            # ADJUST RELATIVE BASE
            elif current_opcode == '09':
                self.relative_base += params[0]

            # move instruction pointer
            if not moved:
                self.instruction_pointer += len(param_dict[current_opcode]) + 1
    
    def parse_current(self):
        current_value = str(self.memory[self.instruction_pointer])
        
        # extract opcode from the value at the instruction pointer
        if len(current_value) == 1:
            current_opcode = '0' + current_value
        else:
            current_opcode = current_value[-2:]
        
        # get parameters
        param_dict = {'01': 'rrw', '02': 'rrw', '03': 'w', '04': 'r', '05': 'rr', '06': 'rr', '07': 'rrw', '08': 'rrw', '09': 'r', '99': ''}
        param_types = param_dict[current_opcode]

        num_params = len(param_types)
        param_modes = str(self.memory[self.instruction_pointer])[:-2]
        if len(param_modes) < num_params:
            param_modes = '0' * (num_params - len(param_modes)) + param_modes
        param_modes = param_modes[::-1]

        params = {}
        for i, j in enumerate(param_modes):
            # if parameter is in position mode
            if j == '0':
                if param_types[i] == 'r':
                    params[i] = self.memory[self.memory[self.instruction_pointer + i + 1]]
                elif param_types[i] == 'w':
                    params[i] = self.memory[self.instruction_pointer + i + 1]
            
            # if parameter is in immediate mode
            elif j == '1': 
                params[i] = self.memory[self.instruction_pointer + i + 1]
            
            # if parameter is in relative mode
            elif j == '2':
                if param_types[i] == 'r':
                    params[i] = self.memory[self.relative_base + self.memory[self.instruction_pointer + i + 1]]
                elif param_types[i] == 'w':
                    params[i] = self.relative_base + self.memory[self.instruction_pointer + i + 1]
        
        return current_opcode, params
    

