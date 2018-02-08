import pyglet
import time
import math

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
                                  particle_types[settings['shape']])

        if settings['gravity']:
            p.force_y += self.constants['g'] * p.mass
        return p

    # Adds to the main program loop
    # Called every frame
    # After window is cleared - before elements are redrawn
    def loop(self):
        now = time.time()
        self.delta_t = self.last_time - now
        self.last_time = now

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

            square = (math.floor(particle.x / 2), math.floor(particle.y / 2))
            if square in particle_pos:
                particle_pos[square].append(particle)
            else:
                particle_pos[square] = [particle]

        # Check if any particles are colliding
        for p_list in particle_pos:
            if len(p_list) >= 2:
                dist_sqr = (p_list[0].x - p_list[1].x) ** 2 + (p_list[0].y - p_list[1].y) ** 2
