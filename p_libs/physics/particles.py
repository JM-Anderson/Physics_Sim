import pyglet

from enum import Enum

from p_libs.graphics.primitives_2d import prim_creator


class particle_types(Enum):
    square = 0


class particle:
    def __init__(self, v_list, x, y, p_type):
        self.v_list = v_list
        self.x = x
        self.y = y
        self.type = p_type

    def move(self, x, y):
        self.x += x
        self.y += y

        # Even vertices are x values, odds are y values
        for i in range(len(self.v_list.vertices)):
            if i % 2:
                self.v_list.vertices[i] += y
            else:
                self.v_list.vertices[i] += x

        return


class particle_manager:
    particles = []

    def __init__(self, batch):
        self.prim_creator = prim_creator(batch)

    def spawn(self, x, y, p_type=particle_types.square):
        p = particle(self.prim_creator.square(x, y, 5),
                     x, y,
                     p_type)

        self.particles.append(p)

        return p
