import pyglet
import time
import math
import numpy as np

from p_libs.physics.particles import particle_manager
from p_libs.physics.particles import particle_types


class sim:
    constants = {
        # Gravity
        'g': -9.8,
        'damping': 1,
        'pixToMeter': 2
    }

    def __init__(self, batch, window):
        # Set up particle manager
        self.particle_m = particle_manager(batch, self)

        # Keep track of window
        self.window = window

        # Used to keep track of time between frames
        self.last_time = time.time()
        self.delta_t = 0

        # Generate starting particles
        self.create_particles()

    def create_particles(self):
        return

    # Spawns a particle at the mouse's current position with the
    # current material settings
    def click_spawn(self, x, y, settings):
        p = self.particle_m.spawn(x, y,
                                  settings['radius'],
                                  particle_types[settings['shape']],
                                  settings['color'])

        p.mass = settings['mass']

        if settings['gravity']:
            p.force_y += self.constants['g'] * p.mass
        return p

    # Width of each grid square
    grid_scale = 6

    # Adds to the main program loop
    # Called every frame
    # After window is cleared - before elements are redrawn
    def loop(self):
        now = time.time()
        self.delta_t = now - self.last_time

        self.last_time = now

        # Reset grid tracker
        particle_pos = {}

        # Loop through each particle
        for particle in self.particle_m.particles:
            # Updates each particles velocity based on forces acting on it
            particle.update(self.delta_t)

            # Move each particle, account for colliding with walls
            distance_y = particle.velocity_y * self.delta_t
            if particle.y + distance_y < particle.r:
                # Time to get to collision
                dt1 = ((particle.r - particle.y) / particle.velocity_y)
                # Time after collision
                dt2 = self.delta_t - dt1

                particle.velocity_y *= -1 * self.constants['damping']
                particle.set_pos(particle.x, dt2 * particle.velocity_y + particle.r)
            else:
                particle.move(particle.velocity_x * self.delta_t,
                              particle.velocity_y * self.delta_t)

            # Calculate collisions between particles
            grid_x = particle.x / self.grid_scale
            grid_y = particle.y / self.grid_scale

            fgrid_x = math.floor(grid_x)
            fgrid_y = math.floor(grid_y)

            # Grid squares that the particle is contained in
            squares = [(fgrid_x, fgrid_y)]

            if grid_x > fgrid_x:
                squares.append((fgrid_x + 1, fgrid_y))
            if grid_y > fgrid_y:
                squares.append((fgrid_x, fgrid_y + 1))
            if len(squares) == 3:
                squares.append((fgrid_x + 1, fgrid_y + 1))

            for square in squares:
                if square in particle_pos:
                    particle_pos[square].append(particle)
                else:
                    particle_pos[square] = [particle]

            self.handle_collision(particle_pos)

    def handle_collision(self, particle_pos):
        # Check if any particles are colliding
        for p_list in particle_pos.values():
            # Check if there are at least 2 particles in the square
            if len(p_list) >= 2:
                res = self.calc_collision(p_list[0], p_list[1])
                if res is None:
                    continue
                else:
                    neg_coll_time = self.calc_coll_time(p_list[0], p_list[1]) * self.delta_t

                    if neg_coll_time == 0:
                        continue
                    else:
                        print(p_list[0].id, p_list[1].id)

                    p_list[0].move(p_list[0].velocity_x * neg_coll_time,
                                   p_list[0].velocity_y * neg_coll_time)
                    p_list[1].move(p_list[1].velocity_x * neg_coll_time,
                                   p_list[1].velocity_y * neg_coll_time)

                    p_list[0].velocity_x = res[0][0]
                    p_list[0].velocity_y = res[0][1]

                    p_list[1].velocity_x = res[1][0]
                    p_list[1].velocity_y = res[1][1]

                    p_list[0].move(p_list[0].velocity_x * neg_coll_time * -1,
                                   p_list[0].velocity_y * neg_coll_time * -1)
                    p_list[1].move(p_list[1].velocity_x * neg_coll_time * -1,
                                   p_list[1].velocity_y * neg_coll_time * -1)

    # This method is not meant for readability
    # It is meant purely for performance
    # No single calculation is performed twice
    @staticmethod
    def calc_collision(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y

        d_sqr = dx ** 2 + dy ** 2

        # Check if particles are overlapping
        are_colliding = (p1.r + p2.r) ** 2 > d_sqr
        if not are_colliding:
            return None

        dvelx = p1.velocity_x - p2.velocity_x
        dvely = p1.velocity_y - p2.velocity_y

        dsum = dx * dvelx + dy * dvely

        denom = d_sqr * (p1.mass + p2.mass)

        c_ans = 2 * dsum / denom

        c_ans1 = c_ans * p1.mass
        vx1 = p1.velocity_x - c_ans1 * dx
        vy1 = p1.velocity_y - c_ans1 * dy

        c_ans2 = c_ans * p2.mass
        vx2 = p2.velocity_x + c_ans2 * dx
        vy2 = p2.velocity_y + c_ans2 * dy

        return [(vx1, vy1), (vx2, vy2)]

    # Calculates the time at which the collision takes place in the frame
    # Stolen shamelessly from https://gamedev.stackexchange.com/questions/62360/small-high-speed-object-collisions-avoiding-tunneling
    @staticmethod
    def calc_coll_time(p1, p2):
        a = p1.x
        b = p1.y

        c = p2.x
        d = p2.y

        w = p1.velocity_x
        x = p2.velocity_x

        y = p1.velocity_y
        z = p2.velocity_y

        r = p1.r
        s = p2.r

        discrim = (2*a*w-2*a*x+2*b*y-2*b*z-2*c*w+2*c*x-2*d*y+2*d*z)**2-4*(w**2-2*w*x+x**2+y**2-2*y*z+z**2)*(a**2-2*a*c+b**2-2*b*d+c**2+d**2-r**2-2*r*s-s*2)
        if discrim <= 0:
            return 0

        t = (-1/2 * math.sqrt(discrim)-a*w+a*x-b*y+b*z+c*w-c*x+d*y-d*z)/(w**2-2*w*x+x**2+y**2-2*y*z+z**2)

        return t
