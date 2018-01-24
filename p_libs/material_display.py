import pyglet
from pyglet.gl import *
from pyglet.window import key, mouse

from p_libs.easy_graphics import primitives

WINDOW = 400
KEY_SENSITIVITY = 1
MOUSE_SENSITIVITY = 1
SCROLL_SENSITVITY = 10
MAX_ZOOM_DIST = -200
MIN_ZOOM_DIST = 10000


# Custom Material Display Window - extends pyglet.window.Window
class MaterialDisplay(pyglet.window.Window):

    # Cube 3D start rotation and start zoom
    xRotation = yRotation = 30
    zDepth = -400

    def __init__(self, width, height, title=''):
        super(MaterialDisplay, self).__init__(width, height, title)

        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)

        # Create batch
        self.batch = pyglet.graphics.Batch()

        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)

        # Add cube to batch
        primitives.Primitives.cube_batchmode(self.batch)

    @staticmethod
    def load_window():
        window = MaterialDisplay(WINDOW, WINDOW, 'Custom Material')
        pyglet.clock.schedule_interval(window.update, 1/120.0)
        pyglet.app.run()

    def on_draw(self):
        # Clear the current GL Window
        self.clear()

        # Reset Matrix
        glLoadIdentity()

        # Push Matrix onto stack
        glPushMatrix()

        # Apply zoom
        glTranslatef(0, 0, self.zDepth)

        # Rotate matrix according to user input
        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        # Draw whole batch
        self.batch.draw()

        # Pop Matrix off stack
        glPopMatrix()

    def on_resize(self, width, height):
        # set the Viewport
        glViewport(0, 0, width, height)

        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # Set up perspective
        # (gluPerspective is deprecated, but I could find
        # no resources pointing to a non-trivial alternative)
        aspectRatio = width / height
        gluPerspective(35, aspectRatio, 1, 10000)

        glMatrixMode(GL_MODELVIEW)

    def update(self, dt):
        if self.keys[key.LEFT]:
            self.yRotation -= KEY_SENSITIVITY
        if self.keys[key.RIGHT]:
            self.yRotation += KEY_SENSITIVITY
        if self.keys[key.UP]:
            self.xRotation -= KEY_SENSITIVITY
        if self.keys[key.DOWN]:
            self.xRotation += KEY_SENSITIVITY

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        # Bitwise operation with `buttons` holding info for each mouse button
        if buttons & mouse.LEFT:
            self.xRotation -= dy * MOUSE_SENSITIVITY
            self.yRotation += dx * MOUSE_SENSITIVITY
        elif buttons & mouse.MIDDLE:
            self.zDepth += dy

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if scroll_y > 0 and self.zDepth >= MAX_ZOOM_DIST:
            self.zDepth = MAX_ZOOM_DIST
        elif scroll_y < 0 and self.zDepth <= MIN_ZOOM_DIST:
            self.zDepth = MIN_ZOOM_DIST
        else:
            self.zDepth += scroll_y * SCROLL_SENSITVITY
