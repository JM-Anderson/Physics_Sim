import pyglet
import time

from p_libs.physics.particles import particle_manager
from p_libs.physics.particles import particle_types


class sim:
    def __init__(self, batch):
        self.particle_m = particle_manager(batch)

        # Used to keep track of time between frames
        self.last_time = time.time()
        self.delta_t = 0

        particle = self.particle_m.spawn(10, 10)

        particle.move(100, 300)

        # Add a force in the Y direction equal to mg (gravity)
        particle.force_y += -9.8 * particle.mass

    def click_spawn(self, x, y, settings):
        p = self.particle_m.spawn(x, y, 3)

        if settings['gravity']:
            p.force_y += -9.8 * p.mass
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
