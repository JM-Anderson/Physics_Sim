import pyglet

from p_libs.physics.particles import particle_manager


class sim:
    def __init__(self, batch):
        self.particle_m = particle_manager(batch)

        particle = self.particle_m.spawn(10, 10)

        particle.move(100, 300)

    # Adds to the main program loop
    # Called every frame
    # After window is cleared - before elements are redrawn
    def loop(self):
        return
