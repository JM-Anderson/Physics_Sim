from pyglet_gui.containers import HorizontalContainer as HoriCont, VerticalContainer as VertCont, GridContainer as GridCont, Spacer
from pyglet_gui.buttons import OneTimeButton, Button, Checkbox, GroupButton
from pyglet_gui.option_selectors import Dropdown, VerticalButtonSelector
from pyglet_gui.sliders import HorizontalSlider as HoriSlide
from pyglet_gui.text_input import TextInput
from pyglet_gui.gui import Label, Frame

from p_libs.ui.element import GUIElement, get_theme


class sidebar(GUIElement):

    override_settings = {
        'anchor': (0, 1)
    }

    override_theme = {
        "input": {
            "highlight": {
                "image": {
                    "source": "input-highlight.png"
                }
            },
            "focus": {
                "image": {
                    "source": "input-highlight.png"
                }
            },
            "focus_color": [0, 0, 200, 64],
            "image": {
                "source": "input.png",
                "frame": [3, 3, 2, 2],
                "padding": [10, 5, 2, 3]
            }
        }
    }

    def viewer(self):
        elems = {}

        # Title
        elems['title'] = Label('Customize Material')

        # Particle shape setting
        elems['shape'] = HoriCont([
            GroupButton(group_id='shape',
                        label='Circle',
                        is_pressed=True),
            GroupButton(group_id='shape',
                        label='Square')
        ])

        # Size setting
        """ Temporarily removed to work on same-size optimization
        r_display = Label('3.0 m')
        r_slider = HoriSlide(on_set=lambda x: self.lbl_slider(x,
                                                              r_display,
                                                              after=' m'),
                             min_value=1,
                             max_value=10,
                             value=3)

        elems['radius'] = HoriCont([r_display, r_slider])
        """

        # Mass setting
        m_display = Label('1.00 kg')
        m_slider = HoriSlide(on_set=lambda x: self.lbl_slider(x,
                                                              m_display,
                                                              digits=4,
                                                              after=' kg'),
                             min_value=1,
                             max_value=100,
                             value=1)
        elems['mass'] = HoriCont([m_display, m_slider])

        # Color setting
        red_in = TextInput(' 255',
                           length=4,
                           max_length=4,
                           on_input=lambda x: self.color_input(x,
                                                               'red',
                                                               red_in))
        green_in = TextInput(' 0',
                             length=4,
                             max_length=4,
                             on_input=lambda x: self.color_input(x,
                                                                 'green',
                                                                 green_in))
        blue_in = TextInput(' 0',
                            length=4,
                            max_length=4,
                            on_input=lambda x: self.color_input(x,
                                                                'blue',
                                                                blue_in))
        elems['color'] = HoriCont([red_in, green_in, blue_in])

        # Gravity setting
        elems['gravity'] = Checkbox('Has gravity', is_pressed=True)

        self.elems = elems

        sidebar = Frame(VertCont(self.get_elem_list(), padding=20))

        return sidebar

    @staticmethod
    def lbl_slider(pos, display, digits=3, after=''):
        out = str(pos)[:digits]
        if len(out) < digits and '.' in out:
            out += '0' * (digits - len(out))
        display.set_text(out + after)

    last_color = {
        'red': 255,
        'green': 0,
        'blue': 0
    }

    def color_input(self, text, color_chan, text_box):
        if text != '':
            if text[0] == ' ':
                num = text[1:]
            else:
                num = str(text)

            if num.isdigit() and 0 <= int(num) <= 255:
                text_box.set_text(' ' + num)
                self.last_color[color_chan] = int(num)
                return

        text_box.set_text(' ' + str(self.last_color[color_chan]))

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
        for button in self.elems['shape'].content:
            if button.is_pressed:
                settings['shape'] = button.label.lower()
                shape_selected = True
        if not shape_selected:
            return None

        # Get radius setting from slider
        settings['radius'] = 9
        """ Temporarily removed
        settings['radius'] = self.elems['radius'].content[1].value
        """

        # Get mass from slider
        settings['mass'] = self.elems['mass'].content[1].value

        # Get color settings
        settings['color'] = self.last_color.values()

        return settings
