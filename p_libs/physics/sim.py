import pyglet
import time
import math

from itertools import combinations

from p_libs.physics.particles import particle_manager
from p_libs.physics.particles import particle_types

from p_libs.physics.utils import calc_coll_time, calc_exit_vels

from p_libs.physics.collisions import collision_stack

from p_libs.physics.organization import uniform_grid


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

        self.batch = batch

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
        p.velocity_x = settings['vel_x']
        p.velocity_y = settings['vel_y']

        if settings['gravity']:
            p.force_y += self.constants['g'] * p.mass
        return p

    # Width of each grid square
    grid_scale = 6
    framerate = True

    # Adds to the main program loop
    # Called every frame
    # After window is cleared - before elements are redrawn
    def loop(self):
        now = time.time()
        self.delta_t = now - self.last_time
        self.last_time = now

        # Display framerate and period
        if self.framerate:
            out = str(1 / self.delta_t)[:2] + ', ' + str(self.delta_t)[:4]
            txt = pyglet.text.Label(out,
                                    font_name='Times New Roman',
                                    font_size=10,
                                    color=(0, 0, 0, 255),
                                    x=20, y=self.window.height - 20)
            txt.draw()

        org = uniform_grid(self.particle_m.particles)
        org.organize()

        coll_stack = collision_stack(org.organized.values(), self.delta_t)
        coll_stack.resolve_all()

        for particle in self.particle_m.particles:
            # Move particle normally if it wasn't in a collision
            if not particle.in_collision:
                time_left = self.handle_wall_coll('y',
                                                  self.delta_t,
                                                  particle,
                                                  0, self.window.height)
                time_left = self.handle_wall_coll('x',
                                                  time_left,
                                                  particle,
                                                  0, self.window.width)

                particle.p_move(time_left)

            # Update particle velocity based on forces
            particle.update(self.delta_t)

            # Reset particle collision status
            particle.in_collision = False

    @staticmethod
    def handle_wall_coll(axis, dt, particle, min_pos, max_pos):
        if axis == 'x':
            pos = particle.x
            vel = particle.velocity_x
        elif axis == 'y':
            pos = particle.y
            vel = particle.velocity_y
        else:
            return None

        if vel == 0:
            return dt

        if pos + vel * dt - particle.r <= min_pos:
            # Calculate time till collision
            coll_time = (particle.r + min_pos - pos) / vel

        elif pos + vel * dt + particle.r >= max_pos:
            # Calculate time till collision
            coll_time = (max_pos - particle.r - pos) / vel

        else:
            coll_time = None

        if coll_time is not None:
            # Move particle to collision
            particle.p_move(coll_time)

            if axis == 'x':
                # Reverse x velocity
                particle.velocity_x *= -1
            if axis == 'y':
                # Reverse y velocity
                particle.velocity_y *= -1

            dt -= coll_time

        return dt
