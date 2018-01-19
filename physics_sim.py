"""
Do some physics simulation things you know? ---Testing---pls---ignore---
"""

import pyglet
import pyglet_gui.theme
import pyglet_gui.manager
import pyglet_gui.gui

import main_interface


class gfx_context:
    def __init__(self, window, theme, batch):
        self.window = window
        self.theme = theme
        self.batch = batch

if __name__ == '__main__':
    # Setup application window
    window = pyglet.window.Window(1600, 900,
                                  resizable=True,
                                  caption='Simity sim sim')

    window.set_minimum_size(700, 400)

    # Setup GUI theme
    theme = pyglet_gui.theme.Theme({'font': 'Arial',
                                    'font_size': 12,
                                    'text_color': [255, 255, 255, 255]
                                    }, resources_path='')

    # Create graphics batch
    batch = pyglet.graphics.Batch()

    # Setup draw event to render each frame
    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    # Create graphics context
    gfx_context = gfx_context(window=window, theme=theme, batch=batch)

    # Add UI to batch
    main_interface.create_ui(gfx_context)

    # Start application
    pyglet.app.run()
