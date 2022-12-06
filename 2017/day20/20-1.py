import re

def main():
    with open('day20/20.txt', 'r') as open_file:
        input_data = open_file.read()
    
    gpu = GPU(input_data)
    gpu.find_straggler()


    
class GPU:
    def __init__(self, input_data):
        self.particles = []
        for i in input_data.split('\n'):
            vals = [int(x) for x in re.findall(r'[\-0-9]+', i)]
            self.particles.append(Particle(vals))
    
    def find_straggler(self):
        straggler = -1
        slowest = 100000
        slowest_vel = 100000
        slowest_pos = 100000
        for x, particle in enumerate(self.particles):
            acc = abs(particle.xa) + abs(particle.ya) + abs(particle.za)
            vel = abs(particle.xv) + abs(particle.yv) + abs(particle.zv)
            pos = abs(particle.x) + abs(particle.y) + abs(particle.z)
            if acc < slowest:
                straggler = x
                slowest = acc
                slowest_vel = vel
                slowest_pos = pos
            elif acc == slowest and vel < slowest_vel:
                straggler = x
                slowest = acc
                slowest_vel = vel
                slowest_pos = pos
            elif acc == slowest and vel == slowest_vel and pos < slowest_pos:
                straggler = x
                slowest = acc
                slowest_vel = vel
                slowest_pos = pos

        print(f'Straggling particle is particle {straggler}')
            


class Particle:
    def __init__(self, vals):
        self.x = vals[0]
        self.y = vals[1]
        self.z = vals[2]
        self.xv = vals[3]
        self.yv = vals[4]
        self.zv = vals[5]
        self.xa = vals[6]
        self.ya = vals[7]
        self.za = vals[8]


if __name__ == '__main__':
    main()