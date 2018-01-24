"""
Draws main interface elements
"""
import pyglet

from pyglet_gui.buttons import Button
from pyglet_gui.gui import Label
from pyglet_gui.manager import Manager
from pyglet_gui.theme import Theme
from pyglet_gui.containers import HorizontalContainer, VerticalContainer, GridContainer

import os
import json

import p_libs.material_display

CWD = os.getcwd()


class MainWindow(pyglet.window.Window):
    min_x = 700
    min_y = 400

    def __init__(self, x, y, title):
        super(MainWindow, self).__init__(x, y,
                                         title,
                                         resizable=True)
        self.set_minimum_size(self.min_x, self.min_y)

        self.batch = pyglet.graphics.Batch()
        self.load_theme()
        self.load_elements()

    @staticmethod
    def load_window(x, y, title='Physics Sim'):
        window = MainWindow(x, y, title)
        return window

    def on_close(self):
        pyglet.app.exit()

    def on_draw(self):
        self.clear()

        self.batch.draw()

    def load_theme(self):
        # Load theme from json document /theme/theme.json
        with open(os.path.join(CWD, 'theme/theme.json'), 'r') as f:
            theme_json = json.load(f)

            # Setup GUI theme
            self.theme = Theme(theme_json,
                               resources_path=os.path.join(CWD, 'theme'))

    def load_elements(self):
        sidebar_vlay = VerticalContainer(content=[Label('Vlay')])
        projection = GridContainer(content=[[Label('Grid')]])
        main_hlay = HorizontalContainer(content=[projection,
                                                 sidebar_vlay])

        Manager(main_hlay, window=self, batch=self.batch, theme=self.theme)
