import pyglet
import time

from p_libs.physics.particles import particle_manager
from p_libs.physics.particles import particle_types


class sim:
    constants = {
        # Gravity
        'g': -9.8,
        'damping': 0.6
    }

    def __init__(self, batch):
        self.particle_m = particle_manager(batch, self)

        # Used to keep track of time between frames
        self.last_time = time.time()
        self.delta_t = 0

        self.create_particles()

    def create_particles(self):
        particle = self.particle_m.spawn(100, 300)

        # Add a force in the Y direction equal to mg (gravity)
        particle.force_y += self.constants['g'] * particle.mass

    def click_spawn(self, x, y, settings):
        p = self.particle_m.spawn(x, y, 3)

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
            particle.update(self.delta_t)
