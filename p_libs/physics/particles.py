import pyglet
from enum import Enum

from p_libs.graphics.primitives_2d import prim_creator, primitive


class particle_types(Enum):
    square = 0
    circle = 1


class particle:
    def __init__(self, prim_creator, sim, x, y, r, p_type):
        if p_type == particle_types.square:
            self.prim = prim_creator.square(x, y, r)
        elif p_type == particle_types.circle:
            self.prim = prim_creator.circle(x, y, r)

        self.constants = sim.constants

        # Graphical properties
        self.size = r
        self.type = p_type

        # Physics properties
        self.mass = 100
        self.damping = 1

        # Current forces acting on the particle
        self.force_x = 0
        self.force_y = 0

        # Current movement
        self.velocity_x = 0
        self.velocity_y = 0
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y
        self.prim.move(x, y)

    def update(self, dt):
        if self.y > self.size:
            self.move(self.velocity_x * dt, self.velocity_y * dt)
        else:
            self.force_y = 0

        # Calculate and apply acceleration
        self.velocity_x += (self.force_x / self.mass) * dt
        self.velocity_y += (self.force_y / self.mass) * dt


class particle_manager:
    particles = []

    def __init__(self, batch, sim):
        self.prim_creator = prim_creator(batch)
        self.sim = sim

    def spawn(self, x, y, r=5, p_type=particle_types.square):
        p = particle(self.prim_creator, self.sim, x, y, r, p_type)

        self.particles.append(p)

        return p
