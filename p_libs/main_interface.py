"""
Draws main interface elements
"""
from pyglet_gui.buttons import Button
from pyglet_gui.gui import Label
from pyglet_gui.manager import Manager

import p_libs.material_display


def handle_button(arg):
    print('runs')
    print(arg)


def create_ui(gfx_context):
    button = Button('Press me', on_press=handle_button)
    manager = Manager(button,
                      window=gfx_context.window,
                      batch=gfx_context.batch,
                      theme=gfx_context.theme)
    p_libs.material_display.MaterialDisplay.load_window()


def material_creation_ui():
    vlay = VerticalContainer()

    return vlay
