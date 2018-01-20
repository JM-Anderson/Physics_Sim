"""
Do some physics simulation things you know?
"""

import pyglet
from pyglet_gui.theme import Theme
import pyglet_gui.manager
import pyglet_gui.gui
from pyglet.gl import *

import p_libs.main_interface as main_interface

import json
import os

CWD = os.getcwd()


class gfx_context:
    def __init__(self, window, theme, batch):
        self.window = window
        self.theme = theme
        self.batch = batch

if __name__ == '__main__':
    # Setup application window
    window = pyglet.window.Window(800, 450,
                                  resizable=True,
                                  caption='Simity sim sim')

    window.set_minimum_size(700, 400)

    # Load theme from json document /theme/theme.json
    with open(os.path.join(CWD, 'theme/theme.json'), 'r') as f:
        theme_json = json.load(f)

        # Setup GUI theme
        theme = Theme(theme_json, resources_path=os.path.join(CWD, 'theme'))

    # Create graphics batch
    batch = pyglet.graphics.Batch()
    
    # Setup draw event to render each frame
    @window.event
    def on_draw():
        window.clear()

        batch.draw()

    # Create graphics context
    gfx_context = gfx_context(window,
                              theme,
                              batch)

    # Add UI to batch
    main_interface.create_ui(gfx_context)

    # Start application
    pyglet.app.run()
