from pyglet_gui.containers import HorizontalContainer as HoriCont, VerticalContainer as VertCont, GridContainer as GridCont, Spacer
from pyglet_gui.buttons import OneTimeButton, Button, Checkbox
from pyglet_gui.gui import Label, Frame

from p_libs.ui.element import GUIElement, get_theme


class sidebar(GUIElement):
    override_settings = {
        'anchor': (0, 1)
    }

    def viewer(self):
        label = Frame(VertCont([Label('Customize Material'),
                                Checkbox('Has gravity')],
                               padding=20))

        return label
