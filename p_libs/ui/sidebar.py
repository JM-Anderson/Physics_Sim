from pyglet_gui.containers import HorizontalContainer as HoriCont, VerticalContainer as VertCont, GridContainer as GridCont
from pyglet_gui.buttons import Button


def sidebar_create():
    hlay = HoriCont(content=[VertCont(content=[Button("(1, 1)"),
                                               Button("(1, 2)")]),
                             VertCont(content=[Button("(2, 1)"),
                                               Button("(2, 2)")])])

    grid = GridCont([[Button("(1,1)"), Button("(1,2)")],
                     [Button("(2,1)"), Button("(2,2)")]])

    vlay = VertCont([hlay, grid])

    return vlay
