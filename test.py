import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *

from pyglet_gui.theme import Theme
from pyglet_gui.gui import Label
from pyglet_gui.manager import Manager

import os
import json

WINDOW = 400
INCREMENT = 5
CWD = os.getcwd()


class Window(pyglet.window.Window):

    # Cube 3D start rotation
    xRotation = yRotation = 30

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title)
        self.batch = pyglet.graphics.Batch()
        self.ui_batch = pyglet.graphics.Batch()
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)

        with open(os.path.join(CWD, 'theme/theme.json'), 'r') as f:
            theme_json = json.load(f)

            self.theme = Theme(theme_json,
                               resources_path=os.path.join(CWD, 'theme'))

        primitive.cube2_batchmode(self.batch)
        label = Label('Press me')

        manager = Manager(label,
                          window=self,
                          batch=self.ui_batch,
                          theme=self.theme)
        label.set_position(10, 10)

    def on_draw(self):
        # Clear the current GL Window
        self.clear()

        glLoadIdentity()

        # Push Matrix onto stack
        glPushMatrix()

        glTranslatef(0, 0, -400)
        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        #self.batch.draw()
        # primitive.cube2()

        # Pop Matrix off stack
        glPopMatrix()

        #glTranslatef(0, 0, -310)
        self.ui_batch.draw()

    def on_resize(self, width, height):
        # set the Viewport
        glViewport(0, 0, width, height)

        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 1000)

        glMatrixMode(GL_MODELVIEW)

    def on_text_motion(self, motion):
        if motion == key.UP:
            self.xRotation -= INCREMENT
        elif motion == key.DOWN:
            self.xRotation += INCREMENT
        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
        elif motion == key.RIGHT:
            self.yRotation += INCREMENT


class primitive:
    @staticmethod
    def cube1():
        glBegin(GL_QUADS)

        # ---QUAD #1---
        glColor3ub(255, 0, 0)
        glVertex3f(50, 50, 50)
        glVertex3f(50, -50, 50)
        glVertex3f(-50, -50, 50)
        glVertex3f(-50, 50, 50)

        # ---QUAD #2---
        glColor3ub(255, 255, 0)
        glVertex3f(50, 50, -50)
        glVertex3f(50, -50, -50)
        glVertex3f(-50, -50, -50)
        glVertex3f(-50, 50, -50)

        # ---QUAD #3---
        glColor3ub(128, 128, 128)
        glVertex3f(50, -50, -50)
        glVertex3f(50, -50, 50)
        glVertex3f(50, 50, 50)
        glVertex3f(50, 50, -50)

        # ---QUAD #4---
        glColor3ub(255, 0, 255)
        glVertex3f(-50, -50, -50)
        glVertex3f(-50, -50, 50)
        glVertex3f(-50, 50, 50)
        glVertex3f(-50, 50, -50)

        # ---QUAD #5---
        glColor3ub(0, 0, 255)
        glVertex3f(-50, 50, -50)
        glVertex3f(50, 50, -50)
        glVertex3f(50, 50, 50)
        glVertex3f(-50, 50, 50)

        # ---QUAD #6---
        glColor3ub(255, 255, 255)
        glVertex3f(-50, -50, -50)
        glVertex3f(50, -50, -50)
        glVertex3f(50, -50, 50)
        glVertex3f(-50, -50, 50)

        glEnd()

    @staticmethod
    def cube2():
        pyglet.graphics.draw_indexed(8, GL_TRIANGLE_STRIP,
                                     [5, 4, 6, 7, 3, 4, 0,
                                      5, 1, 6, 2, 3, 1, 0],
                                     ('v3i', (50, 50, 50,
                                              -50, 50, 50,
                                              -50, -50, 50,
                                              50, -50, 50,
                                              50, 50, -50,
                                              -50, 50, -50,
                                              -50, -50, -50,
                                              50, -50, -50)),
                                     ('c3B', (0, 255, 0,
                                              255, 128, 128,
                                              0, 0, 255,
                                              255, 255, 0,
                                              0, 255, 255,
                                              255, 0, 255,
                                              255, 0, 0,
                                              255, 255, 255)))

    @staticmethod
    def cube2_batchmode(batch):
        vertex_list = batch.add_indexed(8, GL_TRIANGLE_STRIP, None,
                                     [5, 4, 6, 7, 3, 4, 0,
                                      5, 1, 6, 2, 3, 1, 0],
                                     ('v3i', (50, 50, 50,
                                              -50, 50, 50,
                                              -50, -50, 50,
                                              50, -50, 50,
                                              50, 50, -50,
                                              -50, 50, -50,
                                              -50, -50, -50,
                                              50, -50, -50)),
                                     ('c3B', (0, 255, 0,
                                              255, 128, 128,
                                              0, 0, 255,
                                              255, 255, 0,
                                              0, 255, 255,
                                              255, 0, 255,
                                              255, 0, 0,
                                              255, 255, 255)))
if __name__ == '__main__':
    Window(WINDOW, WINDOW, 'Pyglet Colored Cube')
    pyglet.app.run()
