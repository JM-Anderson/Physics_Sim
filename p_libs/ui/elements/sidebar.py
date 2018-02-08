from pyglet_gui.containers import HorizontalContainer as HoriCont, VerticalContainer as VertCont, GridContainer as GridCont, Spacer
from pyglet_gui.buttons import OneTimeButton, Button, Checkbox, GroupButton
from pyglet_gui.option_selectors import Dropdown, VerticalButtonSelector
from pyglet_gui.sliders import HorizontalSlider
from pyglet_gui.gui import Label, Frame

from p_libs.ui.element import GUIElement, get_theme


class sidebar(GUIElement):

    override_settings = {
        'anchor': (0, 1)
    }

    def viewer(self):
        elems = {}

        # Title
        elems['title'] = Label('Customize Material')

        # Particle shape setting
        elems['shape'] = [GroupButton(group_id='shape',
                                      label='Circle',
                                      is_pressed=True),
                          GroupButton(group_id='shape',
                                      label='Square')]

        # Size setting
        display = Label('3')
        slider = HorizontalSlider(on_set=lambda x: self.rad_slider(x, display),
                                  min_value=1,
                                  max_value=10,
                                  value=3)

        elems['radius'] = HoriCont([display, slider])

        # Gravity setting
        elems['gravity'] = Checkbox('Has gravity', is_pressed=True)

        self.elems = elems

        sidebar = Frame(VertCont(self.get_elem_list(), padding=20))

        return sidebar

    def rad_slider(self, pos, display):
        out = str(pos)[:3]
        if out == '10.0':
            out = '10'
        display.set_text(out)

    def get_elem_list(self):
        l = []
        for elem in self.elems.values():
            if isinstance(elem, list):
                for elem2 in elem:
                    l.append(elem2)
            else:
                l.append(elem)

        return l

    def get_settings(self):
        settings = {}

        # Get gravity setting from checkbox
        settings['gravity'] = self.elems['gravity'].is_pressed

        # Get shape setting from buttons
        shape_selected = False
        for button in self.elems['shape']:
            if button.is_pressed:
                settings['shape'] = button.label.lower()
                shape_selected = True
        if not shape_selected:
            return None

        # Get radius setting from slider
        settings['radius'] = self.elems['radius'].content[1].value

        return settings
