from abc import ABC, abstractmethod
from pyglet_gui.constants import *
from pyglet_gui.theme import Theme

import os
import json

CWD = os.getcwd()


def get_theme():
        # Load theme from json document /theme/theme.json
        with open(os.path.join(CWD, 'theme/theme.json'), 'r') as f:
            theme_json = json.load(f)

            return dict(theme_json)


class GUIElement(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def viewer(self):
        pass

    default_settings = {
        'is_movable': False,
        'anchor': ANCHOR_CENTER
    }
    override_settings = {}
    override_theme = {}

    def theme(self):
        theme = dict(get_theme())
        for rule, val in self.override_theme.items():
            theme[rule] = val

        return theme

    def manager_settings(self):
        settings = dict(self.default_settings)

        # Load settings from default if not manually defined
        for rule, val in self.override_settings.items():
            settings[rule] = val

        settings['theme'] = Theme(self.theme(),
                                  resources_path=os.path.join(CWD, 'theme'))

        return settings
