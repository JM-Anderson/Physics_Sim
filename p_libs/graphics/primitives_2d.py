from pyglet.graphics import vertex_list
from pyglet.gl import GL_QUADS


class prim_creator:
    def __init__(self, batch):
        self.batch = batch

    def square(self, x, y, r, color=[255, 0, 0]):
        v_list = self.batch.add(4, GL_QUADS, None, 'v2f', 'c3B')

        v_list.vertices = [x-r, y-r,
                           x+r, y-r,
                           x+r, y+r,
                           x-r, y+r]

        v_list.colors = multiply_arr(color, 4)
        return v_list


def multiply_arr(arr, x):
    out = []
    for i in range(x):
        out.extend(arr)
    return out
