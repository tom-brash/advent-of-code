import re
from collections import defaultdict
from tqdm import tqdm

def main():
    with open('day20/20.txt', 'r') as open_file:
        input_data = open_file.read()
    
    gpu = GPU(input_data)
    gpu.run()


class GPU:
    def __init__(self, input_data):
        self.particles = []
        self.space = {}
        self.tick = 0
        for n, i in enumerate(input_data.split('\n')):
            vals = [int(x) for x in re.findall(r'[\-0-9]+', i)]
            p = Particle(vals, n)
            self.particles.append(p)
            self.space[(p.x, p.y, p.z)] = p.id
    
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
    
    def run(self):
        for i in range(100):
            self.tick += 1
            space = defaultdict(list)
            for x, p in enumerate(self.particles):
                p.step()
                space[(p.x, p.y, p.z)].append(p)
            
            collisions = [v for v in space.values() if len(v) > 1]
            for crashing_particles in collisions:
                print(f'Collision detected at tick {self.tick} with {len(crashing_particles)} particles. Remaining: {len(self.particles) - len(crashing_particles)}')
                crashing_ids = [p.id for p in crashing_particles]
                self.particles = [p for p in self.particles if p.id not in crashing_ids]

            
            self.space = space
            

class Particle:
    def __init__(self, vals, n):
        self.id = n
        self.x = vals[0]
        self.y = vals[1]
        self.z = vals[2]
        self.xv = vals[3]
        self.yv = vals[4]
        self.zv = vals[5]
        self.xa = vals[6]
        self.ya = vals[7]
        self.za = vals[8]
    
    def step(self):
        self.xv += self.xa
        self.yv += self.ya
        self.zv += self.za
        self.x += self.xv
        self.y += self.yv
        self.z += self.zv


if __name__ == '__main__':
    main()