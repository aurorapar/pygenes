import os

from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, PushMatrix, Rotate, PopMatrix
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout

from gui.buttons import NewFamilyLineLayout
from gui.toolbar import ToolbarWidget
from gui.theme import MAIN_COLOR, FOREGROUND_COLOR

from translations import Translator, TRANSLATION

translator = Translator()

class MainLayout(AnchorLayout):

    COLOR = MAIN_COLOR
    BACKGROUND_IMAGE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'res', 'dna.png')

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(MainLayout, self).__init__(**kwargs)
        self.size = Window.size

        with self.canvas.before:
            Color(*MainLayout.COLOR)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=Window.size)
            self.rect.pos = self.pos
        self.bind(size=self._size_listener)

        self._add_toolbar()
        self._set_background()

        self._add_new_button()

    def _size_listener(self, instance, value):
        self.rect.size = Window.size
        self.rect.pos = self.pos
        self.background_image.size = self.size
        self.new_button.reposition()

    def _set_background(self):
        background_image = Image(source=MainLayout.BACKGROUND_IMAGE, pos=[325, 250])
        background_image.size_hint = [None, None]
        background_image.size = self.size
        with background_image.canvas.before:
            PushMatrix()
            Rotate(angle=-30, axis=(0, 0, 1), origin=self.center)
        with background_image.canvas.after:
            PopMatrix()

        self.add_widget(background_image)
        self.background_image = background_image
        background_image.pos = [0, -500]

    def _add_toolbar(self):
        toolbar = ToolbarWidget()
        self.add_widget(toolbar)
        self.toolbar = toolbar

    def _add_new_button(self):
        new_button_layout = NewFamilyLineLayout()
        self.add_widget(new_button_layout)
        self.new_button = new_button_layout


