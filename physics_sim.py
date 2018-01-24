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

if __name__ == '__main__':
    window1 = MainWindow.load_window(800, 450, 'Simity sim sim')
    window2 = MaterialDisplay.load_window(400, 400)
    pyglet.app.run()
