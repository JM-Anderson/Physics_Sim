import pyglet
import time

from p_libs.physics.particles import particle_manager
from p_libs.physics.particles import particle_types


class sim:
    constants = {
        # Gravity
        'g': -9.8,
        'damping': 0.6,
        'pixToMeter': 2
    }

    def __init__(self, batch):
        self.particle_m = particle_manager(batch, self)

        # Used to keep track of time between frames
        self.last_time = time.time()
        self.delta_t = 0

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

        for particle in self.particle_m.particles:
            # Updates each particles velocity based on forces acting on it
            particle.update(self.delta_t)

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
