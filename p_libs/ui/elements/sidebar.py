from pyglet_gui.containers import HorizontalContainer as HoriCont, VerticalContainer as VertCont, GridContainer as GridCont, Spacer
from pyglet_gui.buttons import OneTimeButton, Button, Checkbox
from pyglet_gui.gui import Label, Frame

from p_libs.ui.element import GUIElement, get_theme


class sidebar(GUIElement):

    override_settings = {
        'anchor': (0, 1)
    }

    def __init__(self):
        self.material_settings = {
            'gravity': False
        }

    def viewer(self):
        elements = []

        elements.append(Label('Customize Material'))
        elements.append(Checkbox('Has gravity',
                                 on_press=lambda x: self.apply('gravity', x)))

        label = Frame(VertCont(elements, padding=20))

        return label

    def apply(self, setting, val):
        self.material_settings[setting] = val
