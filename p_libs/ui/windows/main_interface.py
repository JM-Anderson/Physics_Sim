"""
Draws main interface elements
"""
import pyglet
from pyglet.gl import glClearColor

from pyglet_gui.manager import Manager
from pyglet_gui.gui import PopupMessage

from threading import Timer

from p_libs.ui.elements.sidebar import sidebar
from p_libs.graphics.primitives_2d import prim_creator
from p_libs.physics.sim import sim


class MainWindow(pyglet.window.Window):
    min_x = 700
    min_y = 400

    all_elements = {}

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
        glClearColor(255, 255, 255, 1)

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

        self.all_elements[elem.__class__.__name__] = elem

    def load_graphics(self):
        self.sim = sim(self.batch)

    def on_draw(self):
        self.clear()
        self.sim.loop()
        self.batch.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            settings = self.all_elements['sidebar'].get_settings()
            if settings is None:
                label = pyglet.text.Label('Pick a shape',
                                          x=10, y=10,
                                          batch=self.batch)
                fadeout = Timer(3, lambda: label.delete())
                fadeout.start()
            else:
                self.sim.click_spawn(x, y, settings)

    def on_close(self):
        pyglet.app.exit()
