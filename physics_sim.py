"""
Do some physics simulation things you know?
"""

import pyglet
from pyglet_gui.theme import Theme
import pyglet_gui.manager
import pyglet_gui.gui
from pyglet.gl import *

from p_libs.main_interface import MainWindow
from p_libs.material_display import MaterialDisplay

MAIN_WINDOW_SIZE = [800, 450]
MATERIAL_WINDOW_SIZE = [400, 400]


def translate_window(window, dx, dy):
    x, y = window.get_location()
    window.set_location(x + dx, y + dy)

if __name__ == '__main__':
    # Windows are loaded in the order they are created
    # The first windows will appear on bottom

    # By default the Windows OS will cascade window position

    window1 = MainWindow.load_window(MAIN_WINDOW_SIZE[0],
                                     MAIN_WINDOW_SIZE[1],
                                     'Simity sim sim')
    window2 = MaterialDisplay.load_window(MATERIAL_WINDOW_SIZE[0],
                                          MATERIAL_WINDOW_SIZE[1])
    translate_window(window2, MAIN_WINDOW_SIZE[0], 0)

    pyglet.app.run()
