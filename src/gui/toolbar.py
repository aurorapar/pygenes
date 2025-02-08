from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.actionbar import ActionBar

from gui.toolbar_view import ToolbarView


class ToolbarWidget(ActionBar):

    LAYOUT_HEIGHT = 25
    COLOR = [.5, .5, .5, 1]

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(ToolbarWidget, self).__init__(**kwargs)

        with self.canvas.before:
            Color(*ToolbarWidget.COLOR)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=[self.size[0], ToolbarWidget.LAYOUT_HEIGHT])

        self.bind(size=self._update_rect, pos=self._update_rect)
        toolbar = ToolbarView()
        self.add_widget(toolbar)
        toolbar.padding = [0,0,625,0]


    def _update_rect(self, instance, value):
        self.rect.pos = (0, Window.height - ToolbarWidget.LAYOUT_HEIGHT)
        self.rect.size = (value[0], ToolbarWidget.LAYOUT_HEIGHT)
