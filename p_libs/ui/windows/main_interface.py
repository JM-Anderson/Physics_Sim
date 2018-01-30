"""
Draws main interface elements
"""
import pyglet
from pyglet_gui.manager import Manager

from p_libs.ui.elements.sidebar import sidebar

from p_libs.graphics.primitives_2d import square

from pyglet.gl import GL_QUADS


class MainWindow(pyglet.window.Window):
    min_x = 700
    min_y = 400

    @staticmethod
    def load_window(x, y, title='Physics Sim'):
        window = MainWindow(x, y, title)
        return window

    def __init__(self, x, y, title):
        # Set up window
        super(MainWindow, self).__init__(x, y,
                                         title,
                                         resizable=True)
        self.set_minimum_size(self.min_x, self.min_y)

        # Set up UI and graphics
        self.batch = pyglet.graphics.Batch()

        # Load elements
        self.load_elements(sidebar)

        # Load graphics
        self.load_graphics()

    def load_elements(self, *elems):
        for elem in elems:
            self.load_elem(elem())

    def load_elem(self, elem):
        Manager(elem.viewer(),
                window=self,
                batch=self.batch,
                **elem.manager_settings())

    def load_graphics(self):
        v_list = self.batch.add(4, GL_QUADS, None, 'v2f', 'c3B')
        square(v_list, 10, 10, 2)

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def on_close(self):
        pyglet.app.exit()
