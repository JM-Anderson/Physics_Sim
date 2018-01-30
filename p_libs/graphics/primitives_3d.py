import pyglet
from pyglet.gl import *


class Primitives:
    @staticmethod
    def cube_batchmode(batch):
        vertex_list = batch.add_indexed(8, GL_TRIANGLE_STRIP, None,
                                        [5, 4, 6, 7, 3, 4, 0,
                                         5, 1, 6, 2, 3, 1, 0],
                                        ('v3i', (50, 50, 50,
                                                 -50, 50, 50,
                                                 -50, -50, 50,
                                                 50, -50, 50,
                                                 50, 50, -50,
                                                 -50, 50, -50,
                                                 -50, -50, -50,
                                                 50, -50, -50)),
                                        ('c3B', (0, 255, 0,
                                                 255, 128, 128,
                                                 0, 0, 255,
                                                 255, 255, 0,
                                                 0, 255, 255,
                                                 255, 0, 255,
                                                 255, 0, 0,
                                                 255, 255, 255)))
