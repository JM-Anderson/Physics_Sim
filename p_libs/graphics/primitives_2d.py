from pyglet.graphics import vertex_list
from pyglet.gl import GL_QUADS, GL_TRIANGLE_FAN
from math import sin, cos, pi


def gen_square(x, y, r):
        v_list = [
            x-r, y-r,
            x+r, y-r,
            x+r, y+r,
            x-r, y+r
        ]
        return v_list


class primitive:
    def __init__(self, v_list, x, y, r, gl_type):
        self.gl_type = gl_type
        self.v_list = v_list
        self.x = x
        self.y = y
        self.r = r

    def move(self, x, y):
        self.x += x
        self.y += y

        # Even vertices are x values, odds are y values
        for i in range(len(self.v_list.vertices)):
            if i % 2:
                self.v_list.vertices[i] += y
            else:
                self.v_list.vertices[i] += x

    def set_pos(self, x, y):
        self.x = x
        self.y = y

        self.v_list.vertices = gen_square(x, y, r)


class prim_creator:
    def __init__(self, batch):
        self.batch = batch

    def square(self, x, y, r, color=[255, 0, 0]):
        v_list = self.batch.add(4, GL_QUADS, None, 'v2f', 'c3B')

        v_list.vertices = gen_square(x, y, r)

        v_list.colors = multiply_arr(color, 4)

        return primitive(v_list, x, y, r, GL_QUADS)

    def circle(self, x, y, r, color=[255, 0, 0]):
        n = 32

        v_list = self.batch.add(n+2, GL_TRIANGLE_FAN, None, 'v2f', 'c3B')
        v_list.vertices = draw_circle(x, y, r, n)
        v_list.colors = multiply_arr(color, n+2)
        return primitive(v_list, x, y, r, GL_TRIANGLE_FAN)


def multiply_arr(arr, x):
    out = []
    for i in range(x):
        out.extend(arr)
    return out


def draw_circle(x, y, r, n):
    verts = [x, y]

    interval = (2*pi) / n
    for i in range(n+1):
        verts.append(x + cos(i * interval) * r)
        verts.append(y + sin(i * interval) * r)

    return verts
