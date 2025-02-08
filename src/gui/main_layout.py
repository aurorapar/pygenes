import os

from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, PushMatrix, Rotate, PopMatrix
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout

from gui.toolbar import ToolbarWidget


class MainLayout(AnchorLayout):

    COLOR = [.1, .1, .1, 1]
    BACKGROUND_IMAGE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'res', 'dna.png')

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(MainLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(*MainLayout.COLOR)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=Window.size)

        self.bind(size=self._size_update_listener)
        toolbar = ToolbarWidget()
        self.add_widget(toolbar)

        background_image = Image(source=MainLayout.BACKGROUND_IMAGE, pos=[325,250])
        with background_image.canvas.before:
            PushMatrix()
            Rotate(angle=-30, axis=(0, 0, 1), origin=background_image.center)
        with background_image.canvas.after:
            PopMatrix()

        self.add_widget(background_image)
        background_image.pos = [0, 500]

    def _size_update_listener(self, instance, value):
        self.rect.size = Window.size