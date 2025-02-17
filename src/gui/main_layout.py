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
        self.controller = MainController(self)
        self.size = Window.size
        self.reset_default_layout()
        self._add_toolbar()

    def reset_default_layout(self):
        with self.canvas.before:
            Color(*MainLayout.COLOR)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=Window.size)
            self.rect.pos = self.pos
        self.bind(size=self.controller.adjust_size)

        self._set_background()
        self._add_new_button()

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
        toolbar = ToolbarWidget(self.controller)
        self.add_widget(toolbar)
        self.toolbar = toolbar

    def _add_new_button(self):
        new_button_layout = NewFamilyLineLayout(self.controller)
        self.add_widget(new_button_layout)
        self.new_button = new_button_layout


class MainController:

    def __init__(self, layout):
        self.layout = layout

    def adjust_size(self, instance, value):
        self.layout.rect.size = Window.size
        self.layout.rect.pos = self.layout.pos
        self.layout.background_image.size = self.layout.size
        self.layout.new_button.reposition()

    def reset_canvas(self):
        for layout_child in self.layout.children:
            self.layout.remove_widget(layout_child)
        self.layout.remove_widget(self.layout.new_button)
        self.layout.toolbar = None
        self.layout.new_button = None
        self.layout.reset_default_layout()