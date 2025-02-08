from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, PushMatrix, Rotate, PopMatrix
from kivy.uix.anchorlayout import AnchorLayout

from gui.toolbar import ToolbarWidget


class MainLayout(AnchorLayout):

    COLOR = [.1, .1, .1, 1]

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(MainLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(*MainLayout.COLOR)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=Window.size)

        self.bind(size=self._size_update_listener)
        toolbar = ToolbarWidget()
        self.add_widget(toolbar)

    def _size_update_listener(self, instance, value):
        self.rect.size = Window.size