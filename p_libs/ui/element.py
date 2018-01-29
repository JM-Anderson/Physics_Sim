from abc import ABC, abstractmethod
from pyglet_gui.constants import *


class GUIElement(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def viewer(self):
        pass

    default_settings = {'is_movable': False,
                        'anchor': ANCHOR_CENTER}

    @abstractmethod
    def manager_settings(self):
        return self.default_settings
