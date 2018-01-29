from pyglet_gui.containers import HorizontalContainer as HoriCont, VerticalContainer as VertCont, GridContainer as GridCont
from pyglet_gui.buttons import Button
from pyglet_gui.gui import Label

from p_libs.ui.element import GUIElement

from abc import ABC, abstractmethod


class sidebar(GUIElement):
    def viewer(self):
        return Label('hi der')

    def manager_settings(self):
        super().manager_settings()
"""
def sidebar_create():
    hlay = HoriCont(content=[VertCont(content=[Button("(1, 1)"),
                                               Button("(1, 2)")]),
                             VertCont(content=[Button("(2, 1)"),
                                               Button("(2, 2)")])])

    grid = GridCont([[Button("(1,1)"), Button("(1,2)")],
                     [Button("(2,1)"), Button("(2,2)")]])

    vlay = VertCont([hlay, grid])

    return vlay
"""
