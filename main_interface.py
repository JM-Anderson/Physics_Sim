"""
Draws main interface elements
"""
from pyglet_gui.buttons import Button
from pyglet_gui.gui import Label
from pyglet_gui.manager import Manager


def handle_button():
    print('runs')


def create_ui(gfx_context):
    button = Label('Press me')
    manager = Manager(button,
                      window=gfx_context.window,
                      batch=gfx_context.batch,
                      theme=gfx_context.theme)
