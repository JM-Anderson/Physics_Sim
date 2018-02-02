import pyglet

from p_libs.graphics.primitives_2d import prim_creator


class sim:
    def __init__(self, batch):
        self.prim_creator = prim_creator(batch)

        self.prim_creator.square(100, 100, 50, [128, 128, 255])
