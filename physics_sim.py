"""
Do some physics simulation things you know?
"""

import pyglet
from pyglet_gui.theme import Theme
import pyglet_gui.manager
import pyglet_gui.gui
from pyglet.gl import *

from p_libs.ui.windows import main_interface, material_display

MAIN_WINDOW_SIZE = [800, 450]
MATERIAL_WINDOW_SIZE = [400, 400]


def translate_window(window, dx, dy):
    x, y = window.get_location()
    window.set_location(x + dx, y + dy)

if __name__ == '__main__':
    # Windows are loaded in the order they are created
    # The first windows will appear on bottom

    # By default the Windows OS will cascade window position

    window1 = main_interface.MainWindow.load_window(MAIN_WINDOW_SIZE[0],
                                                    MAIN_WINDOW_SIZE[1],
                                                    'Simity sim sim')

    window2 = material_display.MaterialDisplay.load_window(MATERIAL_WINDOW_SIZE[0],
                                                           MATERIAL_WINDOW_SIZE[1])
    translate_window(window2, MAIN_WINDOW_SIZE[0], 0)

    pyglet.app.run()
